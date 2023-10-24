import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="Meu Site com API")

base_url = 'https://api.github.com'

response = requests.get(url)

st.subheader("Algo com API nesse site test")
st.title("Dados de alguma aqui aqui")

def selecionarUsuario(username):
    url = f'{base_url}/users/{username}'
    response = requests.get(url)
    
    return response.json()  
