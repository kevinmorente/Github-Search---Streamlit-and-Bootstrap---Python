import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="Meu Site com API")

base_url = 'https://api.github.com'

def selecionarUsuario(username):
    url = f'{base_url}/users/{username}'
    response = requests.get(url)
    if response.status_code==200:
        return response.json()
    else:
        return None
    
def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)
    st.title('Github Users')