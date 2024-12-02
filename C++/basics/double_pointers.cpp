#include <iostream>
void printData(int size, const char** data) {
    for(int i = 0;i < size; i++) {
        std::cout << data[i] << std::endl;
    }
}

void modifyData(int** data){
    int* temp = new int (10);
    delete *data;
    *data = temp;
    std::cout << **data << std::endl;
}

int main(int argx, char** argv) {
    // for (int i = 1; i < argv[i]; i++) {
    //     std::cout << argv[i] << std::endl;
    // }

    const char* data[] = {"test test test", "test test test"};

    printData(2, data);

    //example 2
    int* data = new int(5);
    modifyData(&data);
    std::cout << *data << std::endl;
    return 0;
}