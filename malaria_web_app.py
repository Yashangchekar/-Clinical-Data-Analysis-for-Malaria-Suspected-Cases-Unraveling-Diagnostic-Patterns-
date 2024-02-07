# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:17:53 2024

@author: yash
"""

import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('C:/Users/yash/Documents/Deployment/malaria/trained_model.sav','rb')) #rb read the binary format

#create function for prediction
def malaria_prediction(input_data):
    
    #changing the input_data to numpy array
    input_data_as_numpy_array=np.asarray(input_data,dtype=object)

    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    #standardize the input data
    #std_data=ss.transform(input_data_reshaped)
    #print(std_data)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0]==0:
        return "non -malaria Infection"
    elif prediction[0]==1:
        return "uncomplicated malaria"
    elif prediction[0]==2:
        return "Severe malaria"
        
        
def main():
    #giving a atitle
    st.title("Malaria Prediction web App")
    #fever_symptom 	Suspected_Organism 	Suspected_infection 	RDT 	Microscopy 	Laboratory_Results 	Clinical_Diagnosis 	temperature 	parasite_density 	wbc_count 	rbc_count 	hb_level 	hematocrit 	mean_cell_volume 	mean_corp_hb 	mean_cell_hb_conc 	platelet_count 	platelet_distr_width 	mean_platelet_vl 	neutrophils_percent 	lymphocytes_percent 	mixed_cells_percent 	neutrophils_count 	lymphocytes_count 	mixed_cells_count 	RBC_dist_width_Percent
    fever_symptom=st.text_input("fever symptoms")
    Suspected_Organism=st.text_input("suspected input")
    Suspected_infection=st.text_input("si")
    RDT=st.text_input("RDT Negative 0 and positive 1")
    Microscopy=st.text_input("Microscopy Negative 0 and positive 1")
    Laboratory_Results=st.text_input("Lab results")
    #Clinical_Diagnosis=st.text_input("Clincial Diganosis")
    temperature=st.text_input("temprature")
    parasite_density=st.text_input("parasite")
    rbc_count=st.text_input("rbc count")  
    wbc_count=st.text_input("wbc count") 
    hb_level = st.text_input("Enter Hemoglobin Level:")
    hematocrit = st.text_input("Enter Hematocrit:")
    mean_cell_volume = st.text_input("Enter Mean Cell Volume:")
    mean_corp_hb = st.text_input("Enter Mean Corpuscular Hemoglobin:")
    mean_cell_hb_conc = st.text_input("Enter Mean Cell Hemoglobin Concentration:")
    platelet_count = st.text_input("Enter Platelet Count:")
    platelet_distr_width = st.text_input("Enter Platelet Distribution Width:")
    mean_platelet_vl = st.text_input("Enter Mean Platelet Volume:")
    neutrophils_percent = st.text_input("Enter Neutrophils Percentage:")
    lymphocytes_percent = st.text_input("Enter Lymphocytes Percentage:")
    mixed_cells_percent = st.text_input("Enter Mixed Cells Percentage:")
    neutrophils_count = st.text_input("Enter Neutrophils Count:")
    lymphocytes_count = st.text_input("Enter Lymphocytes Count:")
    mixed_cells_count = st.text_input("Enter Mixed Cells Count:")
    RBC_dist_width_Percent=st.text_input("enter Rbc width percent")
    #code for prediction
    diagnosis=''
    #creating  a button for prediction
    if st.button("malaria test result"):
        diagnosis=malaria_prediction([fever_symptom, 	Suspected_Organism, 	Suspected_infection, 	RDT ,	Microscopy, 	Laboratory_Results,  temperature ,	parasite_density, 	rbc_count ,wbc_count 	,hb_level 	,hematocrit, 	mean_cell_volume ,	mean_corp_hb ,	mean_cell_hb_conc, 	platelet_count ,	platelet_distr_width 	,mean_platelet_vl ,	neutrophils_percent ,	lymphocytes_percent ,	mixed_cells_percent ,	neutrophils_count ,	lymphocytes_count ,	mixed_cells_count ,	RBC_dist_width_Percent])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
    
    