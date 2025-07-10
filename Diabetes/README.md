# Healthcare Diabetes Prediction

## Project Description
This project develops a machine learning solution to predict diabetes in patients based on various health indicators including pregnancies, glucose levels, blood pressure, skin thickness, insulin levels, BMI, genetic factors, and age to determine the likelihood of diabetes.

The analysis is based on data sourced from Kaggle, specifically the Healthcare Diabetes Dataset available at https://www.kaggle.com/datasets/nanditapore/healthcare-diabetes/data 

## Problem Statement
Diabetes is a chronic disease that affects millions of people worldwide and can lead to serious health complications if left undiagnosed or untreated. Early detection and prediction of diabetes can significantly improve patient outcomes and reduce healthcare costs. This project aims to create an accurate predictive model that can assist healthcare professionals in identifying patients at risk of diabetes based on readily available clinical measurements.

## Dataset Description
The dataset contains health information for diabetes prediction with the following features:

### Columns:
1.	Id: Unique identifier for each data entry.
2.	Pregnancies: Number of times pregnant.
3.	Glucose: Plasma glucose concentration over 2 hours in an oral glucose tolerance test.
4.	Blood Pressure: Diastolic blood pressure (mm Hg).
5.	Skin Thickness: Triceps skinfold thickness (mm).
6.	Insulin: 2-Hour serum insulin (mu U/ml).
7.	BMI: Body mass index (weight in kg / height in m^2).
8.	Diabetes Pedigree Function: Diabetes pedigree function, a genetic score of diabetes.
9.	Age: Age in years.
10.	Outcome: Binary classification indicating the presence (1) or absence (0) of diabetes.

## Methodology Overview
This project implements and compares multiple machine learning algorithms to identify the best performing model for diabetes prediction:

1.	Logistic Regression - Linear approach for binary classification
2.	Support Vector Classifier (SVC) - Support vector machine for classification
3.	Naive Bayes - Probabilistic classifier based on Bayes' theorem
4.	K-Nearest Neighbors (KNN) - Instance-based learning algorithm
5.	Decision Tree - Tree-based decision-making model
6.	Random Forest - Ensemble method using multiple decision trees
7.	XGB Classifier - Gradient boosting classifier

### Data Preprocessing
1. Train-test split for model validation

### Model Evaluation
1. Accuracy score calculation
2. Classification reports
3. Confusion matrix analysis

## Key Findings and Insights

### Model Performance Comparison
1. Random Forest	99.64%
2. Decision Tree	98.92%
3. XGB Classifier	98.01%
4. K-Nearest Neighbors	77.62%
5. Support Vector Classifier	76.17%
6. Naive Bayes	75.27%
7. Logistic Regression	68.05%

### Key Insights
1.	Random Forest achieved the highest accuracy (99.64%), making it the best performing model for this dataset
2.	Tree-based models (Random Forest, Decision Tree, XGBoost) significantly outperformed other algorithms
3.	Ensemble methods like Random Forest and XGBoost showed superior performance compared to single algorithms
4.	Traditional linear models like Logistic Regression showed lower performance, suggesting non-linear relationships in the data

## Installation and Setup
### Prerequisites
1. Python 3.7 or higher
2. pip package manager

### Required Dependencies
bash

Install all dependencies at once

pip install -r requirements.txt

## Usage Instructions

1. Clone the Repository
   
   git clone https://github.com/Taktom-M/healthcare-diabetes.git

   cd healthcare-diabetes

2. Install Dependencies
   
   pip install -r requirements.txt

## Future Improvements
1. Feature engineering and selection
2. Hyperparameter tuning for optimal performance
3. Cross-validation for more robust evaluation
4. Integration with healthcare systems
