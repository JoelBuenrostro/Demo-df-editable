import streamlit as st
import pandas as pd

# Configuracion
st.set_page_config(
    page_title='Widget editable dataframes',
    page_icon=None,
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Creamos un DataFrame de ejemplo
data = {'nombre': ['Juan', 'Ana', 'Pedro', 'Lucía'],
        'edad': [25, 30, 40, 35],
        'país': ['México', 'Argentina', 'España', 'Chile']}
df = pd.DataFrame(data)

# Creamos el título y la descripción de la aplicación
st.title('Editor de datos')
st.write('''¡Aprende a utilizar la función st.experimental_data_editor de
Streamlit para crear aplicaciones web interactivas que permitan editar y
manipular datos fácilmente! Con esta herramienta, podrás mostrar un DataFrame
 en una tabla interactiva que permita a los usuarios hacer clic en las celdas
 para editar su contenido, agregar nuevas filas o columnas, y ver los cambios
  en tiempo real. ''')

st.write('''st.experimental_data_editor es una función de la biblioteca Streamlit
que permite mostrar y editar un DataFrame en una aplicación web de manera
interactiva.''')

st.write('''Cuando se llama a st.experimental_data_editor, se muestra el
DataFrame en una tabla interactiva en la aplicación. Los usuarios pueden
hacer clic en las celdas para editar su contenido y agregar nuevas filas
 o columnas según sea necesario.''')

# Mostramos el editor de datos y almacenamos la copia editada en una variable
edited_data = st.experimental_data_editor(
    data=df,
    use_container_width=True,
    num_rows='dynamic',
    disabled=False,
    key='editable',
)

st.write('''Cuando los usuarios hacen cambios en la tabla,
st.experimental_data_editor devuelve una copia editada del DataFrame original.
Esta copia se puede utilizar en la aplicación para realizar más operaciones
o se puede mostrar al usuario para que vea los cambios que ha realizado.''')

# Mostramos el DataFrame editado
st.write('DataFrame editado:', edited_data)

footer_column1, footer_column2, footer_column3, footer_column4 = st.columns(4)

with footer_column1:
    st.markdown('[![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joelbuenrostro/)')

with footer_column2:
    st.markdown('[![Follow](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/esteGeek)')

with footer_column3:
    st.markdown('[![Follow](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/joel_buenrostro/)')

with footer_column4:
    st.markdown('[![Follow](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/JoelBuenrostro/)')
