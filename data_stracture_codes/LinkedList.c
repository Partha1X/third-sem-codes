// WAP to Create a Linked List
#include<stdio.h>
#include<stdlib.h>

struct node
{
    int info;
    struct node *link;
};

struct node *start = NULL;

void createList()
{
    int item, i, n;
    struct node *tmp, *ptr;

    printf("\nEnter No of Nodes: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        printf("\nEnter Item: ");
        scanf("%d", &item);

        tmp = (struct node *)malloc(sizeof(struct node));
        tmp->info = item;
        tmp->link = NULL;

        if (start == NULL)
            start = tmp;
        else
        {
            ptr = start;
            while (ptr->link != NULL)
                ptr = ptr->link;

            ptr->link = tmp;
        }
    }

    ptr = start;
    printf("The Elements Are: ");
    while (ptr != NULL)
    {
        printf("%d->", ptr->info);
        ptr = ptr->link;
    }

    printf("NULL");
}

int main()
{
    createList();
    return 0;
}
