# Home page
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

# Welcome text
st.subheader("Seja bem vindo ao PetroBayes, {}".format("Bia"))
st.write(
    """PetroBayes é um software projetado para conduzir análises 
Bayesianas, estimativas de confiabilidade e análise de disponibilidade. 
Ele é dividido em vários módulos, cada um atendendo a necessidades 
específicas."""
)

# Modules access
# Define custom CSS for the containers
st.markdown(
    """
    <style>
    .container_stat {
        background-color: #1F5E82;
        padding: 10px;
        border-radius: 10px;
    }
    .container_bayes {
        background-color: #11717E;
        padding: 10px;
        border-radius: 10px;
    }
    .container_disp {
        background-color: #1B8370;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inject CSS for styling the arrow and link
st.markdown(
    """
    <style>
    .arrow-link {
        color: black;
        text-decoration: none;
        font-size: 20px;
        font-weight: light;
        display: inline-flex;
        align-items: center;
    }

    .arrow-link:hover {
        color: gray;
        text-decoration: none;
    }

    .arrow {
        margin-left: 5px;
        font-size: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inject CSS for styling the arrow and link
st.markdown(
    """
    <style>
    .arrow-link {
        color: black; /* Link text color */
        text-decoration: none;
        font-size: 20px;
        font-weight: light;
        display: inline-flex;
        align-items: center;
    }

    .arrow-link:hover {
        color: gray;
        text-decoration: none;
    }

    .arrow {
        margin-left: 5px;
        font-size: 25px;
        color: white; /* Set arrow color to white */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create columns for modules blocks
col1, col2, col3 = st.columns(3)

# Modulo estatístico

# create link to file
app_path = "http://localhost:8501"
page_file_path = "pages/page_test.py"
page = page_file_path.split("/")[1][0:-3]  # get page

# Create containers and apply the CSS class
cont_stat = col1.container()
cont_stat.markdown(
    f"""<div class='container_stat'> 
    <h2 style='color: white;'>Módulo <br> Estatístico</h2>
    <p style='color: white;'>Auxiliam na análise preliminar de dados de falha de equipamentos, como aderência à uma distribuição paramétrica ou homogeneidade entre equipamentos.</p>
    <a class="arrow-link" href="{app_path}/{page}" target="_self">
    <span class="arrow">➔</span>
    </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Modulo bayesiano

# create link to file
app_path = "http://localhost:8501"
page_file_path = "pages/page_test.py"
page = page_file_path.split("/")[1][0:-3]  # get page

# Create containers and apply the CSS class
cont_bayes = col2.container()
cont_bayes.markdown(
    f"""<div class='container_bayes'> 
    <h2 style='color: white;'>Módulo <br> Bayesiano</h2>
    <p style='color: white;'>Aplicam a metodologia Bayesiana para inferir uma distribuição de incerteza sobre a função confiabilidade de um equipamento.</p>
    <a class="arrow-link" href="{app_path}/{page}" target="_self">
    <span class="arrow">➔</span>
    </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Modulo bayesiano

# create link to file
app_path = "http://localhost:8501"
page_file_path = "pages/page_test.py"
page = page_file_path.split("/")[1][0:-3]  # get page

# Create containers and apply the CSS class
cont_disp = col3.container()
cont_disp.markdown(
    f"""<div class='container_disp'> 
    <h2 style='color: white;'>Módulo <br> Disponibilidade</h2>
    <p style='color: white;'>Avalia a disponibilidade de determinado equipamento ao longo do tempo, através de estados discretos de uma Cadeia de Markov.</p>
    <a class="arrow-link" href="{app_path}/{page}" target="_self">
    <span class="arrow">➔</span>
    </a>
    </div>
    """,
    unsafe_allow_html=True,
)
