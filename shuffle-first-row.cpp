#include <algorithm>
#include <iostream>

int main()
{
    // piece abbreviations come from http://en.wikipedia.org/wiki/Shogi
    std::string first_row("LNSGKGSNL");
    std::sort(first_row.begin(), first_row.end());
    do {
        std::cout << first_row << '\n';
    } while (std::next_permutation(first_row.begin(), first_row.end()));
 
    return 0;
}
