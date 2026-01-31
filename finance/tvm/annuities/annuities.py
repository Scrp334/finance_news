class Annuity:
    def init(self):
        pass
class OrdAnnuity(Annuity):
    @staticmethod
    def pV(pmt,rate,time):
        pv = pmt * ( (1 - ( (1 + rate)**(-time) )) / rate )
        format_ans = f"The Present value of {pmt} is {pv} when discounted at rate {rate} for {time} time in Ordinary Annuity"
        return pv,format_ans
    @staticmethod
    def fV(pmt,rate,time):
        fv = pmt * (( ((1 + r)**t) - 1 ) / 1 ) 
        format_ans = f"The Future value of {pmt} is {fv} at {rate} rate in {time} time in Ordinary Annuity"
        return fv,format_ans
class DueAnnuity(OrdAnnuity):
    @staticmethod
    def pV(pmt,rate,time):
        ord_ann, _ = OrdAnnuity.pV(pmt,rate,time)
        pv = ord_ann * (1 + rate)
        format_ans =  format_ans = f"The Present value of {pmt} is {pv} when discounted at rate {rate} for {time} time in Annuity Due"
        return pv,format_ans
    @staticmethod
    def fV(pmt,rate,time):
        ord_ann, _ = OrdAnnuity.fV(pmt,rate,time)
        pv = ord_ann * (1 + rate) 
        ormat_ans = f"The Future value of {pmt} is {fv} at {rate} rate in {time} time in Annuity Due"
        return fv, format_ans
        
pv_ord,ff = OrdAnnuity.pV(1000,0.05,10)
print(f"{pv_ord} & {ff}")