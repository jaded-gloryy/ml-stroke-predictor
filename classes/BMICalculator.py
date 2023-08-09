class BMICalculator:
    def __init__(self, weight_lb =  None, height_ft_in =  None, weight_kg =  None, height_m =  None, age = None):
        self.weight_lb = weight_lb
        self.height_ft_in = height_ft_in
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.age = age

    def bmi_standard(self):
        """ 
        Inputs:
            height_ft_in = (height feet, height in)
            weight_lb = 
        """
        height = (self.height_ft_in[0] * 12) + self.height_ft_in[1]
        bmi = self.weight_lb / (height **2)

        return bmi

    def bmi_imperial(self):

        bmi = self.weight_kg / (self.height_m **2)

        return bmi