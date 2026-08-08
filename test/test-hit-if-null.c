// test-hit-if-null.c: rules that use the check_for_null hook (FF1046
// CreateProcess, FF1060 SetSecurityDescriptorDacl) must report a null
// argument in the checked position exactly ONCE, and must stay silent
// when that argument is not null.

// --- These should produce exactly ONE hit each ---

void null_dacl(void *sd) {
    SetSecurityDescriptorDacl(sd, 1, NULL, 0);
}

void null_app_name(void) {
    CreateProcess(NULL, "C:\\Program Files\\GoodGuy\\GoodGuy.exe -x", "");
}

// --- These should produce NO hits (checked argument is not null) ---

void real_dacl(void *sd, void *dacl) {
    SetSecurityDescriptorDacl(sd, 1, dacl, 0);
}

void real_app_name(void) {
    CreateProcess("C:\\GoodGuy.exe", "-x", "");
}
