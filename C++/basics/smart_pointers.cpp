#include <iostream>
#include <memory> //for smart pointers

//dont use stack, use heap

int* getData(){//new
    int* a = new int(5);
    return a;
}

std::shared_ptr<int> getData2(){ //shared
    std::shared_ptr<int> a = std::make_shared<int>(5);
    return a;
}

std::unique_ptr<int> getData3(){ //unique
    auto a = std::make_unique<int>(5);
    return a;
}

int main() {
    //new
    int* b = getData();
    std::cout << *b << std::endl;
    delete b; //good practice with new keyword

    //smart pointer
    std::shared_ptr<int> b2 = getData2();
    std::cout << *b2 << std::endl;
    auto c = b2; //automation for pointers
    std::cout << *c << std::endl;
    //b.use_count()

    //moving owners
    //auto c = std::move(b);
    //if(b) {
        //do something
    //}

    //weak pointer
    auto d = getData2();
    std::weak_ptr<int> weak = d;
    //try to acces it --> create a shared pointer from it
    auto shared = weak.lock();
    if(shared){
        std::cout << *shared << std::endl;
    }
    return 0;
}