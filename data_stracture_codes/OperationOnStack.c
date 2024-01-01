/*(2) WAP  to implement stack operations using an array with a menu-driven approach
Stack Operations Menu:
(1) Push
(2) PoP
(3) Traverse
(4) Exit
*/
#include<stdio.h>
#include<stdlib.h>

#define MAX 10
int stack[MAX];
int top = -1;

void push();
void pop();
void traverse();

int main()
{
    int ch;
    while (1)
    {
        printf("\n1.Push \n2.Pop \n3.Traverse \n4.Exit \nEnter your choice:");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            push();
            break;
        case 2:
            pop();
            break;
        case 3:
            traverse();
            break;
        case 4:
            exit(0);
            break;
        default:
            printf("\nInvalid choice");
        }
    }
}

void push()
{
    int item;
    if (top == MAX - 1)
    {
        printf("Stack overflow");
        return;
    }
    printf("\nEnter item:");
    scanf("%d", &item);
    top = top + 1;
    stack[top] = item;
    printf("\nItem inserted");
}

void pop()
{
    if (top == -1)
    {
        printf("Stack underflow");
        return;
    }
    top = top - 1;
    printf("\nItem deleted");
}

void traverse()
{
    int i;
    printf("The items are:");
    if (top == -1)
    {
        printf("Empty");
        return;
    }
    for (i = top; i >= 0; i--)
    {
        printf("%d ", stack[i]);
    }
}
