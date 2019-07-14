// ������5���滻�ո�
// ��Ŀ����ʵ��һ�����������ַ����е�ÿ���ո��滻��"%20"���������롰We are happy.����
// �������We%20are%20happy.����

#include <stdio.h>
#include <string.h>

//====================��Ŀ���=====================
/*length Ϊ�ַ�����str�������������ڻ�����ַ���str��ʵ�ʳ���*/
void ReplaceBlank(char str[], int length)
{
	if (str == nullptr || length <= 0)
	{
		return;
	}
	/*����ԭʼ�ַ�������*/
	int originLength = 0;
	int number_blank = 0;
	int i = 0;
	while (str[i] != '\0')
	{
		originLength++;
		if (str[i] == ' ')
		{
			number_blank++;
		}
		i++;
	}

	/*newlength Ϊ�滻�ո���ַ����µĳ���*/
	int newLength = originLength + number_blank * 2;

	/*���鳤�Ȳ���*/
	if (newLength > length)
	{
		return;
	}

	/*ʹ������ָ��Ӻ���ǰ����*/
	int indexOrigin = originLength;
	int indexNew = newLength;
	while (indexOrigin >= 0 && indexNew > indexOrigin)
	{	
		if (str[indexOrigin] != ' ')
		{
			str[indexNew--] = str[indexOrigin--];
		}
		else 
		{
			str[indexNew--] = '0';
			str[indexNew--] = '2';
			str[indexNew--] = '%';

			indexOrigin--;

		}
		
	}



}

// ====================���Դ���====================
//�㲻��Ϊʲô��һ��Ҫ��const����
void Test(const char* testName, char str[], int length, const char expected[])
{
	if (testName != nullptr)
		printf("%s begins: ", testName);

	ReplaceBlank(str, length);

	if (expected == nullptr && str == nullptr)
		printf("passed.\n");
	else if (expected == nullptr && str != nullptr)
		printf("failed.\n");
	else if (strcmp(str, expected) == 0)
		printf("passed.\n");
	else
		printf("failed.\n");
}

// �ո��ھ����м�
void Test1()
{
	const int length = 100;

	char str[length] = "hello world";
	Test("Test1", str, length, "hello%20world");
}

// �ո��ھ��ӿ�ͷ
void Test2()
{
	const int length = 100;

	char str[length] = " helloworld";
	Test("Test2", str, length, "%20helloworld");
}

// �ո��ھ���ĩβ
void Test3()
{
	const int length = 100;

	char str[length] = "helloworld ";
	Test("Test3", str, length, "helloworld%20");
}

// �����������ո�
void Test4()
{
	const int length = 100;

	char str[length] = "hello  world";
	Test("Test4", str, length, "hello%20%20world");
}

// ����nullptr
void Test5()
{
	Test("Test5", nullptr, 0, nullptr);
}

// ��������Ϊ�յ��ַ���
void Test6()
{
	const int length = 100;

	char str[length] = "";
	Test("Test6", str, length, "");
}

//��������Ϊһ���ո���ַ���
void Test7()
{
	const int length = 100;

	char str[length] = " ";
	Test("Test7", str, length, "%20");
}

// ������ַ���û�пո�
void Test8()
{
	const int length = 100;

	char str[length] = "helloworld";
	Test("Test8", str, length, "helloworld");
}

// ������ַ���ȫ�ǿո�
void Test9()
{
	const int length = 100;

	char str[length] = "   ";
	Test("Test9", str, length, "%20%20%20");
}

int main(int argc, char* argv[])
{
	Test1();
	Test2();
	Test3();
	Test4();
	Test5();
	Test6();
	Test7();
	Test8();
	Test9();

	int mkc = getchar();
	return 0;
}