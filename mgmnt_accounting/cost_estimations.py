class CostEstimations:
    def __init__(self):
        pass
    @staticmethod
    def high_and_low(cost_high_act,cost_low_act,high_act,low_act):
        unit_vc = (cost_high_act - cost_low_act ) / (high_act - low_act)
        fixed_cost = cost_low_act - (unit_vc * low_act)
        formula = f"y = {fixed_cost} + {unit_vc}x"
        return fixed_cost,unit_vc,formula
    @staticmethod
    def regression_analysis(x_values,y_values):
        x_sum = 0
        x_sum_squared = 0
        y_sum = 0 
        n = 0
        xy_sum = sum(x*y for x,y in zip(x_values,y_values))
        for x in x_values:
            x_sum += x
            x_sum_squared += x*x
            n += 1
        for y in y_values:
            y_sum += y
        b = ((xy_sum - (x_sum*y_sum)) / n ) / ((x_sum_squared - (x_sum**2)) / n )
        a = (y_sum / n) - (b*(x_sum / n))
        formula = f"y = {a} + {b}x"
        return a,b,formula 

