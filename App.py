import streamlit as st
from db_fxns import * 
import pandas as pd

import plotly.express as px 
import webbrowser

import requests
from streamlit_lottie import st_lottie

from pages import Admin, User, Home
import pyautogui

st.set_page_config(
    
    page_title="Team Alfredo",
    page_icon="images (2).jpeg",
    layout="wide",
)
st.markdown('<style>body{text-align: center;}</style>', unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
    

    
def main():

    #Home.Home_page()
    
    #lottie_login=load_lottie("https://assets7.lottiefiles.com/private_files/lf30_zh2jz2uz.json")
    #st_lottie(lottie_login,height=300, key="Imagera")
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    #status=Admin.logout()
    #st.write(Admin.logout())
    logform=st.sidebar.form("loginformsidebar",clear_on_submit=True)
    username=logform.text_input("Username :")
    password=logform.text_input("Password :",type = 'password')
    loginjud=logform.form_submit_button("🗝️    Log in")
    
    #Admin.callback()
    if "Load_state" not in st.session_state:
            st.session_state.Load_state=False
            Home.Home_page()
            
    if loginjud or st.session_state.Load_state:
        st.session_state.Load_state=True
        create_table()
        result = login_user(username,password)
        if username == 'Admin' and password == 'admin':
            
            page = Admin
            page.Admin()
                
        elif result:
            
            new_ActiveStatus='Online'
            active_status(new_ActiveStatus,"Offline",username)
            page = User
            page.User(username)
                    
                   
        else:
            st.sidebar.error("Username or Password is incorrect!")
            Home.Home_page()
    #elif 
    
    
    
    
    
    
    
  
if __name__ == '__main__':
	main()






    
