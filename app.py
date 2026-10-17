import streamlit as st
import pypdf
import os

def main():
    st.title("Lector de Directrices de Despliegue")
    st.write("Esta aplicación lee de forma dinámica las pautas de despliegue desde el documento PDF.")

    pdf_path = '/content/Guidelines __ Model Deployment via Streamlit and GitHub_Spanish.pdf'

    if not os.path.exists(pdf_path):
        st.error(f"No se encontró el archivo PDF en la ruta: {pdf_path}")
        return

    try:
        # Cargar y procesar el archivo PDF
        reader = pypdf.PdfReader(pdf_path)
        num_pages = len(reader.pages)
        
        st.sidebar.header("Navegación")
        st.sidebar.write(f"Total de páginas: {num_pages}")
        
        # Selector de página
        page_num = st.sidebar.slider("Selecciona una página para leer", 1, num_pages, 1)
        
        # Extraer texto de la página seleccionada
        page = reader.pages[page_num - 1]
        text = page.extract_text()
        
        st.subheader(f"Contenido de la Página {page_num}")
        st.text_area("Texto extraído:", value=text, height=400)
        
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo PDF: {e}")

if __name__ == '__main__':
    main()