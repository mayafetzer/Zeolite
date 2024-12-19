# Project: Zeolite

## Author
Maya Fetzer  
Semester: Fall 2024  
Course: CHEG 472  

## Purpose
This repository creates an app to model if zeolite formation is successful.

Zeolites are essential materials with applications in catalysis, separation, and adsorption. However, their
traditional synthesis relies on organic structure-directing agents (OSDAs), which are expensive and
environmentally unfriendly. Seed-assisted zeolite synthesis provides a green and economical alternative by
reducing or eliminating the need for OSDAs. Despite its potential, identifying optimal synthesis conditions
remains a challenge due to the high-dimensional chemical space involved.

To address this challenge, your task is to develop a machine learning model that predicts the success of seed-
assisted zeolite synthesis experiments using a provided dataset. The dataset contains 385 historical records of seed-assisted zeolite synthesis experiments conducted in a trial-and-error manner. Each experiment is
categorized into one of two classes:

• Class "0": Failed experiments resulting in amorphous, mixed, dense, or layered phases.

• Class "1": Successful experiments resulting in a pure zeolite phase.

The dataset includes the following parameters:

1. Seed properties:
   
o Seed amount (normalized to SiO2 weight = 1)

o Seed framework density (FD) in T/Å3

o Seed Si/Al molar ratio (measured using ICP-AES)

2. Gel composition:
   
o SiO2 (normalized to 1)

o NaOH/SiO2 molar ratio

o B2O3/SiO2 molar ratio

o H2O/SiO2 molar ratio

o OTMAC/SiO2 molar ratio (SDA)

3. Crystallization conditions:
   
o Crystallization temperature (°C)

o Crystallization time (days)

## Summary of Analysis

Overall, while there are not strong correlations present in the dataset, it is possible to create a machine learning GUI platform to predict the success of different zeolite formations. 

The best model chosen was random forest, but it did not show a great test-train split. If further time permitted, I would have liked to continue to hyperparameter train the model to make sure that it worked the best it could. I would have also liked to continue to try a variety of different models to see if any other models would have been better at predicted the success or failure of the zeolite formation.

This model can be used for researchers to have a better understanding of what to prioritize when forming zeolites. It is important for researchers to save time and effort in the lab because that ultimately saves money for the person who is paying for the research.

When using this model, it is important to recognize that the R2 is not perfect and that it will not always be completely accurate in its prediction. The model needs to be used with caution and in the future if further time permitted, the model could be reinforced with results gained from a lab so that it could become more accurate. 

## Public App
Here is the public app for the model: https://huggingface.co/spaces/mayafetzer/Zeolite

## Files in this repository

Dataset_3_zeeolites.xlsx - the dataset provided for analysis

best_model.pkl - the pickle file with the model

scaler.pkl - the pickle file with the scaler

app.py - the app code for the HuggingFace platform

requirements.txt - the requirements file for the HuggingFace GUI

Fetzer_CHEG472_FINAL.ipynb - the Google colab file used for analysis


## Prerequisites

### Python
Ensure you have Python 3.10 or later installed.

### Libraries
Install the following libraries using pip:

```
pip install gradio
pip install pandas
pip install numpy
pip install sklearn
pip install openpyxl
pip install pickle5
```

## Explanation

- **Streamlit**: Provides a simple way to create interactive web applications with Python.
- **Matplotlib**: Used for creating visualizations like plots and charts.
- **Pandas**: Offers data structures and analysis tools for working with tabular data.
- **NumPy**: Provides efficient numerical operations and arrays.
- **Sklearn**: Machine learning library.
- **Gradio:** A user-friendly library for building and sharing interactive web interfaces for machine learning models and data science projects.
- **Openpyxl:** A library for reading and writing Excel files in the XLSX format, making it easy to work with spreadsheets directly from Python.
- **Pickle5:** An enhanced version of Python's pickle module for object serialization and
