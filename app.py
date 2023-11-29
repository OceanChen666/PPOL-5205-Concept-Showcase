import streamlit as st
from multiapp import MultiApp
from apps import conclusion, home,data,cluster,kmeans,ahc,dbscan

st.set_page_config(
     page_title='Tutorial of Cluster Analysis -Offshore Oil Platform Use case',
     layout="wide",
     initial_sidebar_state="expanded",
)

st.sidebar.markdown('''
# About this page
''')

st.sidebar.info("This is a tutorial on how to choose the best parameter in cluster analysis based on the Offshore oil platform in the U.S.  You can find all the corresponding code in this [GitHub]() repo.\n\n Created by [Ocean Chen]")



app = MultiApp()

app.add_app("Home",home.app)
app.add_app("Cluster",cluster.app)
app.add_app("Data",data.app)
app.add_app("K-means",kmeans.app)
app.add_app("AHC",ahc.app)
app.add_app("DBSCAN",dbscan.app)
app.add_app("Conclusion",conclusion.app)
# The main app
app.run()

