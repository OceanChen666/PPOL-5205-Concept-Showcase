import streamlit as st
import plotly.express as px
import pandas as pd
from sklearn.cluster import KMeans

def build_model(df,for_cluster,n_cluster_set):

    km = KMeans(n_clusters=n_cluster_set, init='k-means++', 
                random_state=0).fit(for_cluster)
    df["kmeans_label"] = km.labels_
    df2 = for_cluster.copy()
    df2["kmeans_label"] = km.labels_

    df["kmeans_label"] = df["kmeans_label"].astype(str)
    df2["kmeans_label"] = df2["kmeans_label"].astype(str)
    # df["dbscan_label"] = df["dbscan_label"].astype(str)

    fig = px.scatter_geo(df, 
                     lat='LATITUDE', 
                     lon='LONGITUDE',  
                           color="kmeans_label", 
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
                color = "kmeans_label")
    st.plotly_chart(fig2)




def app():
    st.markdown(
        """
# K-means
"""
    )
    df = pd.read_csv("Data/Plot_data.csv")
    for_cluster = pd.read_csv("Data/after_PCA.csv")

    df = df.drop(columns = ["Unnamed: 0"])
    for_cluster = for_cluster.drop(columns = ["Unnamed: 0"])

    st.sidebar.subheader("Parameter Setting")
    n_cluster_set = st.sidebar.slider("N cluster",
                                min_value=3, max_value=8, 
                                value=3,  step=1)
    
    st.write("K-Means is an unsupervised machine learning algorithm used for clustering. Its primary goal is to partition a dataset into groups, or “clusters,” such that data points in the same cluster are more similar to each other than to those in other clusters. Each cluster is represented by its center, known as a “centroid.”")
    st.subheader("Process")
    st.markdown("""
                1. Initialization: Choose the number of clusters (K) and randomly initialize K centroids in the feature space.
                2. Assignment: Assign each data point to the nearest centroid, forming K clusters.
                3. Update Centroids: Recalculate the centroids by taking the mean of all data points assigned to each cluster.
                4. Repeat: Iteratively repeat steps 2 and 3 until convergence. Convergence occurs when the centroids no longer change significantly, or a specified number of iterations is reached.
                5. Final Clustering: The algorithm converges to a set of centroids, and the data points are assigned to their final clusters.

                """)


    if st.sidebar.button('Press to use Example Dataset'):
        st.sidebar.markdown('Press to use Update Parameter')

        build_model(df,for_cluster,n_cluster_set)
    
   

    