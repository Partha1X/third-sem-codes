//WAP to implement insertation short algorithm 
#include<stdio.h>
#include<conio.h>

void main()
{
    int arr[30], i, j, n, tmp;
    //clrscr(); // Corrected function name

    printf("\nEnter no of Element: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++)
    {
        printf("\nEnter value for arr[%d]: ", i);
        scanf("%d", &arr[i]); // Corrected syntax
    }

    printf("\nBefore Sorting: ");
    for(i = 0; i < n; i++)
        printf("%d ", arr[i]); // Added space for better formatting

    for(i = 1; i < n; i++)
    {
        tmp = arr[i];
        j = i - 1; // Corrected initialization

        while(tmp < arr[j] && j >= 0)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = tmp;
    }

    printf("\nAfter Sorting: ");
    for(i = 0; i < n; i++)
    {
        printf("%d ", arr[i]); // Added space for better formatting
    }

    getch();
}
