#include <iostream>

class Position
{
    public:
        int x = 10;
        int y = 20;
        Position operator + (Position pos) //operator overload
        {
            Position new_pos;
            new_pos.x = x + pos.x; //middle x in pos1, last x parameter, first pos3
            new_pos.y = y + pos.y;
            return new_pos;
        }
        bool operator == (Position pos)
        {
            if(x == pos.x && y == pos.y)
            {
                return true;
            }
            return false;
        }
};

std::ostream

int main()
{
    /*Position pos1, pos2;
    Position pos3 = pos1 + pos2;
    std::cout << pos3.x << " " << pos3.y << std::endl;

    pos2.x = 30;

    if(pos1 == pos2)
    {
        std::cout << "They are the same";
    }*/

    User user;
    std::cout << user << std::endl;

    return 0;
}