#include "utils.hpp"

#include <iostream>
#include <string>
#include <cmath>
#include <utility>
#include <cstdint>
#include <sstream>

class Annuity{
public:
    virtual ~Annuity() = default;
};

class OrdAnnuity : public Annuity {
public:
    static std::pair<std::int64_t,std::string> pV(std::string pmt,std::string rate,std::string time) {
        std::int64_t pv = utils::turn_to_ll(pmt) * (1 - ( std::pow((1 + utils::turn_to_ll(rate) ), utils::turn_to_ll(time)) ) / utils::turn_to_ll(rate));
        std::ostringstream format_ans; 
        format_ans << "The present value of " << pmt << " is " << pv << " when discounted at rate "
            << rate << " for time " << time << " on Ordinary Annuity";
        return {pv,format_ans.str()};
    }
    static std::pair<std::int64_t, std::string> fV(std::string pmt,std::string rate,std::string time) {
        std::int64_t fv = utils::turn_to_ll(pmt) * ( (std::pow((1 + utils::turn_to_ll(rate)), utils::turn_to_ll(time))) / utils::turn_to_ll(rate) );
        std::ostringstream format_ans;
        format_ans << "The future value of " << pmt << " is " << fv << " when compounded at rate "
            << rate << " for time " << time << " on Ordinary Annuity";
        return {fv,format_ans.str()};
    }
};

class DueAnnuity : public Annuity{
public:
    static std::pair<std::int64_t, std::string> pV(std::string pmt,std::string rate,std::string time) {
        auto [ord_pv, _ ] = OrdAnnuity::pV(pmt,rate,time); 
        std::int64_t pv = ord_pv * (1 + utils::turn_to_ll(rate));
        std::ostringstream format_ans;
        format_ans << "The present value of " << pmt << " is " << pv << " when discounted at rate "
            << rate << " for time " << time << " on Annuity Due";
        return {pv,format_ans.str()};
    }
    static std::pair<std::int64_t,std::string> fV(std::string pmt,std::string rate,std::string time) {
        auto [ord_fv, _ ] = OrdAnnuity::fV(pmt,rate,time);
        std::int64_t fv = ord_fv * (1 + utils::turn_to_ll(rate));
         std::ostringstream format_ans;
        format_ans << "The future value of " << pmt << " is " << fv << " when componuded at rate "
            << rate << " for time " << time << " on Annuity Due";
        return {fv,format_ans.str()};     
    }
};   
