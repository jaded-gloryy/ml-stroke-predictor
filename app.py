import gradio as gr
from api import request_bmi, request_prediction
from config import CONFIG

#demo


with gr.Blocks() as demo:
    gr.Markdown(""" 
                    # Stroke Predictor  
                    This model takes user submitted information and makes a prediction of whether that information is predicted to
                    result in a stroke. [A stroke, sometimes called a brain attack, occurs when something blocks blood supply to 
                    part of the brain or when a blood vessel in the brain bursts. 
                    In either case, parts of the brain become damaged or die.](https://www.cdc.gov/stroke/about.htm#:~:text=A%20stroke%2C%20sometimes%20called%20a,brain%20become%20damaged%20or%20die.)

                """)
    gr.Markdown("""
                        *Disclaimer: This demo is for educational purposes only. I'm not a doctor and this is not intended to
                        inform any medical decisions.*
                        """)
    # calc bmi logic 
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
                            ## Inputs
                            Please input your information below.
                            """)
            with gr.Row():
            
                h_text = gr.Number(label = "Height", minimum = 1)
                h_unit = gr.Radio(["in", "m"], label = "Height units")
                w_text = gr.Number(label = "Weight", minimum = 1)
                w_unit = gr.Radio(["lb", "kg"], label = "Weight units")

            with gr.Row():
                add_btn = gr.Button(value = "Submit")

            with gr.Row(): 
                bmi = gr.Number(label = "BMI", interactive = False, precision = 1)
                run_status = gr.Text(label= "Run Status")
            
            add_btn.click(request_bmi, inputs=[h_text, h_unit, w_text, w_unit], outputs={run_status, bmi})
            
            # get the rest of the inputs and input bmi
            with gr.Row():
                age_in = gr.Number(label = "Age", minimum = 2)
                gend_in = gr.Radio(choices = ["Male", "Female"], label="Gender?")
                marr_in = gr.Radio(choices = ["Yes", "No"], label="Ever Married?")

            with gr.Row():
                res_in = gr.Radio(choices = ["Urban", "Rural"], label="Residence Type")
                hyp_in = gr.Radio(choices = ["Yes", "No"], label="Hypertension?")
                hdis_in = gr.Radio(choices = ["Yes", "No"], label="Heart Disease?")

            with gr.Row():    
                smoke_in = gr.Radio(label = "Smoking Status", choices = ["smokes", "never smoked", "formerly smoked", "Unknown"], show_label = True)
                
            with gr.Row():
                submit_btn = gr.Button("Submit")
            

        with gr.Column():
            with gr.Row():
                gr.Markdown("""
                            ## Prediction
                            After information submission, your prediction will appear here.
                            """)
            pred = gr.Textbox(value = "...", label = "Prediction")
            disclaimer = gr.PlayableVideo(value = CONFIG["NOT_DOC"])
            submit_btn.click(request_prediction, inputs = [age_in, gend_in, res_in, hyp_in, hdis_in, smoke_in, marr_in, bmi], outputs= pred)

if __name__ == "__main__":
    demo.launch()