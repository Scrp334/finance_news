#ifndef RETURNS_HPP
#define RETURNS_HPP

#include <iostream>
#include <string>
#include <cmath>
#include <sstream>
#include <utility>
#include <cstdint>

class Returns {
public:
    virtual ~Returns() = default;
    static std::pair<std::int64_t,std::string> dividend_yield(const std::string& dvdnd_per_share,const std::string& price_per_share);
    static std::pair<std::int64_t,std::string> capital_gain(const std::string& new_price,const std::string& old_price);
    static std::pair<std::int64_t,std::string> holding_period_return(const std::string& dividend,const std::string& new_price, const std::string& old_price);

};

#endif 