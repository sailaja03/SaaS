import streamlit as st

header = st.container()
main = st.container()

with header:
    st.title("Responsible AI")
    st.markdown("""
    Most of the world is concerned about the far-off, seemingly apocalyptic potential of AI.
    But in this process we tend to overlook the immediate problem of amplifying biases of our 
    society through our programs.

    > A prime example of this would be when Microsoft's commercial algorithm
    identified some individuals with darker skin as gorillas

    > LinkedIn job adverstisements should a bias towards male users
    """)

