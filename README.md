# Crop Prediction Model

Welcome to the Crop Prediction Model repository! This project implements a Random Forest-based model for predicting the most suitable crop based on user-inputted values of soil potassium, phosphorous, nitrogen levels, temperature, humidity, and soil type.

![Crop Prediction Model](/path/to/your/image.png)

## About the Model

The Crop Prediction Model employs a powerful Random Forest algorithm to predict the optimal crop to cultivate based on specific soil and environmental conditions. This machine learning model has been meticulously trained and fine-tuned to deliver exceptional accuracy.

## Model Accuracy

After rigorous testing and evaluation, the Random Forest model achieved an impressive accuracy rate of 99.92%. This remarkable performance has been determined through extensive benchmarking against other models, highlighting the effectiveness of the chosen approach.

The details of the models considered during the development process, along with their respective accuracies, can be found in the `data_exploration.ipynb` file.

## Technology Stack

The Crop Prediction Model consists of two integral components: the backend, developed using the Flask framework, and the frontend, designed with HTML and CSS.

### Backend
- Framework: Flask
- Python Version: [Specify Python version]
- Dependencies: [List any required Python packages and their versions]

### Frontend
- HTML
- CSS

## How to Use

To harness the capabilities of the Crop Prediction Model, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary dependencies using the provided `requirements.txt` file.
4. Run the Flask application using the command: `python app.py`.
5. Access the model's user interface by opening a web browser and navigating to `http://localhost:5000`.

On the user interface, provide input values for the following parameters:
- Soil potassium level
- Soil phosphorous level
- Soil nitrogen level
- Temperature
- Humidity
- Soil type

After submitting the input, the model will perform its predictions and display the most suitable crop based on the input conditions.

## Model Selection Process

The Crop Prediction Model was chosen after a thorough evaluation of various models. The Random Forest algorithm exhibited exceptional performance, achieving an accuracy rate of 99.92%. Detailed insights into the model selection process can be found in the `data_exploration.ipynb` file.

## Requirements

Ensure you have the required dependencies installed by running:
