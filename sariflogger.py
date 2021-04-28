import json
import re

def to_json(o):
    return json.dumps(o, default=lambda o: o.__dict__, sort_keys=False, indent=2)

class SarifLogger(object):
    _hitlist = None
    TOOL_NAME = "Flawfinder"
    TOOL_URL = "https://dwheeler.com/flawfinder/"
    TOOL_VERSION = "2.0.15"
    URI_BASE_ID = "SRCROOT"
    SARIF_SCHEMA = "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json"
    SARIF_SCHEMA_VERSION = "2.1.0"
    CWE_TAXONOMY_NAME = "CWE"
    CWE_TAXONOMY_URI = "https://raw.githubusercontent.com/sarif-standard/taxonomies/main/CWE_v4.4.sarif"
    CWE_TAXONOMY_GUID = "FFC64C90-42B6-44CE-8BEB-F6B7DAE649E5"

    def __init__ (self, hits):
        self._hitlist = hits

    def output_sarif(self):
        tool = {
            "driver": {
                "name": self.TOOL_NAME,
                "version": self.TOOL_VERSION,
                "informationUri": self.TOOL_URL,
                "rules": self._extract_rules(self._hitlist),
                "supportedTaxonomies": [{
                    "name": self.CWE_TAXONOMY_NAME,
                    "guid": self.CWE_TAXONOMY_GUID,
                }],
            }
        }

        runs = [{
            "tool": tool,
            "columnKind": "utf16CodeUnits",
            "results": self._extract_results(self._hitlist),
            "externalPropertyFileReferences": {
                "taxonomies": [{
                    "location": {
                        "uri": self.CWE_TAXONOMY_URI,
                    },
                    "guid": self.CWE_TAXONOMY_GUID,
                }],
            },
        }]

        report = {
            "$schema": self.SARIF_SCHEMA,
            "version": self.SARIF_SCHEMA_VERSION,
            "runs": runs,
        }

        jsonstr = to_json(report)
        return jsonstr

    def _extract_rules(self, hitlist):
        rules = {}
        for hit in hitlist:
            if not hit.ruleid in rules:
                rules[hit.ruleid] = self._to_sarif_rule(hit)
        return list(rules.values())

    def _extract_results(self, hitlist):
        results = []
        for hit in hitlist:
            results.append(self._to_sarif_result(hit))
        return results

    def _to_sarif_rule(self, hit):
        return {
            "id": hit.ruleid,
            "name": "{0}/{1}".format(hit.category, hit.name),
            "shortDescription": {
                "text": self._append_period(hit.warning),
            },
            "defaultConfiguration": {
                "level": self._to_sarif_level(hit.defaultlevel),
            },
            "helpUri": hit.helpuri(),
            "relationships": self._extract_relationships(hit.cwes()),
        }

    def _to_sarif_result(self, hit):
        return {
            "ruleId": hit.ruleid,
            "level": self._to_sarif_level(hit.level),
            "message": {
                "text": self._append_period("{0}/{1}:{2}".format(hit.category, hit.name, hit.warning)),
            },
            "locations": [{
                "physicalLocation": {
                    "artifactLocation": {
                        "uri": self._to_uri_path(hit.filename),
                        "uriBaseId": self.URI_BASE_ID,
                    },
                    "region": {
                        "startLine": hit.line,
                        "startColumn": hit.column,
                        "endColumn": len(hit.context_text) + 1,
                        "snippet": {
                            "text": hit.context_text,
                        }
                    }
                }
            }],
            "fingerprints": {
                "contextHash/v1": hit.fingerprint()
            },
            "rank": self._to_sarif_rank(hit.level),
        }

    def _extract_relationships(self, cwestring):
        # example cwe string "CWE-119!/ CWE-120", "CWE-829, CWE-20"
        relationships = []
        for cwe in re.split(',|/',cwestring):
            cwestr = cwe.strip()
            if cwestr:
                relationship = {
                    "target": {
                        "id": int(cwestr.replace("CWE-", "").replace("!", "")),
                        "toolComponent": {
                            "name": self.CWE_TAXONOMY_NAME,
                            "guid": self.CWE_TAXONOMY_GUID,
                        },
                    },
                    "kinds": [
                        "relevant" if cwestr[-1] != '!' else "incomparable"
                    ],
                }
                relationships.append(relationship)
        return relationships

    @staticmethod
    def _to_sarif_level(level):
        # level 4 & 5
        if level >= 4:
            return "error"
        # level 3
        if level == 3:
            return "warning"
        # level 0 1 2
        return "note"

    @staticmethod
    def _to_sarif_rank(level):
        #SARIF rank  FF Level    SARIF level Default Viewer Action
        #0.0         0           note        Does not display by default
        #0.2         1           note        Does not display by default
        #0.4         2           note        Does not display by default
        #0.6         3           warning     Displays by default, does not break build / other processes
        #0.8         4           error       Displays by default, breaks build/ other processes
        #1.0         5           error       Displays by default, breaks build/ other processes
        return level * 0.2

    @staticmethod
    def _to_uri_path(path):
        return path.replace("\\", "/")

    @staticmethod
    def _append_period(text):
        return text if text[-1] == '.' else text + "."
