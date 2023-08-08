import numpy as np
import pandas as pd

class DataInterface:
    def encode(self):
        pass


class Age(DataInterface):
    def __init__(self,df, ref_col):
        self.df = df
        self.ref_col = ref_col
    
    def encode(self):
        """
        
        """
        # initialize df with 0s-80s for age
        age_labels = ["a0", "a10", "a20", "a30", "a40", "a50", "a60", "a70", "a80"]
        # Define the age category ranges and corresponding labels
        age_ranges = [0, 10, 20, 30, 40, 50, 60, 70, 80,90]

        # Use pd.cut to assign age categories based on the specified ranges and labels
        age_category = pd.cut(self.df[self.ref_col], bins=age_ranges, labels=age_labels, right=False)
        for each in age_labels:
            self.df[each] = np.where(age_category == each, 1, 0)
        
        return self.df

class SmokingStatus(DataInterface):
    def __init__(self,df, ref_col):
        self.df = df
        self.ref_col = ref_col
    
    def encode(self):
    
        cats = ["ss_1", "ss_2","ss_3", "ss_4"]
        vals = self.df["smoking_status"].unique()
        col_dict = {key:val for key,val in zip(cats,vals)}

        for each in col_dict.keys():
            self.df[each] = np.where(self.df[self.ref_col] == col_dict.get(each), 1, 0)
        return self.df

#for gender marriage and residence - try to subclass (since they all behave the same)

class SimpleConvert(DataInterface):

    def __init__(self, radius):
        # super().__init__(radius)
        def keyword():
        pass

class Marriage(SimpleConvert):


def get_bmi_bucket(bmi_table, data_table):
# def calculate_Z(bmi_table, data_table):
    """
    Calcuate BMI categories provided bmi lookup table and a dataframe of bmi values.

    Calculate Z based on the provided formula and return a dataframe of Z values.
    """
    def get_row(gender, age):
        """
        Used to lookup rows in bmi table.
        Output: 
            Single row df.
        """
        age_mask = bmi_table["Agemos"] == age
        gender_mask = bmi_table["Sex"] == gender
        
        lookup_row = bmi_table[age_mask & gender_mask]
        
        return lookup_row
    # Define a function to calculate Z
    def bucket_adult_bmi(bmi):

        if bmi < 18.5:
            bmi_bucket = "under weight"
        elif 18.5 <= bmi <= 24.9:
            bmi_bucket = "healthy weight" 
        elif 25.0 <= bmi <=  29.9:
            bmi_bucket = "over weight" 
        else:
            bmi_bucket = "obese" 

        return bmi_bucket

    def bucket_child_bmi(bmi, lookup_row):

        c_under = bmi < lookup_row["P5"].item()
        c_healthy = lookup_row["P5"].item() <= bmi < lookup_row["P85"].item()
        c_over = lookup_row["P85"].item() <= bmi < lookup_row["P95"].item()
        c_obese = bmi >= lookup_row["P95"].item()


        if c_under:
            bmi_bucket = "under weight"
        elif c_healthy:
            bmi_bucket = "healthy weight" 
        elif c_over:
            bmi_bucket = "over weight" 
        else:
            bmi_bucket = "obese" 
        
        return bmi_bucket

    # Create an empty list to store Z values
    bmi_buckets = []

    # Iterate through each row in the data_table
    for index, row in data_table.iterrows():
        gender = 1 if row['gender'] == "Male" else 2
        age = row["age"]
        bmi = row['bmi']
        
        # convert ages below 21 to age in months
        if age < 21:
            age_in_months = age * 12
            age = age_in_months + 0.5 if age_in_months not in [24,240] else age_in_months
        

        # Get the relevant row from the bmi_table
        lookup_row = get_row(gender, age)

        if not lookup_row.empty:
            bucket = bucket_child_bmi(bmi, lookup_row)
        else:
            # Handle the case where no lookup row is found
            bucket = bucket_adult_bmi(bmi)

        bmi_buckets.append(bucket)

    # Add Z_values to the data_table and return as a new dataframe
    data_table['bmi_buckets'] = bmi_buckets
    return data_table

# bucket age 10 year buckets
def encode_ages(df,ref_col):
    """ 
    
    """
    # initialize df with 0s-80s for age
    age_labels = ["a0", "a10", "a20", "a30", "a40", "a50", "a60", "a70", "a80"]
    # Define the age category ranges and corresponding labels
    age_ranges = [0, 10, 20, 30, 40, 50, 60, 70, 80,90]

    # Use pd.cut to assign age categories based on the specified ranges and labels
    age_category = pd.cut(df[ref_col], bins=age_ranges, labels=age_labels, right=False)
    for each in age_labels:
        df[each] = np.where(age_category == each, 1, 0)

def encode_bmi(df,ref_col):

    cats = ["bmi_under", "bmi_healthy", "bmi_over", "bmi_obese"]
    vals = ["under weight", "healthy weight", "over weight", "obese"]
    col_dict = {key:val for key,val in zip(cats,vals)}

    for each in col_dict.keys():
        df[each] = np.where(df[ref_col] == col_dict.get(each), 1, 0)

def encode_gender(df):
    df["is_male"] = np.where(df["gender"] == "Male", 1, 0)

def encode_marriage(df):
    df["c_ever_married"] = np.where(df["ever_married"] == "Yes", 1, 0)

def encode_residence(df):
    df["live_urban"] = np.where(df["Residence_type"] == "Urban", 1, 0)

def encode_smoke_stat(df,ref_col):
    
    cats = ["ss_1", "ss_2","ss_3", "ss_4"]
    vals = df["smoking_status"].unique()
    col_dict = {key:val for key,val in zip(cats,vals)}

    for each in col_dict.keys():
        df[each] = np.where(df[ref_col] == col_dict.get(each), 1, 0)

