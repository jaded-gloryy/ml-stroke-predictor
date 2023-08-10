class Formatter:
    def __init__(self,text):
        self.text = text
    
    def format():
        pass

class ImperialMeasurementTextFormatter(Formatter):
    def __init__(self, text):
        super().__init__(text)

    def format(self):
        """ 
        Format standard height measurement text input.

        Input:
            "feet,inches" ; ex: "5,2"
        Output:
            (int(feet), int(inches)); ex: (5, 2)
        """

        height = self.text.split(",")
        
        try: 
            height_tup = (float(height[0]), float(height[1]))
        except:
            print("Input must contain only numbers separated by \",\". Ex: \"5,2\" for 5 feet, 2 inches")

        return height_tup
    
class Text2FloatFormatter(Formatter):
    def __init__(self, text):
        super().__init__(text)

    def format(self):
        """ 
        Convert any text number to a float.

        Input:
            "50.2"
        Output:
            float(50.2)
        """

        try: 
            f_text = float(self.text)
        except:
            print("Input must contain only numbers")  
        
        return f_text