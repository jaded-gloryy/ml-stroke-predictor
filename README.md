# Stroke Predictor

This predictor (SVM model) was trained on [health data](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset) pertaining to [strokes](https://www.cdc.gov/stroke/about.htm#:~:text=A%20stroke%2C%20sometimes%20called%20a,brain%20become%20damaged%20or%20die.). Given certain data, it is inteded to predict whether that data incidates if a stroke is likely to happen or not. The demo was created using [gradio](https://www.gradio.app).

*This predictor was made for educational purposes only. It is not intended to and cannot be used to make or predict medical diagnoses.*

### How the demo works
Body mass index (**BMI**) is one of the features of this predictor. A user is first asked to submit a weight and height to calculate BMI.

The user is then asked to submit the following:
- Age
- Gender
- Marital status
- Smoking status
- If they have hypertension [(high blood pressure)](https://www.who.int/news-room/fact-sheets/detail/hypertension#:~:text=Hypertension%20(high%20blood%20pressure)%20is,get%20your%20blood%20pressure%20checked.) 
- If they have [heart disease](https://www.cdc.gov/heartdisease/about.htm#:~:text=The%20term%20“heart%20disease”%20refers,can%20cause%20a%20heart%20attack.)

Finally, a prediction is made of whether the entered data is likely to result in a stroke or not.

### Using this model

[demo.ipynb](demo.ipynb): Contains logic for the interface of this project.

[api.py](api.py): Contains api logic for this demo, including requesting BMI caluclation, requesting a prediction, and supplementary validation functions.

[classes](classes): Contains logic for encoding categorical input data and formatting.

[stroke-prediction.ipynb](stroke-prediction.ipynb): Contains logic for preprocessing health data, training the model, and saving a trained model.

[model.txt](model.txt): Contains the trained, serialized model used in the demo.

[data](data): Contains the health data the model is trained on as well as a BMI table used to calculate BMI percentiles for children and teens under 20. (For children and teens, BMI is age- and sex-specific and is often referred to as BMI-for-age )


## Demo
<video src="data/stroke_pred_demo_clipped.mp4" controls autoplay title="Stroke Predictor Demo"></video>
