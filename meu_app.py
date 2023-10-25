import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="Github Search")
st.title('Github Search')

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
    username = st.text_input('Insira o Username')

    if st.button('Buscar'):
        infoUsuario = selecionarUsuario(username)
        if infoUsuario is not None:
            st.markdown(f'''
            <div class="container">
                <div class="row">
                    <div class="col-md-4">
                        <img src="{infoUsuario['avatar_url']}" class="rounded-circle" width="140" height="140">
                    </div>
                    <div class="col-md-8">
                        <h2>{infoUsuario['name']}</h2>
                        <p>{infoUsuario['bio']}</p>
                        <a href="{infoUsuario['html_url']}" style="color: white; text-decoration: none" class="btn btn-primary">Ir para Github</a>
                        <a href="{infoUsuario['url']}" style="color: white; text-decoration: none" class="btn btn-primary">Ir para API</a>
                    </div>
                </div>
            </div>
             ''', unsafe_allow_html=True)


ui()