#include <stdio.h>

/*
  Display larggest element of an array
  Jane in accounting needed a quick routine
  TODO - put this into the utilities library - KB
*/
int main(){
    int i, n;
    float arr[100];

    
    printf("Enter total number of elements(1 to 100): ");
    scanf("%d", &n);
    
    printf("\n");
    // Stores number entered by the user
    for(i = 0; i < n; ++i ) 
    {
       printf("Enter Number %d: ", i+1);
            scanf("%f", &arr[i]);}
    for(i = 1; i < n; ++i){
       // Loop to store largest number to arr[0]
      // Change < to > if you want to find the smallest element
      if(arr[0] < arr[i])
	  arr[0] = arr[i];
    }
printf("Largest element = %.2f", arr[0]);

    return 0;
}



