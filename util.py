import pickle
import json
import numpy as np
import pandas as pd

#__data_columns = None
#__model = None

with open('model.pkl', 'rb') as f:
    __model = pickle.load(f)

with open("columns.json", "r") as f:
    __data_columns = json.load(f)['data_columns']

def predict_laptop_price(inches, ram_gb, ssd, hdd, flash_storage, touchscreen, company, type_name, cpu_brand, gpu_brand):
    # Create a DataFrame with columns matching your laptop dataset
    input_data = pd.DataFrame(columns=__data_columns)

    # Fill in the input_data DataFrame with the provided features
    input_data.loc[0] = [inches, ram_gb, ssd, hdd, flash_storage, touchscreen] + [0] * (len(__data_columns) - 6)
    input_data.loc[0, company] = 1
    input_data.loc[0, type_name] = 1
    input_data.loc[0, cpu_brand] = 1
    input_data.loc[0, gpu_brand] = 1

        # Predict the laptop price
    log_predicted_price = __model.predict(input_data)[0]

    # Transform the prediction back to the original scale
    predicted_price = np.exp(log_predicted_price)
    
    return predicted_price

def load_saved_artefacts():
    global __data_columns
    global __model

    #if __model is None:
        

    #if __data_columns is None:
    

if __name__ == '__main__':
    load_saved_artefacts()
    predicted_price = predict_laptop_price(15.6, 32, 0, 1000, 0, 0, 'Company_Apple', 'TypeName_Notebook', 'CPU Brand_Intel Core i7','GPU Brand_AMD')
    print(f"Predicted Price: €{predicted_price:.2f}")
    
    #print(predict_laptop_price(15.6, 8, 256, 1000, 0, 1, 'Company_HP', 'TypeName_Gaming', 'CPU Brand_Intel Core i5', 'GPU Brand_Nvidia'))

