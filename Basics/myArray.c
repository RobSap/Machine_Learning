#include <stdio.h>

int main()
{
//Static
int my_int_array[] = {1, 2, 3, 4, 5, 6};
char my_char_array[] = {'a','b','c','d','e','f'};
char my_char_array2[] = {'g','h','i','j','\0'};
char my_char_array3[] = "hello world";


int i;
int j;

j = sizeof(my_int_array) / sizeof(int);
printf("\nint array\n");
for(i=0; i < j; i++)
{
	printf("%d " ,my_int_array[i]);
}

printf("\nChar array\n");
j = sizeof(my_char_array)/sizeof(char);

for(i=0; i < j; i++)
{
	printf("%c " ,my_char_array[i]);
}

printf("\nChar Array 2 \n");
j = sizeof(my_char_array2)/sizeof(char);

for(i=0; i < j; i++)
{
	printf("%c " ,my_char_array2[i]);
}

printf("\nChar array 3 \n");
j = sizeof(my_char_array3)/sizeof(char);

for(i=0; i < j; i++)
{
	printf("%c" ,my_char_array3[i]);
}

printf("\n");


}
