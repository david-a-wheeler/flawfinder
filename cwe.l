%{

/* cwe by David A. Wheeler (http://www.dwheeler.com).
   This prints anything of the form CWE-#
*/

#include <stdio.h>
#include <ctype.h>
#include <string.h>

void out(char *text) {
	fputs(text,stdout);
}

void outchar(char c) {
	fputc(c, stdout);
}


%}


%%
CWE-[1-9][0-9]* { out(yytext); outchar('\n'); }
.               { }
\n              { }

%%

