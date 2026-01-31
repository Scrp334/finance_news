class Returns:
    def __init__(self):
        pass 
    @staticmethod
    def dividend_yield(dvdnd_per_share,price_per_share):
        dvdnd_yield_pcnt = (dvdnd_per_share / price_per_share ) * 100  
        format_ans = f"Dividend yield is {dvdnd_yield_pcnt:.2f}% at {dvdnd_per_share} dividend per share with {price_per_share} price per share"
        return (dvdnd_yield_pcnt / 100),format_ans
    @staticmethod
    def capital_gain(new_price,old_price):
        gain = ((new_price / old_price) - 1 ) * 100
        format_ans = f"The Capital gain is {gain:.2f}% at new price {new_price} from old price {old_price}"
        return (gain / 100), format_ans 
    @staticmethod
    def holding_period_return(dividend, new_price, old_price):
        h_p_r = ((dividend + (new_price - old_price)) / old_price ) * 100
        format_ans = f"The Holding period return is {h_p_r:.2f}% with {dividend} dividend with new price {new_price} and old price {old_price}"
        return (h_p_t / 100),format_ans 
    @staticmethod
    def int_rate_of_return(interest_paid,loan_amount):
        int_rate_of_return = (interest_paid / loan_amount) * 100
        format_ans = f"The Interest ratte of return is {int_rate_of_return:.2f}% for {loan_amount} loan amount on {interest_paid} interest paid"
        return (int_rate_of_return / 100), format_ans
    @staticmethod
    def required_rate(risk_free_rate,risk_premium):
        required_return = risk_free_rate + risk_premium
        format_ans = f"Th Required return/Huddle rate is {required_rate} with {risk_free_rate} as risk free investment rate and {risk_premium} as rsik premium"
        return required_rate,format_ans
    @staticmethod
    def expected_return(probabilities, returns):
        expected_return = sum(p*r for p,r in zip(probabilities, returns))
        format_ans = f"The Expected return from data is {expected_return:.2f}"
        return expected_return,format_ans
    @staticmethod
    def portfolio_return(weights,expected_return):
        portfolio_return = sum(weight*exp_return for weight,exp_return in zip(weights,expected_returns))  
        format_ans = f"The Portfolio return is {portfolio_return:.2f}%"
        portfolio_return_pcnt = portfolio_return * 100
        return (portfolio_return_pcnt / 100), format_ans 