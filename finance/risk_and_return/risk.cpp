#include "utils.hpp"

#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <utility>
#include <vector>
#include <cstdint>
#include <numeric>


class Risk{
private:
    std::vector<std::int64_t> probabilities;
    std::vector<std::int64_t> returns;
    std::int64_t expected_return;
public:
    Risk(std::vector<std::int64_t>& probabilities,std::vector<std::int64_t>& returns) {

    } 

};