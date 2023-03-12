import streamlit as st
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import re
from pydub import AudioSegment
import speech_recognition as sr

def is_valid_youtube_url(url):
    regex = r'(https?://)?(www\.)?youtube\.com/watch\?v=[\w-]{11}'
    return re.match(regex, url) is not None

def is_valid_youtube_url_mobile(url):
    regex = r'(https?://)?youtu\.be/[\w-]{11}'
    return re.match(regex, url) is not None

st.title(":blue[FD] Download :blue[FD]")
# Ingresa la URL del video de YouTube que deseas descargar
col1, col2, col3= st.columns([3,2,1])
try:
    with col1:
        url = st.text_input("Coloca el URL Aqui!")
        
        if is_valid_youtube_url(url):
            yt = YouTube(url)
        elif is_valid_youtube_url_mobile(url):
            yt = YouTube(url)
        else:
            st.write('Por favor, introduce una URL de video de YouTube válida')
    with col2:
        st.caption("Presiona para Empezar!")
        if st.button("Convertir Audio"):
        #titulo = yt.title
            audio_stream = yt.streams.filter(only_audio=True).first()
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
            with col3:
                if st.button("Convertir audio a texto"):
                    audio = AudioSegment.from_mp3('FDmusic.mp3')
                    audio.export('convert.wav', format='wav')
                    r = sr.Recognizer()
                    with sr.AudioFile('convert.wav') as source:
                        audio = r.record(source)
                    text = r.recognize_google(audio, language='es-ES')
                    texto=st.text_area(text)
                    print(text)
except VideoUnavailable:
    print("DERECHOS DE AUTOR")
    st.write('NO SE PUEDE DESCARGAR POR DERECHOS DE AUTOR')
