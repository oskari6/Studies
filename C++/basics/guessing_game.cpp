#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <array>
#include <fstream>

void save_score(int count)
{
    //file rewriting and comparing
    std::ifstream input ("best_score.txt");
    if(!input.is_open()) //if error
    {
        std::cout << "unable to read file\n";
        return;
    }
    int best_score;
    input >> best_score;

    std::ofstream output("best_score.txt");//can also use just fstream
    if(!output.is_open()) //if error
    {
        std::cout << "unable to read file\n";
        return;
    }

    if(count < best_score)
    {
        output << count;
    }
    else
    {
        output << best_score;
    }
    //the best amount of tries is documented to best_score.txt
}

/*program is going to compare the best results of each 
round and rewrite in file the best score*/

/*void print_array(int array[], int count)
{
    for(int i = 0; i < count; i++)
    {
        std::cout << array[i] << "\t";
    }
    std::cout << "\n";
}*/

void print_vector(std::vector<int> vector) //refactoring a vector
{
    for(int i = 0; i < vector.size(); i++)
    {
        std::cout << vector[i] << "\t";
    }
    std::cout << "\n";
}
//stl array refactor
/*void print_array(std::array<int, 251>, array, int size) //refactoring a vector
{
    for(int i = 0; i < size; i++)
    {
        std::cout << array[i] << "\t";
    }
    std::cout << "\n";
}*/

void play_game()
{
    //std::array <int, 251> guesses; //stl array
    int count = 0;
    std::vector<int> guesses; //vector
    //int guesses[251]; //stl array
    //int guess_count = 0; //c array

    int random = rand() % 251; //there wont be 251 now. 1-250
    std::cout << random << std::endl;
    std::cout << "Guess a number: ";
    while(true)
    {
        int guess;
        std::cin >> guess;
        count++; //or guesses.size(), keeps track of best score this round

        //guesses[count++] = guess //stl array
        //guesses[guess_count++] = guess; //c array
        guesses.push_back(guess); //vector

        if(guess == random)
        {
            std::cout << "You win!\n";
            break;
        }else if (guess < random)
        {
            std::cout << "Too low\n";
        }else
        {
            std::cout << "Too high\n";
        }
    }
    save_score(count);

    //print_array(guesses, guess_count); //c array
    print_vector(guesses); //vector
    //print_array(guesses, count) //stl array
}
int main()
{
    srand(time(NULL)); //NULL = seed, this is seeding
    //if you dont do this give the same sequence of numbers always
    int choice;

    do
    {
        std::cout << "0. Quit" << std::endl <<"1. Play Game\n";
        std::cin >> choice;

        switch(choice)
        {
            case 0:
                std::cout << "Thanks for nothing\n";
                return 0;
            case 1:
            play_game();
                std::cout << "yo let's play\n";
                break;
        }
    }
    while(choice != 0);
}