🌾 Crop Recommendation System Using Random Forest
📌 Project Overview

The Crop Recommendation System is a machine learning project that recommends the most suitable crop to cultivate based on soil nutrient levels and environmental conditions. It uses the Random Forest Classifier to predict the optimal crop from the given agricultural parameters.

The system helps farmers make data-driven decisions, improve crop selection, and support sustainable agricultural practices.

🎯 Objectives
Recommend suitable crops based on soil and environmental parameters.
Apply machine learning techniques to agricultural data.
Train a Random Forest Classifier for crop classification.
Evaluate model performance using standard classification metrics.
Provide a simple and efficient crop recommendation system.
📊 Dataset Information

The project uses a crop recommendation dataset containing 2,201 records.

The dataset includes the following features:

Feature	Description
N	Nitrogen content in the soil
P	Phosphorus content in the soil
K	Potassium content in the soil
temperature	Temperature in degrees Celsius
humidity	Relative humidity percentage
ph	Soil pH value
rainfall	Rainfall in millimeters
label	Recommended crop class

The target variable is label, which represents the crop recommended for the given soil and environmental conditions.

🤖 Machine Learning Algorithm
Random Forest Classifier

The main classification algorithm used in this project is the Random Forest Classifier.

Random Forest is an ensemble learning algorithm that combines predictions from multiple decision trees to produce a final classification. It is suitable for this project because it can learn nonlinear relationships between soil conditions, weather parameters, and crop types.

Key advantages:

Handles multiple numerical input features.
Captures complex relationships in agricultural data.
Reduces overfitting compared with relying on a single decision tree.
Supports multiclass classification.
Provides feature importance scores for model interpretation.
⚙️ Technologies Used
Python — Core programming language
Pandas — Data manipulation and analysis
NumPy — Numerical computations
Scikit-learn — Model training and evaluation
Matplotlib / Seaborn — Data visualization, if used
Streamlit — Web application interface, if implemented
🔄 Project Workflow
Data Collection: Load the crop recommendation dataset containing 2,201 records.
Data Preprocessing: Inspect missing values, duplicate records, feature types, and target labels.
Exploratory Data Analysis: Analyze the distributions and relationships among soil and weather parameters.
Feature Selection: Use nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall as input features.
Data Splitting: Divide the dataset into training and testing sets.
Model Training: Train the Random Forest Classifier on the training data.
Model Evaluation: Evaluate predictions using accuracy, precision, recall, F1-score, and a confusion matrix.
Crop Recommendation: Predict the crop class for new soil and environmental measurements.
🧪 Model Evaluation

The model can be evaluated using the following metrics:

Accuracy: Percentage of correctly classified samples.
Precision: Proportion of correct predictions among samples predicted as a particular crop.
Recall: Proportion of actual samples of a crop correctly identified.
F1-score: Harmonic mean of precision and recall.
Confusion Matrix: Shows correct and incorrect classifications for each crop class.

Actual performance values should be reported after running the trained model on the held-out test set.



Adjust the filenames and structure to match your actual repository.

🚀 Installation and Setup
1. Clone the Repository
git clone https://github.com/mr_ankit360/Crop_Prediction_Project.git

cd Crop-Recommendation-System


Replace the repository URL with your actual GitHub repository.

2. Create a Virtual Environment
python -m venv .venv


Activate it on Windows:

.venv\Scripts\activate

3. Install Dependencies

Create a requirements.txt file containing the libraries required by your implementation. For a typical Random Forest project:

Install the dependencies:

pip install -r requirements.txt

4. Run the Project

For a Python script:

python crop_recommendation.py


For a Streamlit web application:

streamlit run app.py


Run the command corresponding to the files available in your project.

🌱 Expected Output

The system accepts the following inputs:

Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Humidity
Soil pH
Rainfall

The trained Random Forest Classifier predicts a crop label based on these inputs.

Example: Given a set of soil nutrient values and environmental conditions, the system might recommend rice, maize, chickpea, or another crop represented in the training dataset. The actual recommendation depends on the model's learned patterns.


⚠️ Limitations

The system's recommendations depend on the quality, representativeness, and distribution of the training dataset. Predictions should be treated as decision-support suggestions rather than guaranteed agricultural outcomes. Local climate, crop varieties, irrigation, season, soil characteristics, and farming practices should also be considered.

👨‍💻 Author

Ankit Kumar
