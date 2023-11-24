#include<stdio.h>
#include<stdlib.h> // for exit() function

#define MAX 10 // Maximum size of the stack

int stack[MAX]; // Array to store the stack elements
int top = -1;   // Initialize top of the stack to -1

// Function prototypes
void push();
void pop();
void traverse();

int main() {
    int ch;
    // Menu-driven interface
    while (1) {
        // Displaying menu options
        printf("\n1. Push");
        printf("\n2. Pop");
        printf("\n3. Traverse");
        printf("\n4. Exit");
        printf("\nEnter Your Choice: ");
        scanf("%d", &ch);

        // Switch statement to perform the chosen operation
        switch (ch) {
            case 1:
                push(); // Call push function
                break;
            case 2:
                pop(); // Call pop function
                break;
            case 3:
                traverse(); // Call traverse function
                break;
            case 4:
                exit(0); // Exit the program
                break;
            default:
                printf("\nInvalid Choice"); // Display for invalid choices
        }
    }
    return 0;
}

// Function to push an element onto the stack
void push() {
    int item;
    // Check for stack overflow
    if (top == MAX - 1) {
        printf("\nOverflow");
        return;
    }
    printf("\nEnter Item: ");
    scanf("%d", &item);
    top = top + 1;
    stack[top] = item;
    printf("\nItem Inserted");
}

// Function to pop an element from the stack
void pop() {
    // Check for stack underflow
    if (top == -1) {
        printf("\nUnderflow");
        return;
    }
    top = top - 1;
    printf("\nItem Deleted");
}

// Function to traverse and display stack elements
void traverse() {
    int i;
    // Check if the stack is empty
    if (top == -1) {
        printf("\nEmpty");
        return;
    }
    // Display stack elements
    printf("\nStack elements: ");
    for (i = top; i >= 0; i--) {
        printf("%d ", stack[i]);
    }
}
