import streamlit as st

header = st.container()
main = st.container()

with header:
    st.title("Responsible AI")
    st.header("Team: SaaS")
    st.subheader("Solutions-as-a-Service")
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

    st.caption("But how can a computer program be racist?")

