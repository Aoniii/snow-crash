#include <stdio.h>

int main(int argc, char **argv) {
    int i = -1;
	while (argv[1][++i])
		printf("%c", argv[1][i] - i);
	printf("\n");
	return (0);
}
