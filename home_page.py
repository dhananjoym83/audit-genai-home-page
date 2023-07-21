import streamlit as st 
import base64
import webbrowser
from PIL import Image 

 
# Set page title  
st.set_page_config(page_title="Hackathon3 Home", page_icon=":search:", layout="wide") 
  
# Define button labels and URLs  
buttons = {  
    "PCAOB Semantic Search": "https://nprd-pr-genaivang-app-svc-aht3-linux.azurewebsites.net/", 
    "Digital Coach": "https://nprd-pr-genaivang-app-svc-aht3-linux2.azurewebsites.net/",   
    "Understanding the Entity": "https://nprd-pr-genaivang-app-svc-aht3-linux5.azurewebsites.net/", 
    "Benchmarking Financial Statements": "https://nprd-pr-genaivang-app-svc-aht3-linux3.azurewebsites.net/",  
    "Flowchart and Narrative Generation": "https://nprd-pr-genaivang-app-svc-aht3-linux7.azurewebsites.net/",
    "Lead sheets and Testing": "https://nprd-pr-genaivang-app-svc-aht3-linux4.azurewebsites.net/", 
    "Planning Analytics": "https://nprd-pr-genaivang-app-svc-aht3-linux8.azurewebsites.net/",  
    "Going Concern Analysis": "https://nprd-pr-genaivang-app-svc-aht3-linux6.azurewebsites.net/",  
}  
  
# Define page layout  
def app(): 
    col4, col5 = st.columns([1,20])
    with col4:
        image = Image.open('kpmg-logo.webp')
        st.image(image, width=130)
    with col5: 
        st.write("<br>", unsafe_allow_html=True) 
        st.write("<h2 style='text-align: center;'>Welcome to Audit Garage AI Platform</h2>", unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)  
        st.write("<br>", unsafe_allow_html=True)  
        st.write("<h5 style='text-align: center;'>Choose a Use Case to get started</h5>", unsafe_allow_html=True)  
    st.write("<br>", unsafe_allow_html=True)
     
    #col1, col2, col3 = st.columns(3) 
    col1, col2, col3 = st.columns(3) 
    
    for i, (label, url) in enumerate(buttons.items()):  
        if i < 3:
            with col1:
                if st.button(label, key=label):
                    webbrowser.open_new_tab(url)  
        elif i < 6:  
            with col2:
                if st.button(label, key=label):
                    webbrowser.open_new_tab(url)
        else:
            with col3:
                if st.button(label, key=label):
                    webbrowser.open_new_tab(url)  

# Run Streamlit app  
if __name__ == "__main__":  
    app()  
