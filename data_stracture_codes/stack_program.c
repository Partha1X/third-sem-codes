#include <stdio.h>

#define N 5

int stack[N];
int top = -1;

// Function prototypes
void push();
void pop();
void display();

int main() {
    int ch;

    do {
        printf("Enter 1: Push, 2: Pop, 3: Display, 0: Quit: ");
        scanf("%d", &ch);

        switch (ch) {
            case 1:
                push();
                break;
            case 2:
                pop(); // Added missing semicolon here
                break;
            case 3:
                display();
                break;
            case 0:
                break; // Added a case to exit the loop when 0 is entered
            default:
                printf("Invalid choice\n");
        }
    } while (ch != 0); // Moved the loop condition here

    return 0;
}

void push() {
    if (top == (N - 1)) {
        printf("Overflow\n");
    } else {
        int i;
        printf("Enter a number: ");
        scanf("%d", &i);
        top = top + 1;
        stack[top] = i; // Changed "a" to "stack"
        printf("Item inserted\n");
    }
}

void pop() {
    if (top == -1) {
        printf("Underflow\n");
    } else {
        top = top - 1;
        printf("Item deleted\n");
    }
}

void display() {
    if (top == -1) {
        printf("Stack is empty\n");
    } else {
        printf("Items are: ");
        for (int j = top; j >= 0; j--) {
            printf("%d ", stack[j]); // Changed "system.out.printf" to "printf" and added a format specifier
        }
        printf("\n"); // Added a newline to separate items
    }
}
