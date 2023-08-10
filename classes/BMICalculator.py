#make a interface with .calcuate
#make 2 concrete classes
# format text input --> private method
import classes.Formatter as fm

class BMICalculatorInterface:
    def __init__(self, weight_lb =  None, height_ft_in =  None, weight_kg =  None, height_m =  None, age = None):
        self.weight_lb = weight_lb
        self.height_ft_in = height_ft_in
        self.weight_kg = weight_kg
        self.height_m = height_m
    
    def calculate(self):
        pass

class StandardBMICalculator(BMICalculatorInterface):
    def __init__(self, weight_lb, height_ft_in) -> None:
        super().__init__(weight_lb, height_ft_in)

    def calculate(self):
        """ 
        Calculate BMI using standard measurments.
        Inputs:
            height_ft_in = (height feet, height in)
            weight_lb = int() or float()
        
        Output:
            float(BMI)
        """
        if type(self.height_ft_in) == str:
            self.height_ft_in = fm.StandardMeasurementTextFormatter(self.height_ft_in).format()
        
        if type(self.weight_lb) == str:
            self.weight_lb = fm.Text2FloatFormatter(self.weight_lb).format()
        
        height = (self.height_ft_in[0] * 12) + self.height_ft_in[1]
        bmi = (float(self.weight_lb) / (height **2)) * 703

        return bmi
    
   
    class ImperialBMICalculator(BMICalculatorInterface):
        def __init__(self, weight_kg, height_m) -> None:
            super().__init__(weight_kg, height_m)
        
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