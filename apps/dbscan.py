import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import DBSCAN



def build_model(df,for_cluster,eps_set,min_samples_set):


    db = DBSCAN(eps=eps_set, min_samples=min_samples_set).fit(for_cluster)
    df["dbscan_label"] = db.labels_
    df2 = for_cluster.copy()
    df2["dbscan_label"] = db.labels_

    df["dbscan_label"] = df["dbscan_label"].astype(str)
    df2["dbscan_label"] = df2["dbscan_label"].astype(str)
    # df["dbscan_label"] = df["dbscan_label"].astype(str)

    fig = px.scatter_geo(df, 
                     lat='LATITUDE', 
                     lon='LONGITUDE',  
                           color="dbscan_label", 
                        # size="car_hours",
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
                color = "dbscan_label")
    st.plotly_chart(fig2)
    

def app():
    st.markdown(
        """
# DBSCAN
""")
    
    df = pd.read_csv("Data/Plot_data.csv")
    for_cluster = pd.read_csv("Data/after_PCA.csv")

    df = df.drop(columns = ["Unnamed: 0"])
    for_cluster = for_cluster.drop(columns = ["Unnamed: 0"])

    eps_set = st.sidebar.slider("Epsilon",
                                min_value=0.1, max_value=0.8, 
                                value=0.5,  step=0.1)
    min_samples_set = st.sidebar.slider("Min Samples",
                                min_value=10, max_value=20, 
                                value=10,  step=1)
    
    st.write("DBSCAN is an extremely powerful clustering algorithm. The acronym stands for Density-based Spatial Clustering of Applications with Noise. As the name suggests, the algorithm uses density to gather points in space to form clusters. The algorithm can be very fast once it is properly implemented. However, in this article, we would rather be talking about tuning the parameters of DBSCAN for a better utility than the algorithm implementation itself. (Implementation of DBSCAN is very simple. The harder part, if any, would be structuring data for neighbourhood lookups.)")

    st.subheader("Epsilon parameter of DBSCAN")
    st.write("The most important parameter of DBSCAN can be identified as eps. It is the furthest distance at which a point will pick its neighbours. Therefore, intuitively this will decide how many neighbours a point will discover.")
    if st.sidebar.button('Press to use Example Dataset'):
        st.sidebar.markdown('The **Parameter** set is updated.')

        build_model(df,for_cluster,eps_set,min_samples_set)
    
   

