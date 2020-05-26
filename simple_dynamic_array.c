nclude <stdio.h>
# include <stdlib.h>

typedef struct {
	    int *val;
	        int length;
} intArray;

intArray  generateIntArray(int sz) {
		intArray a = {NULL, 0};
			a.val = malloc(sizeof(int) * sz);
				if (a.val == NULL) {
					  		fprintf(stderr, "malloc failed\n");
								}
					a.length = sz;
						return a;
}

intArray resizeIntArray(intArray arr, int sz) {
		arr.val = realloc(arr.val, sz * sizeof(int));
			if (arr.val == NULL) {
				  		fprintf(stderr, "malloc failed\n");
							}
				arr.length = sz;
					return arr;
}

void printIntArray(intArray a) {
		printf("[");
			for (int i = 0; i < a.length; ++i) {
						printf("%d ", a.val[i]);
							}
				printf("]\n");
}

int main () {
		intArray arr = generateIntArray(1);
			arr.val[0] = 1;
				printIntArray(arr);
					arr = resizeIntArray(arr, 2);
						arr.val[1] = 2;
							printIntArray(arr);
								return 0;
}
