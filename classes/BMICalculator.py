#make a interface with .calcuate
#make 2 concrete classes
# format text input --> private method
import classes.Formatter as fm

class BMICalculatorInterface:
    def __init__(self, weight_lb =  None, height_in =  None, weight_kg =  None, height_m =  None):
        self.weight_lb = weight_lb
        self.height_in = height_in
        self.weight_kg = weight_kg
        self.height_m = height_m
    
    def calculate(self):
        pass

class ImperialBMICalculator(BMICalculatorInterface):
    def __init__(self, weight_lb, height_in) -> None:
        super().__init__(weight_lb, height_in)

    def calculate(self):
        """ 
        Calculate BMI using standard measurments.
        Inputs:
            height_in = int() or float()
            weight_lb = int() or float()
        
        Output:
            float(BMI)
        """
        if type(self.height_in) == str:
            self.height_in = fm.Text2FloatFormatter(self.height_in).format()
        
        if type(self.weight_lb) == str:
            self.weight_lb = fm.Text2FloatFormatter(self.weight_lb).format()
        
        height =  self.height_in
        bmi = (float(self.weight_lb) / (height **2)) * 703

        return bmi
    
   
class MetricBMICalculator(BMICalculatorInterface):
    def __init__(self, weight_kg, height_m) -> None:
        super().__init__(weight_kg = weight_kg, height_m = height_m)
    
    def calculate(self):
        """ 
        Calculate BMI from imperial measurements.

        Inputs:
            float(weight_kg)
            float(height_m)
        
        Output:
            float(BMI)
        """

        if type(self.weight_kg) == str:
            self.weight_kg = fm.Text2FloatFormatter(self.weight_kg).format()

        if type(self.height_m) == str:
            self.height_m = fm.Text2FloatFormatter(self.height_m).format()

        bmi = (self.weight_kg) / (self.height_m **2)

        return bmi