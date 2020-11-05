from pytube import YouTube
import os
from tkinter import *
import youtube_dl

root=Tk()
root.geometry('600x200')
root.title('Youtube MB3 Downloder')
Label_1 = Label(root,text="Paste The Youtube Link Here", font=("bold",20))
Label_1.place(x=120,y=20)

mylink=StringVar()
pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140,y=80)
# youtube_video_url = 'https://www.youtube.com/watch?v=DkU9WFj8sYo'
# youtube_video_url = input("Please enter your URL here:")

def downloadAudio():
    youtube_audio_url=str(mylink.get())

    ydl_opts = {
      'format': 'bestaudio/best',
        'keepvideo': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
     }],
   }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_audio_url])

    

       
Button(root,text="Download MB3", width=20, bg='green', fg='white', command=downloadAudio).place(x=220,y=110)

root.mainloop()