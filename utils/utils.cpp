#include "utils.hpp"

#include <string>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <chrono>
#include <optional>
#include <iostream>
#include <cctype>
#include <format>
#include <locale>


namespace utils { // NOTE: THIS NEEDS FURTHER FIX AND IMPLEMENTATION.
	// helper function for integer formatting i.e 12345 to 1234500 for easier calc (12345.00 later when formatted)
    std::int64_t turn_to_ll(const std::string str_amount) {
        std::string amount = str_amount;
        std::int64_t whole_val = 0;
        std::int64_t frac_val = 0;
        bool seen_dot = false;
        int decimal_count = 0;
        std::string frac_digits = "";

        for (char c : amount) {
            if (std::isdigit(c)) {
                if (!seen_dot) {
                    // Build the whole number
                    whole_val = (whole_val * 10) + (c - '0');
                }
                else {
                    // Collect fractional digits as a string to handle rounding/padding later
                    frac_digits += c;
                }
            }
            else if (c == ',') {
                continue; // Ignore commas silently
            }
            else if (c == '.') {
                if (seen_dot) return -1; // ERROR: Second dot found! (e.g., .996.45)
                seen_dot = true;
            }
            else {
                return -1; // ERROR: Junk found! (e.g., 'k' or 'f')
            }
        }

        // Now handle the fractional string (the cents)
        if (frac_digits.length() >= 3) {
            int first_two = std::stoi(frac_digits.substr(0, 2));
            int third_digit = frac_digits[2] - '0';
            if (third_digit >= 5) first_two++;
            frac_val = first_two;
        }
        else {
            // Pad with zeros (e.g., ".5" -> "50")
            while (frac_digits.length() < 2) frac_digits += '0';
            frac_val = (frac_digits.empty()) ? 0 : std::stoll(frac_digits);
        }

        // Handle rounding overflow (.996 -> 1.00)
        if (frac_val >= 100) {
            whole_val += 1;
            frac_val = 0;
        }

        return (whole_val * 100) + frac_val;
    }

    // format currency i.e 123500 to 1235.00
    std::string format_currency(const std::int64_t amount) {
        std::int64_t ll_num = amount;
#ifdef _WIN32
        std::string ll_num_str = std::format(std::locale("en-US"), "{:L}", (double)ll_num / 100.0); 
#else
        std::string ll_num_str = std::format(std::locale("en_US.UTF-8"), "{:L}", (double)ll_num / 100.0);
#endif 
        return ll_num_str;


    }
} //namespace utils