import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pandas as pd



init_streamlit_comm()


st.title("PygWalker ❄️")
st.sidebar.markdown("# PygWalker ❄️")

st.subheader("i_b_v_seleccion.csv")

@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv("./data/i_b_v_seleccion.csv")
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    return StreamlitRenderer(df, spec="./spec/chart_meta_0.json",spec_io_mode="rw")

renderer = get_pyg_renderer()




renderer.explorer()