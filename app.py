import streamlit as st
import mitdeeplearning as mdl
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import load as l

header = st.container()
main = st.container()

from ipywidgets import interact

faces = l.images[np.where(l.labels == 1)[0]]
not_faces = l.images[np.where(l.labels == 0)[0]]


with header:
    st.title("Responsible AI")
    st.header("Team: SaaS")
    st.subheader("Solutions-as-a-Service")
    

with main:
    st.markdown("""
    Most of the world is concerned about the far-off, seemingly apocalyptic potential of AI.
    But in this process we tend to overlook the immediate problem of amplifying biases of our 
    society through our programs.

    Three such instances are
    """)
    col1, col2, col3 = st.columns(3)

    col1.subheader("Google's Face recognition algorithm")
    col1.write("Classified dark skinned males as gorillas")

    col2.subheader("LinkedIn's job advertisements")
    col2.write("Showed preference to male names in searches")

    col3.subheader("Microsoft's AI chatbot Tay")
    col3.write("churned out anti-semitic sentences after being trained on Twitter for one day")

    
    st.header("But how can a computer program be racist?")

    with st.expander("Peek in for an experiment"):
        st.write("What do you see in the image below?")
        st.image('./images/watermelon.png', width = 300)

        st.write("What about now?")
        st.image('./images/yellow_watermelon.png', width = 300)
        
    st.markdown("""
        The above example shows us a pervasive cause ill-performing ML models.

        ### The Devil is in the Data
    """)
    with st.expander("Class imbalances"):
        st.write("Class imbalances in training data causes the the ML models to be biased towards more frequent classes")
        st.markdown("""
            #### Distribution shifts

                Sourcing different datasets for training, testing and validation

            #### Batch Selection
            
                Ensuring that every class has equal representation in the training sample.

            #### Example weighting
                Take the frequency of each class. The weights assigned to each of these samples is now the inverse of the frequencies of the classes. As a result of this, we’ll have equal contribution from each sample to the final model.
        """)

    index = st.slider('Index', 0, 50, 1)
    st.image(faces[index], width= 300)

    st.info("What potential bias do we observe in this dataset?")

    st.markdown("""
            Our solution will involve the use of debiasing-Variational Autoencoders (DB-VAE) first proposed by Alexander Amini et al in 2019. 
            This algorithm will help identify under-represented examples and increase the probability at which the learning algorithm samples these data points. 
            The latent variables that cause these biases are learnt by the DB-VAE during training and must effectively reduce errors.
    """)

    st.image("./images/DB-VAE.png", width = 300)
    st.caption("Here we see the structure of a Debiasing-Variational AutoEncoder")

    with st.expander("A quick look at the results"):
        st.image("./images/accuracies.png")