import gradio as gr
import pickle
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# Load models and scaler
with open('best_model.pkl', 'rb') as f:
    best_model = pickle.load(f)

# Load the pre-fitted scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Define the one-hot encoder for the `seed` categorical variable
seed_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# Fit the encoder on the list of possible seed values (only need to do this once)
seed_values = ['MRE', 'ERI', 'EUO', 'IWV', 'MFI', 'MTT', 'MWW', 'SFE', 'TON']  # Example list of possible seeds
seed_encoded = seed_encoder.fit_transform(np.array(seed_values).reshape(-1, 1))  # Fit and transform known seeds

def predict(seed, NaOH, SDA, B2O3, seed_amount, time, si_al, fd):
    """
    Predict the output based on the given parameters.
    
    Parameters:
    - seed: Seed input variable (categorical: string)
    - NaOH: NaOH input variable (numerical)
    - SDA: SDA input variable (numerical)
    - B2O3: B2O3 input variable (numerical)
    - seed_amount: Seed amount input (numerical)
    - time: Time input variable (numerical)
    - si_al: Si/Al ratio input (numerical)
    - fd: FD input variable (numerical)
    
    Returns:
    - Output prediction (rounded to 2 decimal places)
    """
    
    # Get the index of the input `seed` in the encoded array
    seed_index = seed_values.index(seed)
    seed_vector = seed_encoded[seed_index]  # Get the one-hot encoded vector for the seed
    
    # Prepare the input array with the provided parameters, including the one-hot encoded seed
    input_array = np.array([[NaOH, SDA, B2O3, seed_amount, time, si_al, fd] + list(seed_vector)])
    
    # Scale input values using the pre-fitted scaler
    input_scaled = scaler.transform(input_array)

    # Make prediction using the best model
    output = best_model.predict(input_scaled)[0]

    return round(output, 0)  # Return the prediction to be either a success or a fail

# Create the Gradio interface with sliders for each input variable
iface = gr.Interface(
    fn=predict,  # The prediction function you defined earlier
    inputs=[
        # Dropdown for categorical seed variable
        gr.Dropdown(
            choices=["MRE", "ERI", "EUO", "IWV", "MFI", "MTT", "MWW", "SFE", "TON"], 
            label="Seed Type"
        ),
        gr.Slider(0, 1, step=0.01, label="NaOH (mol/L)"),
        gr.Slider(0, 1, step=0.01, label="SDA (mol/L)"),
        gr.Slider(0, 1, step=0.01, label="B2O3 (%)"),
        gr.Slider(0, 1, step=0.01, label="Seed Amount (g)"),
        gr.Slider(0, 300, step=1, label="Time (min)"),
        gr.Slider(0, 1, step=0.01, label="Si/Al Ratio"),
        gr.Slider(0, 1, step=0.01, label="FD (%)"),
    ],
    outputs=gr.Label(label="Zeolite Success. A 0 indicates failure while a 1 indicates success."),
    title="Zeolite Prediction Model",
    description="Adjust the sliders and select the features of the zeolite to predict success. Note that all inputs should be normalized."
)

# Launch the interface
iface.launch(share=True)
