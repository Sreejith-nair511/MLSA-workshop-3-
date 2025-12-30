#include <stdio.h>

int add(int x, int y) {
    return x + y;
}

int main(void) {
    int num1, num2;

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    printf("Sum = %d\n", add(num1, num2));
    return 0;
}
// Improvements made:
// 1. Added a prompt for user input
// 2. Clear and descriptive output
// 3. Improved readability with proper indentation and spacing
// 4. Modular code with a separate function for addition
