#include <iostream>
#include <string>

template <typename T>

void swap(T &a, T &b) //this is fine too: int& a, int & a
{
    int temp = a;
    a = b;
    b = temp;
}

template <typename T>
void swap( T a[], T b[], int size)
{
    for(int i = 0; i < size; i++)
    {
        T temp = a[i];
        a[i] = b[i];
        b[i] = temp;
    }
}
/*
void swap(std::string &a, std::string &b) //method overloading
{
    std::string temp = a;
    a = b;
    b = temp;
}
*/
int main()
{
    int a = 10;
    int b = 20;
    swap(a, b);
    std::cout << "a: " << a << "\tb: " << b << "\n";

    std::string first_name = "Oskari";
    std::string last_name = "Sulkakoski";
    swap(first_name, last_name);
    std::cout << first_name << " " << last_name << std::endl;

    int nines[] = {9, 9, 9, 9, 9, 9};
    int ones[] = {1, 1, 1, 1, 1, 1};

    for(int i = 0; i < 6; i++)
    {
        std::cout << nines[i] << " " << ones[i] << "\t";
    }
    std::cout << "\n\n";

    swap(nines, ones, 6);

    for(int i = 0; i < 6; i++)
    {
        std::cout << nines[i] << " " << ones[i] << "\t";
    }
    std::cout << "\n\n";

    swap(nines, ones, 6);
    return 0;
}

