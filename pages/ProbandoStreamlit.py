import streamlit as st
import numpy as np
import pandas as pd
import time


st.title("Utilizando CSV")
st.write('data_spotify-api.csv')
df = pd.read_csv("data/data_spotify-api.csv")

st.dataframe(df.head())

st.divider()

# ---------------
st.write('ING_BODEGA_Y_VTAS_20232 - OC_202310-Formateado.csv')

df_bodega = pd.read_csv("data/ING_BODEGA_Y_VTAS_20232-OC_202310-Formateado.csv")
st.table(df_bodega.head())


st.divider()
# ---------------

st.write('ING_BODEGA_Y_VTAS_20232 - OC_202310-Seleccionado.csv')

df_seleccion = pd.read_csv("data/ING_BODEGA_Y_VTAS_20232-OC_202310-Seleccion.csv")

st.dataframe(df_seleccion.style)

st.divider()
# ---------------

x = st.slider('x', min_value=10, step=2)  # 👈 this is a widget
st.write(x, 'squared is', x * x)

map_data = pd.DataFrame(
    np.random.randn(x, 2) / [50, 50] + [-41.31490061565156, -72.99047498782379],
    columns=['lat', 'lon'])

st.dataframe(map_data.head())

st.map(map_data)

st.divider()
# ---------------

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.table(chart_data)

st.divider()
# ---------------

st.text_input("Tu nombre aqui", key="valor_identificador")

# You can access the value at any point with:
st.session_state.valor_identificador


st.divider()
# ---------------

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


st.divider()
# ---------------

df_ssl = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Selecciona el OC',
     df_seleccion['OC'])

'OC seleccionado: ', option





st.divider()
# ---------------

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")



st.divider()
# ---------------

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

st.divider()
# ---------------


if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

st.divider()
# ---------------

if "contador" not in st.session_state:
    st.session_state.contador = 0

st.session_state.contador +=1

st.header(f"La pagina corre {st.session_state.contador} veces")
st.button("Correr denuevo")

st.divider()
# ---------------

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)


'''
conn = st.connection("my_database")
df = conn.query("select * from my_table")
st.dataframe(df)
'''