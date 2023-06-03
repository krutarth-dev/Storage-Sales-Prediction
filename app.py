import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('storage_sales_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the encoder object
with open('encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)

def predict_sales(input_df):
    # Preprocess input data
    numeric_cols = ['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Outlet_Establishment_Year']
    categorical_cols = ['Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type']

    # Preprocess numeric columns
    numeric_data = input_df[numeric_cols].fillna(0)

    # Preprocess categorical columns
    categorical_data = input_df[categorical_cols].fillna('Unknown')

    # One-hot encode categorical features
    categorical_encoded = encoder.transform(categorical_data)

    # Combine numeric and categorical features
    input_encoded = pd.concat([numeric_data, pd.DataFrame(categorical_encoded, columns=encoder.get_feature_names(categorical_cols))], axis=1)

    # Make predictions
    predictions = model.predict(input_encoded)

    return predictions

def main():
    # Add UI elements for user input
    st.title("Storage Sales Prediction")
    st.write("Enter the details below to predict sales:")
    item_weight = st.number_input("Item Weight")
    item_visibility = st.number_input("Item Visibility")
    item_mrp = st.number_input("Item MRP")
    outlet_establishment_year = st.number_input("Outlet Establishment Year")
    outlet_size = st.selectbox("Outlet Size", ['Small', 'Medium', 'High'])
    outlet_location_type = st.selectbox("Outlet Location Type", ['Tier 1', 'Tier 2', 'Tier 3'])
    outlet_type = st.selectbox("Outlet Type", ['Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3', 'Grocery Store'])

    # Create a dictionary from user input
    input_data = {
        'Item_Weight': [item_weight],
        'Item_Visibility': [item_visibility],
        'Item_MRP': [item_mrp],
        'Outlet_Establishment_Year': [outlet_establishment_year],
        'Outlet_Size': [outlet_size],
        'Outlet_Location_Type': [outlet_location_type],
        'Outlet_Type': [outlet_type]
    }

    # Convert input dictionary to a DataFrame
    input_df = pd.DataFrame(input_data)

    if st.button("Predict"):
        # Call the predict_sales function
        predictions = predict_sales(input_df)

        # Display the predictions
        st.write("Predicted Sales:", predictions)

if __name__ == "__main__":
    main()
