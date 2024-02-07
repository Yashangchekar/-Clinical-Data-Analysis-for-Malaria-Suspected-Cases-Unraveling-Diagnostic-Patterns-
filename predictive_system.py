# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:15:27 2024

@author: yash
"""
import numpy as np
import pickle
loaded_model = pickle.load(open('C:/Users/yash/Documents/Deployment/malaria/trained_model.sav', 'rb'))
input_data=data_tuple = (1, 4, 274, 1, 1, 12,38.0, 126080.0, 5.7, 2.80, 5.8, 16.1, 59.0, 21.1, 36.0, 156.0, 8.2, 6.8, 61.8, 31.7, 6.5, 3.6, 1.8, 0.3, 19.0)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = np.array(input_data_as_numpy_array).reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if prediction[0]==0:
    
    
     print("non -malaria Infection")
elif prediction[0]==1:
     print("uncomplicated malaria")
elif prediction[0]==2:
     print("Severe malaria")