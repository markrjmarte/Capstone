import streamlit as st

 
 
def Home_page():
    st.empty()
    with open('style/style3.css') as f:
            st.markdown(f"""<style>{f.read()}</style>
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
          <h1><a href="index.html">E-Guidance<span class="logo_colour"> Consultation App</span></a></h1>
          <h2>Made by Team Alfredo The Greate</h2>
        </div>
      </div>
    </div>
    <div id="site_content">
      <div class="sidebar">
        <!-- insert your sidebar items here -->
        <h3>Team Alfredo</h3>
        <p>Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth</p>
        <p></p>
        <p>Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth</p>
        <h3>Ambut unsa i butang ninyu</h3>
        <p>Alfredo@gmail.com<br /></p>
        <h3>Contact us:</h3>
        <p>Alfredo@gmail.com<br /></p>
      </div>
      <div id="content">
        <!-- insert the page content here -->
        <h1>What is E-GCA ?</h1>
        <p>Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earthAko ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earthAko ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth</p>
        <p>Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earthAko ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earthAko ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth</p>
        <p>Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earthAko ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earthAko ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth Ako ang pina ka gwapo sa earth</p>
        <p>This Web application is made with <strong>STREAMLIT</strong>, <strong>PHYTON</strong>, <strong>HTML</strong> and <strong>CSS</strong>, and can be deploy using streamlit cloud.</p>
        <h2>Sending Quiries Capability</h2>
        <p>The user can send quiries while using the app by google account.</p>
      </div>
    </div>
</body>""", unsafe_allow_html=True)
    
    
   

   