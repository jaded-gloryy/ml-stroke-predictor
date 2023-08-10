#make a interface with .calcuate
#make 2 concrete classes
# format text input --> private method

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
        if type(self.fheight_ft_in) == str:
            height_ft_in = self._format_standard_height(height_ft_in)
        
        height = (self.height_ft_in[0] * 12) + self.height_ft_in[1]
        bmi = self.weight_lb / (height **2)

        return bmi
    
    def _format_standard_height(standard_height):
        """ 
        Format text input.

        Input:
            "feet,inches" ; ex: "5,2"
        Output:
            (int(feet), int(inches)); ex: (5, 2)
        """

        height = standard_height.split(",")
        
        try: 
            height_tup = (float(height[0]), float(height[1]))
        except:
            print("Input must contain only numbers separated by \",\". Ex: \"5,2\" for 5 feet, 2 inches")

        return height_tup

    class StandardBMICalculator(BMICalculatorInterface):
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
            bmi = self.weight_kg / (self.height_m **2)

            return bmi