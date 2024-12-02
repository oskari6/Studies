#include <stdio.h>
#include <stdlib.h>

int* generateArray(int size){
    int* array = malloc(sizeof(int) * size);
    for(int i = 0; i < size; i++){
        array[i] = 1;
    }
    return array;
}

int main(){
    //allocating memory
    //void pointer not optimal

    int size = 20;
    int count = 0;

    int* array = generateArray(size);

    //if system is memory constraint
    if(array == NULL){
        printf("Memory allocation failed");
        return 1;
    }

    size * 2;
    //create new memory or expand the current memory
    int* array2 = realloc(array, sizeof(int) * size);

    if(array2 == NULL){
        printf("New memory allocation failed..\n");
        return 1; //still possible to continue, not necessary to return 1
    } else {
        array = array2;
    }
    
    for(int i = 0; i < size / 2; i++){
        array[i] = i;
        count++;
    }

    for(int i = 0; i < count; i++){
        printf("%i ", array[i]);
    }

    printf("\n");

    printf("size: %i, count %i\n", size, count);

    free(array); //good practice
    return 0;
}