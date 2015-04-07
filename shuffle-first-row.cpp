#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#include <boost/program_options.hpp>
namespace po = boost::program_options;

bool second_row_protected(const std::string& first_row,
                          bool protect_without_king)
{
    const int size = first_row.size();

    std::vector<bool> second_row(size);

    for (auto i = 0; i < size; i++) {
        if (protect_without_king && first_row[i] == 'K')
            continue;

        switch (first_row[i]) {  // no break statements indeed
        case 'S':
        case 'G':
        case 'K':
            if (i-1 >= 0)
                second_row[i-1] = true;
            if (i+1 < size)
                second_row[i+1] = true;
        case 'L':
            second_row[i] = true;
        }
    }

    return std::all_of(second_row.begin(), second_row.end(),
                       [](bool i) { return i; });
}

int main(int argc, char **argv)
{
    po::options_description desc("Allowed options");
    desc.add_options()
        ("help", "produce help message")
        ("protect", "protect all squares on second row")
        ("protect-more",
         "protect all squares on second row without the help of the king")
    ;

    po::variables_map vm;
    try {
        po::store(po::parse_command_line(argc, argv, desc), vm);
        po::notify(vm);
    } catch (po::unknown_option& e) {
        std::cerr << desc;
        return 1;
    }

    if (vm.count("help")) {
        std::cerr << desc;
        return 1;
    } else if (vm.count("protect") && vm.count("protect-more")) {
        std::cerr << "Options --protect and --protect-more cannot be used "
                     "together\n";
        return 1;
    }

    // piece abbreviations come from http://en.wikipedia.org/wiki/Shogi
    std::string first_row("LNSGKGSNL");
    std::sort(first_row.begin(), first_row.end());

    const bool protect = vm.count("protect") || vm.count("protect-more");
    const bool protect_without_king = vm.count("protect-more");
    do {
        if (!protect || second_row_protected(first_row, protect_without_king))
            std::cout << first_row << '\n';
    } while (std::next_permutation(first_row.begin(), first_row.end()));
 
    return 0;
}
