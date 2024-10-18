import streamlit as st

# Page settings
# st.logo("img/logo_petrobayes.png")
st.set_page_config(
    page_title="Petrobayes",
    page_icon="img/logo_petrobayes.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": """
    # Petrobayes
    Desenvolvido por CEERMA/UFPE em parceria com a Petrobras.
    """,
    },
)

# Inject CSS for styling the header
st.markdown(
    """
    <style>
    .css-18ni7ap {
    background-color: #1D6893;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Hello World!")