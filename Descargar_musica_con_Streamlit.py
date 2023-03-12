import streamlit as st
from pytube import YouTube


st.title(":blue[FD] Download :blue[FD]")
# Ingresa la URL del video de YouTube que deseas descargar
col1, col2= st.columns([3,1])
with col1:
    url = st.text_input("Coloca el URL Aqui!")
with col2:
    st.caption("Presiona para Empezar!")
    if st.button("Convertir Audio"):
# Crea un objeto de YouTube
        yt = YouTube(url)
        #titulo = yt.title
# Filtra la transmisión de audio
        audio_stream = yt.streams.filter(only_audio=True).first()
# Descarga el archivo de audio
        #audio_stream.download( output_path=".", filename=f"{titulo}.mp3") lo pondremos sin titulo por el momento
        audio_stream.download( output_path=".", filename=f"FDmusic.mp3")
        st.balloons()
        with col1:
            st.success("Audio bajado, ahora presiona en descargar y disfruta")
        st.caption("Presiona para descargar!")
        with open("FDmusic.mp3", "rb") as file:
            st.download_button(
                label="Descargar Musica",
                data=file,
                file_name='FDmusic.mp3'
                )