import streamlit as st

def main():
    st.title("Guía de Despliegue - Streamlit")
    st.write("Esta aplicación sirve como una referencia interactiva de los pasos requeridos para el despliegue.")

    st.header("Pasos Clave para el Despliegue")
    
    st.subheader("1. Configurar GitHub")
    st.write("Crea un repositorio público y sube tus archivos `app.py` y `requirements.txt`.")
    
    st.subheader("2. Configurar Streamlit Community Cloud")
    st.write("Conéctate a share.streamlit.io, selecciona tu repositorio y haz clic en 'Deploy'.")
    
    st.subheader("3. Monitorear Logs")
    st.write("Si algo falla durante la instalación, revisa los logs de construcción (build logs) a la derecha.")

if __name__ == '__main__':
    main()