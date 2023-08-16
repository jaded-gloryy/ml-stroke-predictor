import os
import traceback
import pickle
from pandas import DataFrame as df
import pandas as pd

import classes.BMICalculator as bmic
import classes.Encoders as enc
from config import CONFIG

# get child bme ref table
child_bmi_data = CONFIG["CHILD_BMI"]
child_bmi_df = pd.read_csv(child_bmi_data)

# import model
with open ("model.txt", "rb") as file:
    model = pickle.load(file)
    file.close()

def calc_bmi(data):
        height = data["h_text"]
        height_unit = data["h_unit"]
        weight = data["w_text"]
        weight_unit = data["w_unit"]
    
        if height_unit == "m":
            imp_obj = bmic.MetricBMICalculator(weight_kg = weight, height_m = height)
            bmi = imp_obj.calculate()
        else:
            imp_obj = bmic.ImperialBMICalculator(weight_lb = weight, height_in = height)
            bmi = imp_obj.calculate()
        
        return bmi

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def request_bmi(*args):
    """Validate input, request bmi"""
    data = {
        "h_text": args[0],
        "h_unit": args[1],
        "w_text": args[2],
        "w_unit": args[3]
    }


    try:
        run_status = "Successful run!"
        valid_input = validate_input(data)
        
        if not valid_input:
            raise Exception(run_status)

        bmi = calc_bmi(data)
        return bmi , run_status
    
    except Exception as error:
        traceback.print_exc()
        print (str(error))
        return 0, str(error)

def validate_input(data):
        """ 
        Validate that one unit type was selected and that each is a number.
        """
        height = data["h_text"]
        weight = data["w_text"]
        height_unit = data["h_unit"]
        weight_unit = data["w_unit"]

        is_zero = any([i == 0 for i in [height, weight]])
        missing_data = any([i is None for i in [height, weight, height_unit, weight_unit]]) 
        if missing_data or is_zero:
            run_status = "Please enter information and try again."
            raise Exception(run_status)
        
        # check if units are consistent
        imperial = ["in", "lb"]
        metric = ["m", "kg"]
        is_imperial = set(imperial) == set([height_unit, weight_unit])
        is_metric = set(metric) == set([height_unit, weight_unit])
        consistent = any([is_imperial, is_metric])
        
        if not consistent:
             run_status = "BMI input units need to be consitently metric (kg and m) or imperial (in and lb). Please try again"
             raise Exception(run_status)
        
        # check that each only contains numbers
        valid_input = all(isfloat(i) for i in [height,weight])

        if not valid_input:
            run_status = "All inputs must be numeric"
            raise Exception(run_status)

        return valid_input

def encode_pred(df, final_cols):

    if all(df["age"] > 19):
        bmi = enc.AdultBMIEncoder(df).encode()
    else:
        bmi = enc.ChildBMIEncoder(bmi_table= child_bmi_data, data_table= df).encode()
    enc.one_hot_enc_bmi(df,"bmi_buckets")
    enc.GenderEncoder(df,"gender").encode()
    enc.AgeEncoder(df,"age").encode()
    enc.MarriageEncoder(df,"ever_married").encode()
    enc.ResidenceEncoder(df,"Residence_type").encode()
    enc.SmokingStatusEncoder(df, "smoking_status").encode()
    enc.HypertensionEncoder(df,"hypertension").encode()
    enc.HeartDiseaseEncoder(df,"heart_disease").encode()
    df = df[final_cols]

    return df

def prep_pred_data(*args):
    """
    Create dataframe to make a prediction on.
    
    """

    data = args
    new_df_dict = {}
    
    new_df_dict["age"] = data[0][0]
    new_df_dict["gender"] = data[0][1]
    new_df_dict["Residence_type"] = data[0][2]
    new_df_dict["hypertension"] = data[0][3]
    new_df_dict["heart_disease"] = data[0][4]
    new_df_dict["smoking_status"] = data[0][5]
    new_df_dict["ever_married"] = data[0][6]
    new_df_dict["bmi"] = data[0][7]
    

    col_order = ["age", "hypertension",	"heart_disease", "bmi_under",	"bmi_healthy",	"bmi_over",	"bmi_obese", "is_male",	"c_ever_married",	"live_urban",	"ss_1",	"ss_2",	"ss_3",	"ss_4"]
    pred_df = df.from_dict([new_df_dict])
    encoded_pred_df = encode_pred(pred_df, col_order)

    return encoded_pred_df

def request_prediction(*args):
    """
    Request user input and predict data
    
    """
    data = args

    try:
        pred_df = prep_pred_data(data)
        stroke_pred = model.predict(pred_df)
        stroke = "Stroke predicted"
        no_stroke = "No stroke predicted"
        pred_val = stroke if stroke_pred == 1 else no_stroke
        return pred_val
    except Exception as error:
        traceback.print_exc()
        print (str(error))