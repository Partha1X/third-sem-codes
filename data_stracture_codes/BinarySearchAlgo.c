//WAP to implement Binary Search Algorithm 
#include<stdio.h>

int main() {
    int arr[10], lb, ub, mid, i, item, n;

    printf("Enter no of Elements: ");
    scanf("%d", &n);

    printf("Enter elements for the array:\n");
    for(i = 0; i < n; i++) {
        printf("Enter Item for arr[%d]: ", i);
        scanf("%d", &arr[i]);
    }

    printf("Enter Item to be Searched: ");
    scanf("%d", &item);

    lb = 0;
    ub = n - 1;
    mid = (lb + ub) / 2;

    while (item != arr[mid] && lb <= ub) {
        if (item < arr[mid])
            ub = mid - 1;
        else
            lb = mid + 1;

        mid = (lb + ub) / 2;
    }

    if (item == arr[mid])
        printf("Item found at Location %d\n", mid);
    else
        printf("Item not Found\n");

    return 0;
}
