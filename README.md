## Breast Cancer Classification
#### $\text{The Cell Nuclei in Breast Cancer patients}$

<center><img src="https://github.com/hasmikmar/MLE/blob/main/images/cancer.jpg?raw=true" width="800px" style="width:800px" /></center>

# Motivation

- Breast cancer classification project addresses a meaningful real-world problem with significant social impact. 
- Breast cancer is a prevalent and serious health issue affecting a large portion of the population, particularly women. Early and accurate detection is crucial for successful treatment outcomes. 
- By developing a machine learning model for breast cancer classification, we are contributing to the improvement of diagnostic processes, potentially leading to earlier detection and better patient outcomes. 
- This has a direct and positive impact on society by enhancing healthcare and saving lives.

  # Dataset
Project idea is taken from [Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data).
Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image. 
Number of samples:569, number of features:32

# Problem Formulation

- So we have data of patients with breast cancer
- Our goal is to predict whether the cancer is benign or malignant


# Modeling
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Modelling
- Model selection
- Deployment
  You can see this all [breast-cancer folder](https://github.com/hasmikmar/MLE/tree/main/breast_cancer). 

<center><img src="https://github.com/Daniboy370/Machine-Learning/blob/master/Misc/Latex/Images/pipeline.png?raw=true" width="800px" style="width:800px" /></center>

We have tried different classification algorithms these are the top 3: GradientBoosting, RandomForest, AdaBoost. The best performed RandomForest.
              
              Model    Validation Score
-            Logistic              94.5
-             SVM              93.6
-           AdaBoost              94.7
-       RandomForest              95.3
-      GradientBoosting              94.9

# Deployment
After successful model development and testing, the next crucial step is deploying the breast cancer classification model for practical use.
Our deployment strategy involves utilizing Flask as the web framework for creating a user-friendly interface and Google Cloud for hosting and scalability.

- Flask Integration:
    -  Flask was chosen for its simplicity and ease of integration with Python, making it an ideal choice for creating a web application to host our breast cancer classification model.
    - The Flask web application provides a user interface where patients or medical professionals can fill the form for classification.
- Google Cloud Hosting:
    - Leveraging the capabilities of Google Cloud Platform (GCP), our model is deployed on a virtual machine instance using Google Compute Engine.
    - Google Cloud Storage is utilized for storing and managing the input medical data that users upload for classification.
    - It makes model publicly available.

## Running Locally

To run this project locally, follow these steps:

1. **Navigate to the Deployment Directory:**
    ```bash
    cd deployment
    ```
2. **Run the Application:**

    ```bash
    python3 app.py
    ```
3. **Access the Application:**

    Click on the following link: [Running on http://127.0.0.1:5000/](http://127.0.0.1:5000/)

    This will open the application in your default web browser.

# Demo
You can access to our app in this [link](https://mleproject-408120.an.r.appspot.com/).

<center><img src="https://github.com/hasmikmar/MLE/blob/main/images/img1.jpg?raw=true" width="800px" style="width:800px" /></center>
<center><img src="https://github.com/hasmikmar/MLE/blob/main/images/img2.jpg?raw=true" width="800px" style="width:800px" /></center>
