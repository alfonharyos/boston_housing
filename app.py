import streamlit as st
from predict import pred

def main():
    st.title("Boston Housing")

    # Create input fields for all 11 features
    input_values = {}
    input_labels = {
        'crim': 'CRIM',
        'zn': 'ZN',
        'indus': 'INDUS',
        'nox': 'NOX',
        'rm': 'RM',
        'age': 'AGE',
        'rad': 'RAD',
        'tax': 'TAX',
        'ptratio': 'PTRATIO',
        'b': 'B',
        'lstat': 'LSTAT'
    }
    for feature_name, feature_label in input_labels.items():
        input_values[feature_name] = st.text_input(feature_label)
    
    # Check if all inputs have been filled
    all_filled = all(input_values.values())

    # Create submit button if all inputs have been filled
    if all_filled and st.button("Submit"):
        # Convert input values to floats
        input_array = [[float(value) for value in input_values.values()]]

        # Make prediction and display result
        value = pred(input_array)
        st.write(f"Prediksi Nilai medv : {value:.3f}")

if __name__ == "__main__":
    main()
