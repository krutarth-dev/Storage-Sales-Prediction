# 💰 Storage-Sales-Prediction

The project of Sales Prediction for storage entails the examination of a Kaggle dataset and the creation of machine learning models with the purpose of forecasting retail sales. In the fiercely competitive retail industry, businesses continuously seek avenues to enhance their revenue and expand their market presence. Employing machine learning algorithms to forecast sales enables companies to attain valuable insights into consumer behavior and optimize their overall business strategies.

## Importance of the model

Accurately predicting future sales holds significant value for companies as it enables them to enhance their revenue and market share, as well as minimize costs related to inventory management and excess stock. Employing machine learning models, like the ones utilized in this project, can offer a competitive edge to retail businesses striving to maintain a leading position within the industry.


##Project roadmap:

### Data exploration:

In this phase, we will delve into the datasets to understand their features and characteristics. The following insights can be gathered from this exploration:

    Presence of null values in both the testing and training datasets.
    Existence of categorical values that require encoding for prediction and model fitting.

### Data preprocessing:

In this stage, we will perform the following tasks:

   1)Data cleaning:
        Replacement of missing numerical values with the mean of the respective column.
        Substitution of categorical missing data with the mode of the corresponding category.

   2)Feature extraction:
        Encoding of features using label encoding, facilitating easier data processing and utilization. We will employ the LabelEncoder from         sklearn, which assigns a unique number to each distinct value within a column.

   3)Standardization and normalization of data (if necessary):
        Standardizing the data to eliminate redundancy and consolidate values that convey the same meaning but have different                       representations (e.g., 'lf', 'low fat', 'Low Fat' all denote the same concept).
        
        
   ### Data analysis:
   Within this phase, I will perform the following tasks:
   1) Identifying correlations among different variables.
   2) Examining the distribution of items across various categories, based on their respective columns.
   3) Creating plots to visualize regression correlations.   

### Model Selection and Prediction:

In this phase, we will explore various regression models to determine the one that yields the most favorable outcomes in terms of minimizing prediction errors. The models we will employ include:

- Simple Linear Regression
- Multiple Linear Regression
- Polynomial Regression
- Random Forest Regression
- XGBoost Regression

 ### Model Comparison:

In this stage, we will compare the different models implemented in the preceding sections to identify the most effective one. This entails:

- Comparing the models based on their errors and accuracy scores.
- Plotting the results to determine the optimal model.

 ### Conclusion:

To summarize, the Big Market Sales Prediction project encompassed the analysis of a Kaggle dataset and the development of machine learning models for sales prediction in the retail industry. Five distinct models were tested, namely linear regression, multiple regression, polynomial regression, random forest regressor, and XGBoost regressor. The models were evaluated using metrics such as R2 score, Mean Absolute Error (MAE), and Mean Squared Error (MSE).

Upon evaluation, it was discovered that the polynomial regressor with a degree of 3 exhibited the best performance in sales prediction. This model achieved the highest R2 score while maintaining the lowest MAE and MSE values. Therefore, it can be concluded that the polynomial regressor with a degree of 3 provides the most accurate forecast for future sales within the retail industry. 
