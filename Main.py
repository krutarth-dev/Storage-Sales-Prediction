import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv('Train.csv')

# Identify the features and target variable
features = ['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type',
            'Item_MRP', 'Outlet_Identifier', 'Outlet_Establishment_Year',
            'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type']
target = 'Item_Outlet_Sales'

# Split the data into features and target variable
X = data[features]
y = data[target]

# Identify the categorical columns
categorical_cols = ['Item_Fat_Content', 'Item_Type', 'Outlet_Identifier',
                    'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type']

# Create the column transformer and fit it on the data
encoder = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(), categorical_cols),
        ('imputer', SimpleImputer(strategy='mean'), ['Item_Weight'])
    ],
    remainder='passthrough'
)
X_encoded = encoder.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the root mean squared error
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f'Root Mean Squared Error: {rmse}')

# Save the encoder object to a file
with open('encoder.pkl', 'wb') as file:
    pickle.dump(encoder, file)
