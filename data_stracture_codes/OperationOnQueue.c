//WAP to Implement the operation of a Queue
#include<stdio.h>
#include<stdlib.h>

#define MAX 5

int queue[MAX];
int front = -1, rear = -1;

void insert();
void delete();
void display();

int main(void) {
    int ch;
    while(1) {
        printf("\n1.Insert");
        printf("\n2.Delete");
        printf("\n3.Traverse");
        printf("\n4.Exit");
        printf("\nEnter Your Choice: ");
        scanf("%d", &ch);

        switch(ch) {
            case 1:
                insert();
                break;
            case 2:
                delete();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
                break;
            default:
                printf("\nInvalid Choice");
        }
    }
    return 0;
}

void insert() {
    int item;
    if (rear == MAX - 1) {
        printf("\nOverflow");
        return;
    }
    if (front == -1 || rear == -1) {
        front = 0;
        rear = 0;
    } else {
        rear = rear + 1;
    }
    printf("\nEnter Item: ");
    scanf("%d", &item);
    queue[rear] = item;
    printf("\nItem Inserted");
}

void delete() {
    if (front == -1 || front > rear) {
        printf("\nUnderflow");
        return;
    } else {
        front = front + 1;
        printf("\nItem Deleted");
    }
}

void display() {
    int i;
    if (front == -1 || front > rear) {
        printf("\nQueue Empty");
    } else {
        for (i = front; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
    }
    printf("\nItems Displayed");
}
