import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import AgglomerativeClustering

def app():
    st.markdown(
        """
# AHC
""")
    df = pd.read_csv("Data/Plot_data.csv")
    for_cluster = pd.read_csv("Data/after_PCA.csv")

    df = df.drop(columns = ["Unnamed: 0"])
    for_cluster = for_cluster.drop(columns = ["Unnamed: 0"])
    
    options = ['ward', 'complete', 'average', 'single']
    linkage_set = st.sidebar.selectbox(
    "Choose an linkage method:",
    options
    )

    st.markdown("""
Hierarchical clustering algorithms group similar objects into groups called clusters. There are two types of hierarchical clustering algorithms:

- Agglomerative — Bottom up approach. Start with many small clusters and merge them together to create bigger clusters.
- Divisive — Top down approach. Start with a single cluster than break it up into smaller clusters.
                """)
    
    st.subheader("Linkage Method")
    st.image("Images/ahc1.png")
    
    if st.sidebar.button('Press to use Update Parameter'):
        st.sidebar.markdown('The **Parameter** set is updated.')

        build_model(df,for_cluster,linkage_set)

    
   
def build_model(df,for_cluster,linkage_set):

    ahc = AgglomerativeClustering(linkage=linkage_set).fit(for_cluster)
    df["ahc_label"] = ahc.labels_
    df2 = for_cluster.copy()
    df2["ahc_label"] = ahc.labels_
    df["ahc_label"] = df["ahc_label"].astype(str)
    df2["ahc_label"] = df2["ahc_label"].astype(str)

    fig = px.scatter_geo(df, 
                     lat='LATITUDE', 
                     lon='LONGITUDE',  
                           color="ahc_label", 
                        # size="car_hours",
                        color_discrete_sequence=px.colors.qualitative.G10,
                  hover_name="OPERNAME")
# Set Size of Dots
    fig.update_traces(marker=dict(size=2.5))
# Layout
    fig.update_geos(
    visible=False, # hides default base map
    showcountries=True, 
    lonaxis_range=[-98, -84],  # longitude range
    lataxis_range=[26, 30],    # latitude range
)
    fig.update_layout(
        title = 'Aged US offshore platform',
        geo=dict(
        scope='north america',
        showland=True,
        landcolor="rgb(212, 212, 212)",
        countrycolor="rgb(255, 255, 255)"
    )
      #   geo_scope='usa',
    )
    st.plotly_chart(fig)

    fig2 = px.scatter(df2,x="PC1",y= "PC2",
                color = "ahc_label",
                color_discrete_sequence=px.colors.qualitative.G10)
    st.plotly_chart(fig2)