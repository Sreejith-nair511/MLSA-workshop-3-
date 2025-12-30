/*
========================================
 BAD CODE: Confusing loop and names
========================================
*/

#include <stdio.h>

int main(){
int i,n,s=0;
scanf("%d",&n);
for(i=0;i<n;i++)s+=i;
printf("%d",s);
}

/*
Problems:
- No explanation of purpose
- Poor variable names
- No prompt or clarity
*/


/*
========================================
 GOOD CODE: Self-explanatory logic
========================================
*/

#include <stdio.h>

int calculate_sum(int limit) {
    int sum = 0;
    for (int i = 1; i <= limit; i++) {
        sum += i;
    }
    return sum;
}

int main(void) {
    int number;

    printf("Enter a positive number: ");
    scanf("%d", &number);

    printf("Sum of first %d numbers is %d\n",
           number, calculate_sum(number));

    return 0;
}

/*
Why this is good:
- Descriptive function and variables
- Clear loop bounds
- Easy to modify
*/
