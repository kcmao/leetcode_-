#include "List.h"
#include <stdio.h>
#include <stdlib.h>

ListNode* CreateListNode(int value)
{
	ListNode* pNode = new ListNode();
	pNode->value = value;
	pNode->next = nullptr;

	return pNode;
}

void ConnectListNodes(ListNode* pCurrent, ListNode* pNext)
{
	if (pCurrent == nullptr)
	{
		printf("Error to connect two nodes.\n");
		exit(1);

	}
	pCurrent->next = pNext;
}

void PrintListNode(ListNode* pNode)
{
	if (pNode == nullptr)
	{
		printf("The node is nullptr\n");
	}
	else
	{
		printf("The key in node is %d.\n", pNode->value);
	}
}

void PrintList(ListNode* pHead)
{
	printf("PrintList starts.\n");
	ListNode* pNode = pHead;
	while (pNode != nullptr)
	{
		printf("%d\t", pNode->value);
		pNode = pNode->next;
	}
	printf("\nPrintList ends.\n");
}

void DestroyList(ListNode *pHead)
{
	ListNode* pNode = pHead;
	delete pNode;
	pNode = pHead;
}


