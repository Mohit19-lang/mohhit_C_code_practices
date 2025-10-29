 import os

codes = {
    1: '''// Code 1: Array Sum
#include <stdio.h>
int main() {
    int n, sum = 0;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter %d numbers: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    printf("Sum of array: %d\\n", sum);
    return 0;
}''',

    2: '''// Code 2: Maximum in Array
#include <stdio.h>
int main() {
    int n, max;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter %d numbers: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) max = arr[i];
    }
    printf("Maximum value: %d\\n", max);
    return 0;
}''',
    # Yahi pattern follow karo: 3, 4, ... 170 sab yahan code paste karo
}

os.makedirs("c_codes", exist_ok=True)

for num, code in codes.items():
    filename = f"c_codes/code_{num}.c"
    with open(filename, 'w') as f:
        f.write(code)
    print(f"File Ban Gayi: {filename}")

print("SAB FILE BAN GAYI - c_codes folder check karo!")
