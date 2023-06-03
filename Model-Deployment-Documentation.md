## Storage Sales Prediction Model Deployment Documentation

### Introduction:
This documentation provides an overview of the problems encountered and the solutions applied during the deployment of the storage sales prediction model. It is intended for individuals new to machine learning and serves as a guide to understanding the challenges and solutions implemented in the deployment process.

#### Problem 1: Handling Categorical Data
Description: The dataset used for storage sales prediction contained categorical features that needed to be encoded before training the model.

Solution:

    Imported the necessary libraries: Pandas and Scikit-learn.
    Identified the categorical columns in the dataset.
    Used one-hot encoding to convert the categorical variables into numerical features.
    Created a separate DataFrame for the encoded features.
    Concatenated the encoded features with the numeric features to obtain the final feature matrix.

#### Problem 2: Handling Missing Values
Description: The dataset had missing values in some of the features, which needed to be addressed before training the model.

Solution:

    Used the SimpleImputer class from Scikit-learn to handle missing values.
    Fit the imputer on the training data to learn the mean values of the numeric features.
    Transformed both the training and test data using the imputer to fill in the missing values with the learned means.

#### Problem 3: Model Selection and Training
Description: A suitable model needed to be selected and trained using the preprocessed data.

Solution:

    Chose the Polynomial Regression model as the predictive model.
    Imported the PolynomialFeatures and LinearRegression classes from Scikit-learn.
    Created polynomial features of degree 3 using PolynomialFeatures.
    Split the data into training and test sets using train_test_split from Scikit-learn.
    Fit the Polynomial Regression model to the training data.
    Evaluated the model's performance on the test set using mean squared error (MSE) and R-squared metrics.

#### Problem 4: Saving and Loading the Trained Model
Description: The trained model needed to be saved for future use and loaded during the prediction phase.

Solution:

    Saved the trained model using the joblib library's dump function.
    Created a pickle file to store the trained model.

#### Problem 5: Building a User Interface for Model Prediction
Description: Developed a user interface to allow users to input data and obtain predictions from the trained model.

Solution:

    Utilized the Streamlit library to build a simple user interface.
    Created a form where users could enter the required input data for prediction.
    Preprocessed the input data using the same steps as during training (encoding categorical features and handling missing values).
    Loaded the trained model from the pickle file.
    Used the loaded model to make predictions on the preprocessed input data.
    Displayed the predicted sales value to the user.

Conclusion:
This documentation outlined the problems encountered and the corresponding solutions applied to deploy the storage sales prediction model. By addressing the challenges related to categorical data, missing values, model selection and training, model saving and loading, as well as building a user interface, the model is now capable of accurately predicting storage sales based on user input.
![image](https://github.com/krutarth-dev/Storage-Sales-Prediction/assets/52596504/dc055a0e-0f57-46d6-a8ad-241a5dabe491)

