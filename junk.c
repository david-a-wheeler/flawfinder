
#include <stdio.h>

main() {
	 char abuf[1000];
	 FILE *FR = stdin;
	 fscanf(FR, "%2000s", abuf);
	 printf("Result = %s\n", abuf);
}
