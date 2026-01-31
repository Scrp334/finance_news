import math
import numpy

from returns import Returns

class Risk:
    def __init__(self,probabilities,returns):
        self.probabilities = probabilities
        self.returns = returns
        self.expected_return , self.format_ans = Returns.expected_return(probabilities, returns)
        self.variance = sum(((r - expected_return)**2)*p for p,r in zip(probabilities,return))
        self.std_dev = math.sqrt(self.variance)
        self.coeff_of_variation = (self.std_dev / self.expected_return) 
        self.inverse_volatility = 1 / self.std_dev

    def variance_measure(self):
        format_ans = f"The risk with variance measure is {self.variance:.2f}"
        return self.variance,format_ans
    
    def standard_deviation(self):
        format_ans = f"The risk with standard deviation measure is {self.std_dev:.2f}"
        return self.std_dev, format_ans
    
    def coefficient_of_variation(self):
        format_ans = f"The Coefficient of Variation is {self.coeff_of_variation:.2f}"
        return self.coeff_of_variation, format_ans

    def inverse_volatility_weigh(self):
        format_ans = f"Inverse volatility weight is {self.inverse_volatility:.2f}"
        return self.inverse_volatility,format_ans

    @staticmethod
    def covariance(returns_a,expected_return_a,returns_b,expected_return_b):
        sum_of_assets = sum((ret_a - expected_return_a)*(ret_b - expected_return_b) for ret_a,ret_b in zip(returns_a,returns_b)) 
        covariance = sum_of_assets / (len(returns_a) - 1) 
        format_ans = f"The Covariance of the 2 assets is {covariance:.2f}"
        return covariance,format_ans
    @staticmethod
    def correlation(covariance_ab,std_dev_a, std_dev_b):
        correlation = covariance_ab / (std_dev_a * std_dev_b)
        format_ans = f"The Correlation of the two assets is {correlation:.2f}"
        return correlation,format_ans
    @staticmethod
    def portfolio_risk_var_covar(weights,variance,covar_matrix):
       weights_np = np.array(weights)
       portfolio_variance = np.dot(weights_np.T, np.dot(covar_matrix,weights_np))  
       portfolio_std_dev = np.sqrt(portfolio_variance)
       individual_var = np.sum(weights_np**2) * np.diag(covar_matrix)
       interactive_risk = portfolio_variance - individual_variances
       format_ans = f"The Portfolio risk using Portfolio-Variance-Covariance(standard deviation) is {portfolio_std_dev:.2f}"
       return portfolio_std_dev,format_ans
    








        

