/*
========================================
 BAD CODE EXAMPLE (BEGINNER STYLE)
========================================
*/

#include <stdio.h>

int main(){
int a,b,c;
printf("Enter two numbers:");
scanf("%d%d",&a,&b);
c=a+b;
printf("%d",c);
}

/*
Problems:
- Poor formatting
- No function separation
- Non-descriptive variable names
- Hard to extend or debug
*/


/*
========================================
 GOOD CODE EXAMPLE (PROFESSIONAL STYLE)
========================================
*/

#include <stdio.h>

int add_numbers(int first, int second) {
    return first + second;
}

int main(void) {
    int number1, number2, sum;

    printf("\nEnter two numbers: ");
    scanf("%d %d", &number1, &number2);

    sum = add_numbers(number1, number2);

    printf("Sum: %d\n", sum);
    return 0;
}

/*
Why this is good:
- Clean formatting
- Meaningful variable names
- Modular function design
- Easy to test and extend
*/
