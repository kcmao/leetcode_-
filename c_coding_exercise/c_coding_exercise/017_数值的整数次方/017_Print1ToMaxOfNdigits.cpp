#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool increment(char* numbers)
{	
	int i = 0;
	int j;
	int n = strlen(numbers);
	for (i = 0; i < n - 1; i++)
	{	
		j = i;
		while (numbers[j] - '0' == '9')
		{
			numbers[j] = '0';
			j += 1;
			numbers[j] = numbers[j] + '1';
		}
		numbers[i] = '0' + '1';
	}
	return true;
}

void print(char* numbers)
{

}
void Print1ToMaxOfNigits_1(int n)
{
	if(n < 0 )
	{
		return; 
	}
	
	char *numbers = (char *)malloc(sizeof(char)*(n + 1));
	memset(numbers, '0', n);
	numbers[n] = '\0';

	while (!increment(numbers))
	{
		print(numbers);
	}

}









int main(int argc, char* argv[])
{
	int a = 2;
	Print1ToMaxOfNigits_1(a);

	return 0;
}