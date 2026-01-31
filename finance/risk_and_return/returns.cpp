#include "utils.hpp"
#include "returns.hpp"

#include <iostream>
#include <string>
#include <cmath>
#include <sstream>
#include <utility>
#include <cstdint> 

std::pair<std::int64_t,std::string> Returns::dividend_yield(const std::string& dvdnd_per_share,const std::string& price_per_share) {
    std::int64_t dvdnd_yield_pcnt = (utils::turn_to_ll(dvdnd_per_share) / utils::turn_to_ll(price_per_share) ) * 100;
    std::ostringstream format_ans;
    format_ans << "Dividend yield is " << dvdnd_yield_pcnt <<  " at " << dvdnd_per_share
        <<" dividend per share with " << price_per_share << " price per share";
    return {(dvdnd_yield_pcnt / 100),format_ans.str()};
}

std::pair<std::int64_t,std::string> Returns::capital_gain(const std::string& new_price,const std::string& old_price) {
    std::int64_t gain = ((utils::turn_to_ll(new_price) / utils::turn_to_ll(old_price)) - 1 ) * 100;
    std::ostringstream format_ans;
    format_ans << "The Capital gain is " << gain << "% at new price " << new_price <<  " from old price " << old_price;
    return {(gain / 100),format_ans.str()};
}
    
std::pair<std::int64_t,std::string> Retruns::holding_period_return(const std::string& dividend,const std::string& new_price, const std::string& old_price) {
    std::int64_t price_difference = (utils::turn_to_ll(new_price) - utils::turn_to_ll(old_price));
    std::int64_t h_p_r = ( (utils::turn_to_ll(dividend) + price_difference) / utils::turn_to_ll(old_price) ) * 100;
    std::ostringstream format_ans;
    format_ans << "The Holding period return is " << h_p_r << "% with " << dividend << " dividend with new price " << new_price << " and old price " << old_price;
    return {(h_p_r / 100),format_ans.str()};
}

    //static std::pair<std::int64_t,std::string> int_rate_of_return(): 
    

