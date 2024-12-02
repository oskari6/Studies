#include <iostream>
#include <vector>

print_array(const int data[], int size) //const makes function work: array not change data, row 8
{
    for(int i = 0; i < size; i++)
    {
        //data[i]++; //when yo upass an array to a function it decays to a pointer, const helps
        std::cout << data[i] << "\t";
    }
    std::cout<<"\n";
}

int main()
{
    int data[] = {1, 2, 3};
    print_array(data, 3);
    std::cout << data[0] << std::endl;

    return 0;
}