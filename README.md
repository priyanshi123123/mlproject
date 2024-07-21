 # MLProject

## Overview

MLProject is designed to predict student performance based on various demographic and educational features. This project implements multiple regression models to predict scores and determines the best-performing model through cross-validation and hyperparameter tuning. This project was created as a comprehensive exercise to understand and implement the complete machine learning workflow, from data ingestion to model deployment.

## Features

- **Data Ingestion**: Automated importing and preprocessing of the dataset.
- **Data Transformation**: Feature engineering and scaling to prepare the data for modeling.
- **Model Training**: Training multiple regression models including Random Forest, Decision Tree, Gradient Boosting, Linear Regression, XGBoost, CatBoost, and AdaBoost.
- **Model Evaluation**: Evaluating models using R² score and selecting the best-performing model.
- **Prediction Pipeline**: Flask application to serve the trained model and make predictions based on user inputs.
- **Deployment**: Ready for deployment on AWS Elastic Beanstalk using AWS CodePipeline.

## Technologies Used

- **Programming Language**: Python
- **Libraries**: Scikit-learn, Pandas, Numpy, Flask, CatBoost, XGBoost, Dill
- **Model Evaluation**: GridSearchCV for hyperparameter tuning
- **Deployment**: AWS Elastic Beanstalk, AWS CodePipeline

