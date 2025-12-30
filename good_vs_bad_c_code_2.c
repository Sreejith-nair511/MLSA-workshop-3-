/*
========================================
 BAD CODE: No validation, poor structure
========================================
*/

#include <stdio.h>

int main(){
int x;
scanf("%d",&x);
if(x>0)printf("Positive");
else printf("Negative");
}

/*
Problems:
- No input prompt
- No validation
- Poor formatting
- No return statement clarity
*/


/*
========================================
 GOOD CODE: Clear logic & validation
========================================
*/

#include <stdio.h>

int get_number(void) {
    int value;
    printf("Enter a number: ");
    if (scanf("%d", &value) != 1) {
        printf("Invalid input\n");
        return 0;
    }
    return value;
}

int main(void) {
    int number = get_number();

    if (number > 0) {
        printf("Number is Positive\n");
    } else if (number < 0) {
        printf("Number is Negative\n");
    } else {
        printf("Number is Zero\n");
    }

    return 0;
}

/*
Why this is good:
- Input validation
- Clear branching
- Modular design
- Readable output
*/
