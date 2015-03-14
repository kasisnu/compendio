#include <iostream>
#include <string>

int main(int argc, char** argv)
{
    std::string str = argv[1];
    std::cout << str.append(" edited.");
    return 0;
}