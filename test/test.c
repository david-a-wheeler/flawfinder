/* Test flawfinder.  This program won't compile or run; that's not necessary
   for this to be a useful test. */

#include <stdio.h>
#define hello(x) goodbye(x)
#define WOKKA "stuff"

main() {
 printf("hello\n");
}

/* This is a strcpy test. */

int demo(char *a, char *b) {
 strcpy(a, "\n"); // Did this work?
 strcpy(a, gettext("Hello there")); // Did this work?
 strcpy(b, a);
 sprintf(s, "\n");
 sprintf(s, "hello");
 sprintf(s, "hello %s", bug);
 sprintf(s, gettext("hello %s"), bug);
 sprintf(s, unknown, bug);
 printf(bf, x);
 scanf("%d", &x);
 scanf("%s", s);
 scanf("%10s", s);
 scanf("%s", s);
 gets(f); // Flawfinder: ignore
 printf("\\");
 /* Flawfinder: ignore */
 gets(f);
 gets(f);
 /* These are okay, but flawfinder version < 0.20 incorrectly used
    the first parameter as the parameter for the format string */
 syslog(LOG_ERR,"cannot open config file (%s): %s",filename,strerror(errno))
 syslog(LOG_CRIT,"malloc() failed");
 /* But this one SHOULD trigger a warning. */
 syslog(LOG_ERR, attacker_string);

}



demo2() {
  char d[20];
  char s[20];
  int n;

  _mbscpy(d,s); /* like strcpy, this doesn't check for buffer overflow */
  memcpy(d,s); // fail - no size
  memcpy(d, s, sizeof(d)); // pass
  memcpy(& n, s, sizeof( n )); // pass
  memcpy(&n,s,sizeof(s)); // fail - sizeof not of destination
  memcpy(d,s,n); // fail - size unguessable
  CopyMemory(d,s);
  lstrcat(d,s);
  strncpy(d,s);
  _tcsncpy(d,s);
  strncat(d,s,10);
  strncat(d,s,sizeof(d)); /* Misuse - this should be flagged as riskier. */
  _tcsncat(d,s,sizeof(d)); /* Misuse - flag as riskier */
  n = strlen(d);
  /* This is wrong, and should be flagged as risky: */
  MultiByteToWideChar(CP_ACP,0,szName,-1,wszUserName,sizeof(wszUserName));
  /* This is also wrong, and should be flagged as risky: */
  MultiByteToWideChar(CP_ACP,0,szName,-1,wszUserName,sizeof wszUserName);
  /* This is much better: */
  MultiByteToWideChar(CP_ACP,0,szName,-1,wszUserName,sizeof(wszUserName)/sizeof(wszUserName[0]));
  /* This is much better: */
  MultiByteToWideChar(CP_ACP,0,szName,-1,wszUserName,sizeof wszUserName /sizeof(wszUserName[0]));
  /* This is an example of bad code - the third paramer is NULL, so it creates
     a NULL ACL.  Note that Flawfinder can't detect when a
     SECURITY_DESCRIPTOR structure is manually created with a NULL value
     as the ACL; doing so would require a tool that handles C/C++
     and knows about types more that flawfinder currently does.
     Anyway, this needs to be detected: */
  SetSecurityDescriptorDacl(&sd,TRUE,NULL,FALSE);
  /* This one is a bad idea - first param shouldn't be NULL */
  CreateProcess(NULL, "C:\\Program Files\\GoodGuy\\GoodGuy.exe -x", "");
  /* Test interaction of quote characters */
  printf("%c\n", 'x');
  printf("%c\n", '"');
  printf("%c\n", '\"');
  printf("%c\n", '\'');
  printf("%c\n", '\177');
  printf("%c\n", '\xfe');
  printf("%c\n", '\xd');
  printf("%c\n", '\n');
  printf("%c\n", '\\');
  printf("%c\n", "'");
}


int getopt_example(int argc,char *argv[]) {
    while ((optc = getopt_long (argc, argv, "a",longopts, NULL )) != EOF) {
    }
}

int testfile() {
  FILE *f;
  f = fopen("/etc/passwd", "r"); 
  fclose(f);
}

/* Regression test: handle \\\n after end of string */

#define assert(x) {\
 if (!(x)) {\
 fprintf(stderr,"Assertion failed.\n"\
 "File: %s\nLine: %d\n"\
 "Assertion: %s\n\n"\
 ,__FILE__,__LINE__,#x);\
 exit(1);\
 };\
 }

int accesstest() {
  int access = 0; /* Not a function call.  Should be caught by the
                     false positive test, and NOT labelled as a problem. */
}

