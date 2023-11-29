import streamlit as st



def app():
    st.title('Cluster Introduction')

   
    st.markdown(
    """
# 
Cluster analysis, a powerful technique in data analysis, 
seeks to identify groups of data elements that share similarities. 
Employing this method, one can discern patterns and relationships 
among different variables, making it a valuable tool for gaining 
insights into data.

In this section, we will delve into what cluster analysis entails, 
how it is used in data mining, and the five types of clusters it can identify

"""
)   
    st.divider()
    st.image('Images/cluster_example.png')

    st.markdown("""
There are methods or algorithms that can be used in case clustering : K-Means Clustering, Affinity Propagation, Mean Shift, Spectral Clustering, Hierarchical Clustering, DBSCAN, ect.

                """)
    
    st.subheader("Fine-tuning Parameters")

    st.markdown("""
                Theortically, there are some common way for choose the best parameters like elbow
                plot for K-means or silhouette score. While the problem is because there is not a 
                standarded metric to evaluate the performance of a cluster. Also, sometimes the best cluster
                in data perstpectie may not have the best interpretation when domain knowledge is involved. 

                So, actually, check it visual could be a additional method in parameter fine-tuning
                process.
                """)    
    # st.image("Image/")
    