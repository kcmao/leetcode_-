#include "..\Utilities\List.h"
#include<stdio.h>
#include<stack>

//ʹ�����鱣���������ÿ��ֵ
void PrintListUseArray(ListNode* pHead)
{
	if (pHead == nullptr)
	{
		return;
	}
	int nodeNumber = 1;

	ListNode* pNode = pHead;
	while (pNode->next != nullptr)
	{
		nodeNumber++;
		pNode = pNode->next;
	}
	int *nodeValueArray;
    nodeValueArray = new int[nodeNumber];

	pNode = pHead;
	int j = 0;
	while (pNode != nullptr)
	{	
		nodeValueArray[j] = pNode->value;
		pNode = pNode->next;
		j++;
	}


	for (int j = nodeNumber-1; j >= 0; j--)
	{
		printf("%d\t", nodeValueArray[j]);

	}

}

//ʹ��һ��ջ
void PrintListReversingly_Iteratively(ListNode* pHead)
{
	std::stack<ListNode*> nodes;
	ListNode* pNode = pHead;
	while (pNode != nullptr)
	{
		nodes.push(pNode);
		pNode = pNode->next;
	}
	while (!nodes.empty())
	{
		pNode = nodes.top();
		printf("%d\t", pNode->value);
		nodes.pop();
	}

}

//ʹ�õݹ�
void PrintListReversingly_Recursively(ListNode* pHead)
{
	if (pHead != nullptr)
	{
		if (pHead->next != nullptr)
		{
			PrintListReversingly_Recursively(pHead->next);
		}
		printf("%d\t", pHead->value);
	}
}


// ====================���Դ���====================
void Test(ListNode* pHead)
{
	PrintList(pHead);
	PrintListUseArray(pHead);
	printf("\n");
	PrintListReversingly_Iteratively(pHead);
	printf("\n");
	PrintListReversingly_Recursively(pHead);
}

// 1->2->3->4->5
void Test1()
{
	printf("\nTest1 begins.\n");

	ListNode* pNode1 = CreateListNode(1);
	ListNode* pNode2 = CreateListNode(2);
	ListNode* pNode3 = CreateListNode(3);
	ListNode* pNode4 = CreateListNode(4);
	ListNode* pNode5 = CreateListNode(5);

	ConnectListNodes(pNode1, pNode2);
	ConnectListNodes(pNode2, pNode3);
	ConnectListNodes(pNode3, pNode4);
	ConnectListNodes(pNode4, pNode5);

	Test(pNode1);

	DestroyList(pNode1);
}

// ֻ��һ����������: 1
void Test2()
{
	printf("\nTest2 begins.\n");

	ListNode* pNode1 = CreateListNode(1);

	Test(pNode1);

	DestroyList(pNode1);
}

// ������
void Test3()
{
	printf("\nTest3 begins.\n");

	Test(nullptr);
}

int main(int argc, char* argv[])
{
	Test1();
	Test2();
	Test3();

	return 0;
}

