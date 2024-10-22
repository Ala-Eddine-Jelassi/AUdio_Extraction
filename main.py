import streamlit as st 
from moviepy.editor  import VideoFileClip
import os
import shutil



st.title("Audio Extractor")

video = st.file_uploader("upload your video",type=["mp3","mp4","mov"])
save_path =""
if not os.path.exists("download_video"):
    os.makedirs("download_video")

if video is not None :
    st.write("please wait a moment")
    save_path = os.path.join("download_video",video.name)
    with open(save_path,"wb") as file : 
        shutil.copyfileobj(video,file)
    

quotes_list = [
    'I Hope You Win The War You Tell No One About',
               "Don't Let The Ugliness In Other Kill The Beauty In You",
               "Don't Ever Set Yourself On Fire , Just To Keep Other People Warm",
               "Don't Manage Their Behavior , Manage Your Expectations",
               "Whatever is good for the soul , do that",
               "It Won't Always Make Sense That's Okay",
               "Creativity is allowing yourself to make mistakes, Art is knowing which ones to keep",
               "You're Not lost You're Here",
               "if you're ever in doubt, choose yourself",
               "stop being mean to yourself , you'e trying your best ",
               "It's peaceful when you're not interested in anyone",
               "vibe alone for a bit , you'll realize a lot ",
               "you deserve the empathy you give others",
               "love yourself the way you wish they did",
               "trust the vibe you get ,energy doesn't lie",
               "work,but don't forget to live",
               "you can still love the people who hurt you, but it doesn't change the face that you need to let those people go ",
               "the best things are not things",
               "happiness is not by chance but by choice",
               "life is short , love yourself more ",
               "the future belongs to those who prepare for it today",
               "your idea of me is not my responsibility to live up to ",
               "to everything i've ever lost : thank you for setting me free",
               "Repeat after me : I don't want what doesn't want me ",
               "love will find you when you stop looking",
               "stop having relationshio problems with people you're not in relationship with",
               "maybe they can't love you because they're still trying to love themselves",
               "the answer is in how they treat you ",
               "it's okay to be sad about someone you never really had ",
               "sometimes you don't get what you want because you deserve better",
               "BE YOU ",
               "Don't give up",
               "the only person you should try to be better than is the person you were yesterday",
               "there's always going to be someone who doesn't see your worth , don't let it be you",
               "GOOD NEWS : you'll get over it just like you got over that other thing",
               "I pray you heal from things nobody ever apologized for ",
               "thank yourself for how far you've come it hasn't been easy ",
               "Your anxiety is lying to you",
               "Be so private they can't do nothing but assume",
               "learn to see people for who they are ,not who you want them to be ",
               "IDK why we met but i'm so happy we did",
               "you will be okay , storms don't last forever",
               "I don't regret , just pretend shit never happend",
               "God heard you , just be patient",
               "People go but how they left alaways stays",
               "take it day by day , don't stress too much about tomorrow"]

if 'index' not in st.session_state:
    st.session_state['index'] = 0
def next_item():
    st.session_state['index'] = (st.session_state['index'] + 1) % len(quotes_list)

def quote(): 
    st.info(f" Quotes Of The Day : “ {quotes_list[st.session_state['index']]}  ”")
    


quote()
st.button("Other Quotes",on_click=next_item)  


st.link_button('Youtube Channel',url="https://www.youtube.com/@Here_We_Code")




try : 
    st.video(video)
    audio_file_path = "download_video/extraction_audio.mp3"
    movie_video = VideoFileClip(save_path)
    audio = movie_video.audio
    audio_file = audio.write_audiofile(audio_file_path) 

    with open(audio_file_path,'rb') as folder :
        st.audio(folder,format='audio/mp3')

    with open(audio_file_path,'rb') as folder :
        st.download_button(
                          label='Download file',
                           data=folder,
                           file_name="extracted_audio.mp3",
                           mime="audio/mp3")
except Exception as e :
    st.write('Please upload you file')
col1,col2 = st.columns(2)

with col1:
    st.video("https://youtu.be/Xiom_UqPqow?si=g3-i5GpId7WiuhKZ",autoplay=True)
with col2:
    st.video("https://youtu.be/q0feWYovr3s?si=Tfqhbu2Ghd3gWeNg")