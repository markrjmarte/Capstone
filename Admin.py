import streamlit as st
from db_fxns import * 
import pandas as pd
#import streamlit.components.v1 as stc
import pyautogui

import plotly.express as px 
import webbrowser

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



def Admin():
    
    
    lottie_admin=load_lottie("https://assets3.lottiefiles.com/packages/lf20_cyvxw69x.json")
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
          <h2>Adminstrator Interface</h2>
        </div>
      </div>
    </div>
 </body>""", unsafe_allow_html=True)
 
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
                        <p class="a">{'Adminstrator'}</p>
                        """
                st.markdown(html_pre,unsafe_allow_html=True)
            
            menu = ["🎓 Student List","📭 Submitted Counselling form", "📧 Open Mail","❌ Log Out"]
            choice1 = st.selectbox("",menu)
            if choice1 == "📭 Submitted Counselling form":
                st.text('')
                st.text('Note:')
                st.markdown(
                "90% of people love to enjoy music, while they are working! \n"
                "are you one of them, we have a curated list of chillout tracks \n"
                "that may help you bring out the calmness in you."
                )
            elif choice1 == "📧 Open Mail":
                st.text('')
                st.text('Note:')
                st.markdown(
                "Mail is open now. at the next tab! \n"
                "are you one of them, we have a curated list of chillout tracks \n"
                "that may help you bring out the calmness in you."
                )
            elif choice1 == "🎓 Student List":
                st.text('')
                st.text('Note:')
                st.markdown(
                "90% of people love to enjoy music, while they are working! \n"
                "are you one of them, we have a curated list of chillout tracks \n"
                "that may help you bring out the calmness in you."
                )
            elif choice1 == "Dashboard": 
                st.text('')
                st.text('Note:')
                st.markdown(
                "90% of people love to enjoy music, while they are working! \n"
                "are you one of them, we have a curated list of chillout tracks \n"
                "that may help you bring out the calmness in you."
                )
                
        with col2:
            st_lottie(lottie_admin,height=300, key="Imagera")
        st.write('---')    
        
    
    if choice1 == "🎓 Student List":
    
        st.write("")
        st.subheader("Student List ")
        st.write("")
        result = view_all_data()
        clean_df = pd.DataFrame(result,columns=["Id Number" ,"First Name" ,"Middle Name" ,"Last Name" ,"Year" ,"Course" ,"Gender" ,"Address" ,"Birth Date" ,"Birth Place","Religion" ,"Contact Number" ,"Civil Status" ,"Email Account"])
        st.dataframe(clean_df)
        Studentlist = ["🟢 Active User","📊 Chart","➕ Add","📅 Update","⛔ Delete"]
        choice = st.selectbox("",Studentlist)
        create_table()
        if choice == "➕ Add":
            with st.form(key= 'Adddata', clear_on_submit=True):
                col1,col2,col3 = st.columns(3)
                with col1:
                    Fname = st.text_input("First Name",key='1')
                    AcYear = st.selectbox("Year",["1","2","2","4"])
                    bdate = st.date_input("Birth Date")
                    Cnumber = st.text_input("Contact Number",key='2')
                       
                        

                with col2:
                    Mname = st.text_input("Midle Name",key='3')
                    Course = st.selectbox("Course",["Bs Info-Tech Net.","Bs Info-Tech Prog.","BS kukunat","4"])
                    Id = st.text_input("Id Number",key='4')
                    bplace = st.text_input("Birth Place",key='5')
                    CStatus = st.selectbox("Civil Status",["Single","Maried","Wedow"])
                        
                        
                        
                with col3:
                    Lname = st.text_input("Last Name",key='6')
                    Gender = st.selectbox("Gender",["Male","Female"])
                    Address = st.text_input("Address",key='7')
                    Religion = st.text_input("Religion",key='8')
                    Eacc = st.text_input("Email Account","@gmail.com",key='9')
                    st.write("")
                AddtoList = st.form_submit_button('Add Data')
               
            if AddtoList : 
                #if (Id == " " or Fname ==" " or Mname=="" or Lname=="" or AcYear=="" or Course=="" or Gender==""or Address=="" or bdate == "" or bplace = "" or Religion=="" or Cnumber=="" or CStatus=="" or Eacc ==""):
                st.warning("Please make your fill in all information ask for!")
                #else:
                ActiveStatus='Offline'
                message="None"
                response="None"
                res_status = "Not ok"
                add_data(Id,Fname ,Mname ,Lname ,AcYear ,Course ,Gender ,Address ,bdate ,bplace,Religion ,Cnumber ,CStatus ,Eacc,ActiveStatus,message,response,res_status)
                st.success("Data Has been Added! Press R to Refresh data list")
                 
        elif choice == "📊 Chart":

            with st.expander("Course Based Chart"):
                Data_frame = clean_df['Course'].value_counts().to_frame()
                Data_frame = Data_frame.reset_index()
                p1 = px.pie(Data_frame,names='index',values='Course')
                st.plotly_chart(p1,use_container_width=True)
                
            with st.expander("Year Based Chart"):
                Data_frame1 = clean_df['Year'].value_counts().to_frame()
                st.bar_chart(Data_frame1)

        elif choice == "📅 Update":
        
            
            list_of_Lname = [i[0] for i in view_all_StudentId()]
            selected_Id = st.selectbox("Select Id Number :",list_of_Lname)
            Id_result = get_Id(selected_Id)
                
                
            if Id_result:
           
                Id = Id_result[0][0]
                Fname = Id_result[0][1]
                Mname = Id_result[0][2]
                Lname = Id_result[0][3]
                AcYear = Id_result[0][4]
                Course = Id_result[0][5]
                Gender = Id_result[0][6]
                Address = Id_result[0][7]
                bdate = Id_result[0][8]
                bplace = Id_result[0][9]
                Religion = Id_result[0][10]
                Cnumber = Id_result[0][11]
                CStatus = Id_result[0][12]
                Eacc  = Id_result[0][13]
                
            with st.form(key= 'Updatedata', clear_on_submit=True):   
                col1,col2,col3 = st.columns(3)
                with col1:
                    new_Fname = st.text_input("First Name",Fname,key='1')
                    new_AcYear = st.selectbox("Year",["1","2","2","4"])
                    new_bdate = st.date_input(bdate)
                    new_Cnumber = st.text_input("Contact Number",Cnumber,key='2')
                with col2:
                    new_Mname = st.text_input("Midle Name",Mname,key='3')
                    new_Course = st.selectbox("Course",["Bs Info-Tech Net.","Bs Info-Tech Prog.","BS kukunat","4"])
                    new_Id = st.text_input("Id Number",Id,key='4')
                    new_bplace = st.text_input("Birth Place",bplace,key='5')
                    new_CStatus = st.selectbox("Civil Status",["Single","Maried","Wedow"])
                with col3:
                    new_Lname = st.text_input("Last Name",Lname,key='6')
                    new_Gender = st.selectbox("Gender",["Male","Female"])
                    new_Address = st.text_input("Address",Address,key='7')
                    new_Religion = st.text_input("Religion",Religion,key='8')
                    new_Eacc = st.text_input(Eacc,"@gmail.com",key='9')
                    st.write("")
                UpdateList= st.form_submit_button("Update Data")
                
            if UpdateList:
                edit_Fname_data(new_Id ,new_Fname,new_Mname,new_Lname,new_AcYear ,new_Course ,new_Gender ,new_Address ,new_bdate ,new_bplace,new_Religion ,new_Cnumber ,new_CStatus ,new_Eacc,Id ,Fname ,Mname ,Lname ,AcYear ,Course ,Gender ,Address ,bdate ,bplace,Religion ,Cnumber ,CStatus ,Eacc )
                st.success("Data Has been Updated! Press R to Refresh data list")
                

        elif choice == "⛔ Delete":
        
            unique_list = [i[0] for i in view_all_StudentId()]
            delete_id =  st.selectbox("Selected Id :",unique_list)
            
            result = view_datattodelete(delete_id)
            st.write("")
            clean_df = pd.DataFrame(result,columns=["Id Number","First Name" ,"Midle Name" ,"Last Name" ,"Year" ,"Course" ,"Gender" ,"Address" ,"Birth Date" ,"Birth Place","Religion" ,"Contact Number" ,"Civil Status" ,"Email Acc", "Active Status"])
            st.dataframe(clean_df)
            st.write("")
            
            if st.button("Delete Data form The List"):
                delete_data(delete_id)
                st.success("Data Has been Deleted! Press R to Refresh data list")
        
        elif choice == "🟢 Active User":
        
            #unique_list = [i[0] for i in view_all_StudentId()]
            #actstate = "Online"
            result = onlinestatus()
            clean_df = pd.DataFrame(result,columns=["Active Status","Id Number","First Name" ,"Midle Name" ,"Last Name" ,"Year" ,"Course",])
            st.dataframe(clean_df)
            #result = view_all_login("Offline",Id,Fname ,Mname ,Lname ,AcYear ,Course)
            #clean_df = pd.DataFrame(result,columns=["Active Status","Id Number","First Name" ,"Midle Name" ,"Last Name" ,"Year" ,"Course",])
            #st.dataframe(clean_df)
        else:
            st.subheader("Option is out of bound")
          
    elif choice1 == "📭 Submitted Counselling form":
        
        #result_rr = response_status()
        #clean_df = pd.DataFrame(result_rr,columns=["Id Number","First Name" ,"Midle Name" ,"Last Name" ,"Year" ,"Course" ,"Message","response"])
        #st.dataframe(clean_df)
        
       
        r_list = [i[0] for i in response_status()]
        r_id =  st.selectbox("Students with quieres :",r_list)
            
        result_r = get_Id(r_id)
        #placeholder = st.empty()
        #placeholder2 = st.empty()
        
        if result_r:
            Id = result_r[0][0]
            Fname = result_r[0][1]
            Mname = result_r[0][2]
            Lname = result_r[0][3]
            AcYear = result_r[0][4]
            Course = result_r[0][5]
            message = result_r[0][15]
            response = result_r[0][16]
       
        if r_id:
            with st.form(key= 'Adddrespo', clear_on_submit=True):
                col1, col2 ,col3= st.columns( [0.1, 0.8, 0.1])
                with col1:
                    st.text("")
                with col2:
                    st.text("")
                    st.text("")
                    htmlmss = f"""
                        <style>
                        p.w{{
                            padding: 0px 0;
                            font: 12px Arial;
                            text-align: left;
                            color: #FF4B4B;
                        }}
                        </style>
                        <p class="w">From Student:</p>
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
                            <p class="e">Admin Responsed</p>
                        """
                        st.markdown(htmlmsss,unsafe_allow_html=True)
                        st.warning(response)
                    new_res=st.text_area("")   
                    st.text("")
                    send = st.form_submit_button("✉️ Send")
                    st.text("")
                with col3:
                    st.text("")
            if send:
                update_convo_r(new_res,Id,response)
                st.info("Message has been sent, to see the changes please press R if you use Personal Computer for the user you can refresh it at menu bar and clink rerun")
                new_rStatus='Ok'
                response_status_change(new_rStatus,"Not ok",Id)
            
        
    elif choice1 == "📧 Open Mail":
        url = 'http://www.gmail.com'
        webbrowser.open_new_tab(url)
        htmlmss1 = f"""
            <style>
            p.e{{
            padding: 3px 0;
            font: 18px Arial;
            text-align: center;
            color: #FF4B4B;
            }}
            </style>
            <p class="e">Mail is open now at the next tab!</p>
            """
        st.markdown(htmlmss1,unsafe_allow_html=True)
        lottie_admin=load_lottie("https://assets1.lottiefiles.com/packages/lf20_78obvmke.json")
        st_lottie(lottie_admin,height=350, key="222")
    elif choice1 == "❌ Log Out":
        pyautogui.hotkey("ctrl","F5")

