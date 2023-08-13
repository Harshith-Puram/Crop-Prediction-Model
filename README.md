# Crop Prediction Model

Welcome to the Crop Prediction Model repository! This project implements a Random Forest-based model for predicting the most suitable crop based on user-inputted values of soil potassium, phosphorous, nitrogen levels, temperature, humidity, and soil type.

## Web Interface
![HOME PAGE](https://github.com/druvikan/Crop-Prediction-Model/assets/97737525/e56c1958-f805-48bf-b201-cb2e5b24f484)

## About the Model

The Crop Prediction Model employs a powerful Random Forest algorithm to predict the optimal crop to cultivate based on specific soil and environmental conditions. This machine-learning model has been meticulously trained and fine-tuned to deliver exceptional accuracy.

## Model Accuracy

After rigorous testing and evaluation, the Random Forest model achieved an impressive accuracy rate of 99.92%. This remarkable performance has been determined through extensive benchmarking against other models, highlighting the effectiveness of the chosen approach.

The details of the models considered during the development process, along with their respective accuracies, can be found in the `data_exploration.ipynb` file.

## Technology Stack

The Crop Prediction Model consists of two integral components: the backend, developed using the Flask framework, and the frontend, designed with HTML and CSS.

### Backend
Framework: Flask
Python Version: 3.9.6
Dependencies: 
- numpy==1.21.2
- pandas==1.3.3
- scikit-learn==0.24.2


### Frontend
- HTML
- CSS

## How to Use

To harness the capabilities of the Crop Prediction Model, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary dependencies using the provided `requirements.txt` file.
4. Run the Flask application using the command: `main.py`.
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

The Crop Prediction Model was chosen after a thorough evaluation of various models. The Random Forest algorithm exhibited exceptional performance, achieving an accuracy rate of 99.92%. Detailed insights into the model selection process can be found in the `dataset exploration.ipynb` file.

## Requirements

Ensure you have the required dependencies installed by running:
pip install -r requirements.txt


## Contributing

Contributions to enhance and extend the capabilities of the Crop Prediction Model are highly welcome. If you wish to contribute, please adhere to these steps:

1. Fork the repository.
2. Create a new branch dedicated to your feature or improvement.
3. Implement your changes and ensure comprehensive testing.
4. Submit a pull request, detailing the modifications and the underlying rationale.

## Credits

This machine-learning marvel was brought to life by the collaborative efforts of [Druvika Nuthalapati](https://github.com/druvikan) and [Harshith Puram](https://github.com/Harshith-Puram), fueled by the demand for accurate and data-driven crop prediction in agriculture.

## Contact

For inquiries, issues, or suggestions, please feel free to reach out via druvikan@gmail.com or harshithppuram@gmail.com.

We extend our gratitude for your interest in the Crop Prediction Model project. It is our hope that this model proves to be an invaluable asset for agricultural decision-making.
