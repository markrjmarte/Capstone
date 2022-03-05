
import streamlit as st
from db_fxns import * 
import pandas as pd 
#import streamlit.components.v1 as stc

import plotly.express as px  
import webbrowser
import pyautogui

import requests
from streamlit_lottie import st_lottie

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
    

def User(Username):

    
    
    lottie_picture=load_lottie("https://assets6.lottiefiles.com/packages/lf20_YPllbK.json")
    with open('style/style3.css') as f:
        st.markdown(f"""<style>{f.read()}</style><head>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=windows-1252" />
  <link rel="stylesheet" type="text/css" href="style/style.css" title="style" />
</head>
<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <div id="logo_text">
          <!-- class="logo_colour", allows you to change the colour of the text -->
          <h1><a href="index.html">E-Guidance<span class="logo_colour">Consultation App</span></a></h1>
          <h2>User Interface</h2>
        </div>
      </div>
    </div>
 </body>""", unsafe_allow_html=True)
 
    userlog= get_Id(Username)
    
    if  userlog:
           
        Id =  userlog[0][0]
        Fname =  userlog[0][1]
        Mname =  userlog[0][2]
        Lname =  userlog[0][3]
        AcYear =  userlog[0][4]
        Course =  userlog[0][5]
        Gender =  userlog[0][6]
        Address =  userlog[0][7]
        bdate =  userlog[0][8]
        bplace =  userlog[0][9]
        Religion =  userlog[0][10]
        Cnumber =  userlog[0][11]
        CStatus =  userlog[0][12]
        Eacc  =  userlog[0][13]
        ActiveStatus =userlog[0][14]
    
    a = f'{ActiveStatus}'
    b = f'{Id}'
    c = f'{Fname}'
    d = f'{Mname}'
    e = f'{Lname}'            
    f = f'{AcYear}'
    g= f'{Course}'
    h= f'{Gender}'
    i= f'{Address}'
    j= f'{bdate}'
    k= f'{bplace}'
    l= f'{Religion}'
    m= f'{Cnumber}'
    n= f'{CStatus}'
    o= f'{Eacc}'
    
    with st.container():
        st.write('---')   
        col1, col2 = st.columns(2)
        with col1:
            with st.container():
                html_pre = f"""
                        <style>
                        p.a{{
                            padding: 20px 0 0 0;
                            font: 30px Arial;
                            text-align: center;
                            color: #c3c3c3;
                        }}
                        </style>
                        <p class="a">{c+' '+ e}</p>
                        """
                st.markdown(html_pre,unsafe_allow_html=True)
            
            menu = ["💁‍♂️ View Profile","📥 Consultation (Default)","📩 Consultation (Email)","❌ Log Out"]
            choice1 = st.selectbox("",menu)
            if choice1 == "💁‍♂️ View Profile":
                st.text('')
                st.text('Note:')
                st.markdown(
                "90% of people love to enjoy music, while they are working! \n"
                "are you one of them, we have a curated list of chillout tracks \n"
                "that may help you bring out the calmness in you."
                )
            elif choice1 == "📥 Consultation (Default)":
                st.text('')
                st.text('Note:')
                st.markdown(
                "90% of people love to enjoy music, while they are working! \n"
                "are you one of them, we have a curated list of chillout tracks \n"
                "that may help you bring out the calmness in you."
                )
            elif choice1 == "📩 Consultation (Email)": 
                st.text('')
                st.text('Note:')
                st.markdown(
                "90% of people love to enjoy music, while they are working! \n"
                "are you one of them, we have a curated list of chillout tracks \n"
                "that may help you bring out the calmness in you."
                )
            
                
        with col2:
            st_lottie(lottie_picture,height=300, key="Imagera")
            #st.text("")
        st.write('---')   
    #pass1 = Password
    if choice1 == "💁‍♂️ View Profile":
        #st.write("")
        #st.subheader("Profile ")
        #st.write("")
        st.markdown(f"""
                <style>
                    #site_content{{
                        width: 100%;
                        overflow: hidden;
                        background-color: #fff;
                        border-radius:20px;
                    }}
                    .tit p{{
                        padding: 60px 0 0 15px;
                        text-align: center;
                        color: #21447B;
                        text-decoration: none;
                        font: normal 250% arial, sans-serif;
                    }}
                    .sidebar{{
                        float: right;
                        text-align: center;
                        width: 100%;
                        padding: 0px 16px;
                        width: 50%;
                    }}
                    .sidebar p {{ 
                        display: block;
                        color: Black;
                        text-align: center;
                        padding: 5px 40px;
                        font-size: 19px;
                        background-color: #5eafd4;
                    }}
                    .sidebar h1{{
                        color: #262730; 
                        font: normal 140% arial, sans-serif; 
                        text-align: center; 
                        padding: 30px 0 5px 0;
                    }}
                    #content{{
                        text-align: center;
                        width: 100%;
                        padding: 0px 16px;
                        width: 50%;
                    }}
                    .Paragraph h1{{
                        color: #262730; 
                        font: normal 140% arial, sans-serif; 
                        text-align: center; 
                        padding: 30px 0 5px 0;
                    }}
                    .Paragraph {{
                        overflow: hidden;
                    }}
                    .Paragraph p {{
                        display: block;
                        color: Black;
                        text-align: center;
                        padding: 5px 40px;
                        font-size: 19px;
                        background-color: #5eafd4;
                    }}
                </style>
                <body>
                    <div class = tit>
                       <p>Information</p> 
                    </div>
                    <div id="site_content">
                        <div class="sidebar">
                                <h1>Address:</h1>
                                <a><p>{i}</p>
                                <h1>Birth Date:</h1>
                                <p>{j}</p>
                                <h1>Birth Place:</h1>
                                <p>{k}</p>
                                <h1>Religion:</h1>
                                <p>{l}</p>
                                <h1>Contact Number:</h1>
                                <p>{m}</p>
                                <h1>Civil status:</h1>
                                <p>{n}</p>
                                <h1>Email Account:</h1>
                                <p>{o}</p>
                        </div>
                        <div id="content">
                            <div class="Paragraph">
                                <h1>Id Number:</h1>
                                <p>{b}</p>
                                <h1>First Name:</h1>
                                <p>{c}</p> 
                                <h1>Middle Name:</h1>
                                <p>{d}</p>
                                <h1>Last Name:</h1>
                                <p>{e}</p>
                                <h1>Year:</h1>
                                <p>{f}</p>
                                <h1>Course:</h1>
                                <p>{g}</p>
                                <h1>Gender:</h1>
                                <p>{h}</p>
                </body>
        """,unsafe_allow_html=True)
    
    elif choice1 == "📥 Consultation (Default)":
        
        
        #post = convo_save()
        #clean_df = pd.DataFrame(post,columns=["Id","Fname","Mname" ,"Lname" ,"AcYear" ,"Course","Message","Response"])
        #st.dataframe(clean_df)
        
        
        user_m= get_Id(Username)
        if user_m:
            Id =  user_m[0][0]
            Fname =  user_m[0][1]
            Mname =  user_m[0][2]
            Lname =  user_m[0][3]
            AcYear =  user_m[0][4]
            Course = user_m[0][5]
            message = user_m[0][15]
            response = user_m[0][16]
        with st.form(key= 'Adddata', clear_on_submit=True):
            col1, col2 ,col3= st.columns( [0.1, 0.8, 0.1])
            with col1:
                st.text("")
            with col2:
                st.text("")
                st.text("")
                if message =="None":
                    lottie_picture=load_lottie("https://assets2.lottiefiles.com/packages/lf20_ucns0iaz.json")
                    st_lottie(lottie_picture, height=200, key="I")
                    htmlmsss = f"""
                    <style>
                    p.ww{{
                        padding: 0px 0;
                        font: 15px Arial;
                        text-align: center;
                        color: #FF4B4B;
                    }}
                    </style>
                    <p class="ww">Contact us by sending message below!</p>
                    """
                    st.markdown(htmlmsss,unsafe_allow_html=True)
                else:
                    htmlmss = f"""
                    <style>
                    p.w{{
                        padding: 0px 0;
                        font: 12px Arial;
                        text-align: left;
                        color: #FF4B4B;
                    }}
                    </style>
                    <p class="w">Your message</p>
                    """
                    st.markdown(htmlmss,unsafe_allow_html=True)
                    st.warning(message)
                if response == "None":
                    st.text("")
                else:
                    htmlmsss = f"""
                        <style>
                        p.e{{
                        padding: 3px 0;
                        font: 12px Arial;
                        text-align: right;
                        color: #FF4B4B;
                        }}
                        </style>
                        <p class="e">Administrator</p>
                    """
                    st.markdown(htmlmsss,unsafe_allow_html=True)
                    st.warning(response)
                new_message=st.text_area("")
                st.text("")
                send = st.form_submit_button("✉️ Send")
                st.text("")
            with col3:
                st.text("")
        if send:
            view_update_convo(new_message,Username,message)
            update_convo_r("None",Username,response)
            new_rStatus='Not ok'
            response_status_change(new_rStatus,"Ok",Username)
            st.info("Message has been sent, to see the changes please press R")
        
        
     
    elif choice1 == "📩 Consultation (Email)":
        col1, col2 = st.columns(2)
        with col1:
            lottie_picture=load_lottie("https://assets10.lottiefiles.com/packages/lf20_cmdbxiek.json")
            st_lottie(lottie_picture,height=400, key="I")
        with col2:
            st.write("")
            st.subheader(":mailbox: Send your inquiry!")
            contact_form = f"""
            <form action = "https://formsubmit.co/blackaesthetic09@gmail.com" method = "POST">
                <input type= "hidden" name="_captcha" value="false">
                <input type="hidden" name="_template" value="table">
                <input type="text" name="name" placeholder="Your email" required>
                <input type = "email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder ="Your message here"></textarea>
                <button type = "submit">Send</button>
           </form>
            """
            st.markdown(contact_form,unsafe_allow_html=True)
            local_css("style/style.css")
            pyautogui.hotkey("R")
        st.write('---')   
                
    
        
    elif choice1 == "❌ Log Out":
        new_ActiveStatus='Offline'
        active_status(new_ActiveStatus,"Online",Username)
        pyautogui.hotkey("ctrl","F5")
       
    
    
    
    
    
    
    
        
  