---
title: ML Stroke Predictor
emoji: 🧪
colorFrom: pink
colorTo: indigo
sdk: docker
# sdk: gradio
# sdk_version: 3.39.0
python_version: 3.10.2
app_file: app.py
pinned: true
---

# ML Stroke Predictor

This predictor (SVM model) was trained on [health data](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset) pertaining to [strokes](https://www.cdc.gov/stroke/about.htm#:~:text=A%20stroke%2C%20sometimes%20called%20a,brain%20become%20damaged%20or%20die.). Given certain data, it is inteded to predict whether that data incidates if a stroke is likely to happen or not. The demo was created using [gradio](https://www.gradio.app).

## Demo
[Link to Demo on Huggingface](https://huggingface.co/spaces/jaded-gloryy/ml-stroke-predictor)

*This predictor was made for educational purposes only. It is not intended to and cannot be used to make or predict medical diagnoses.*

## Description:

This is a supervised learning, classification task, using a Support Vector Machine (SVM). The data used to train this model contains 10 features. The final model utilizes 8 features:  
- age
- BMI
- gender
- has heart disease
- has hypertension
- marriage status
- residence type (urban or rural)
- smoking status

I used pandas to preprocess the data and scikit learn to train and test the model. “Stroke” examples represents 5% of the full dataset, and the model is accurate ~94% of the time.

## Challenges:

*Abstractions*  
>This was my first time implementing abstractions throughout the programming process. Typically I  get function happy, only to come back later and implement classes. Throughout this project I was able to see and experience the benefits of building abstractions right into the process through the encoder classes I incorporated.

*UI Interface*  
>This was my first time using gradio (or any user facing interface for a ml model) along with balancing error handling from user inputs vs choosing interfaces with the proper constraints built in. Figuring out where to call out or raise an error was also a new challenge due to the different abstractions I implemented. I learned how to build the interface for my model separate and independent of using the model itself.

*Integrations*  
>Integrating my GitHub repo with a HuggingFace "Space" was a bit challenging. I wasn't initially familiar with the process but I was able to find documentation on how to sync my repo with a HuggingFace repo using GitHub actions. Now everytime I push code to my "main" branch it will perform an upload to the "space" on hugging face. After getting those to work seamlessly, and adding the necessary items for integration (yml in the ReadMe and an app.py file), I did some troubleshooting to ensure that proper versions of all my dependencies were installed and there were no conflicts. 

*Future work*  
>Going forward I’d like to test a few different models to compare their performance to this SVM. I’m particualry interested in producing confidence intervals around these predictions. I would also like to look deeper into my error rate, ie. what percent of predictions are false positives (a stroke is predicted when no stroke occurred) and also negatives (no stroke is predicted when a stroke has occurred).

### How the demo works
Body mass index (**BMI**) is one of the features of this predictor. A user is first asked to submit a weight and height to calculate BMI.

The user is then asked to submit the following:
- Age
- Gender
- Marital status
- Smoking status
- Resdience type 
- If they have hypertension [(high blood pressure)](https://www.who.int/news-room/fact-sheets/detail/hypertension#:~:text=Hypertension%20(high%20blood%20pressure)%20is,get%20your%20blood%20pressure%20checked.) 
- If they have [heart disease](https://www.cdc.gov/heartdisease/about.htm#:~:text=The%20term%20“heart%20disease”%20refers,can%20cause%20a%20heart%20attack.)

Finally, a prediction is made of whether the entered data is likely to result in a stroke or not.

### Using this model

#### To run locally:

Clone this repository.
````
$ git clone https://github.com/jaded-gloryy/ml-stroke-predictor.git
````
Change the last line in app.py to:

````
if __name__ == "__main__":
    demo.launch(server_name=None, server_port=7860)
````
Run the following command. A link to the demo will be generated as output.
```
$ python app.py
```

### File summary
[Dockerfile](Dockerfile): Contains logic for 

[demo.ipynb](demo.ipynb): Contains logic for the interface of this project.

[api.py](api.py): Contains api logic for this demo, including requesting BMI caluclation, requesting a prediction, and supplementary validation functions.

[classes](classes): Contains logic for encoding categorical input data and formatting.

[stroke-prediction.ipynb](stroke-prediction.ipynb): Contains logic for preprocessing health data, training the model, and saving a trained model.

[model.txt](model.txt): Contains the trained, serialized model used in the demo.

[data](data): Contains the health data the model is trained on as well as a BMI table used to calculate BMI percentiles for children and teens under 20. (For children and teens, BMI is age- and sex-specific and is often referred to as BMI-for-age )


<!-- ## Demo
<video src="data/stroke_pred_demo_clipped.mp4" controls autoplay title="Stroke Predictor Demo"></video> -->
