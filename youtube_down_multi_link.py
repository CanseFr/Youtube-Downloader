import os
from pytube import YouTube
import ffmpeg


#Librairie de Fonction _________________________________

#Chargement en %
def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(f"Progression du téléchargement {int(percent)}%")

#Information concernant le flux 
def get_info_flux(url):
    youtube_video = YouTube(url)
    print()
    print("             Auteur: " + youtube_video.author)
    print("              TITRE: " + youtube_video.title)
    print("            NB VUES:", youtube_video.views)
    print()
    top_video = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="video").order_by('resolution').desc()
    print("     Qualité video :", top_video[0].resolution)
    # print("Format video :", )

    top_audio = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
    print("      Qualité audio: " + top_audio[0].abr)
    # print("Format audio: " + youtube_video.fmt_streams)
    print()
    print("                URL: " + youtube_video.channel_url)
    print("         Channel ID:", youtube_video.channel_id)
    print("           Video ID:", youtube_video.video_id)
    print()
    input("Appuyer sur entré pour retourner au menu precedent.")
 
#Telechargement video 
def download_video():

    urls = input("Saisissez l'url :")
    youtube_video = YouTube(urls)
    youtube_video.register_on_progress_callback(on_download_progress)

    # print("STREAMS")
    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="video").order_by('resolution').desc()
    video_stream = streams[0]

    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
    audio_stream = streams[0]

    print(f"Téléchargement {youtube_video.title}...")
    video_stream.download("video")
    audio_stream.download("audio")

    audio_filename = os.path.join("audio", video_stream.default_filename)
    video_filename = os.path.join("video", video_stream.default_filename)
    output_filename = video_stream.default_filename

    ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)
    print("OK")

    # Suppresion des dossier temporaire 
    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")

def downloadS_videoS():
    
    #     https://www.youtube.com/watch?v=PqvN421JBdc
    #     https://www.youtube.com/watch?v=K_9tX4eHztY
    #     https://www.youtube.com/watch?v=YcFt1Fcesss

    nbUrls = int(input(" Combien d'URL souhaitez vous telecharger ? : "))

    tabURLS = []
    for i in range (nbUrls) :
        url_saisie = input(f"Saisissez l'url {i} :")
        tabURLS.append(url_saisie)
    
    print(tabURLS)

    for url in tabURLS:

        youtube_video = YouTube(url)
        youtube_video.register_on_progress_callback(on_download_progress)

        # Selection Best Quali
        streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="video").order_by('resolution').desc()
        video_stream = streams[0]

        streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
        audio_stream = streams[0]

        # Telechargement
        print(f"Téléchargement {youtube_video.title}...")
        video_stream.download("video")
        audio_stream.download("audio")

        audio_filename = os.path.join("audio", video_stream.default_filename)
        video_filename = os.path.join("video", video_stream.default_filename)
        output_filename = video_stream.default_filename

        ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)
        print("OK")

        # Suppresion des dossier temporaire 
        os.remove(audio_filename)
        os.remove(video_filename)
        os.rmdir("audio")
        os.rmdir("video")


#Telechargement audio 
def download_audio():

    urls = input("Saisissez l'url :")
    youtube_video = YouTube(urls)
    youtube_video.register_on_progress_callback(on_download_progress)

    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
    audio_stream = streams[0]

    print(f"Téléchargement {youtube_video.title}...")
    audio_stream.download("audio")

def downloadS_audioS():
    
    #     https://www.youtube.com/watch?v=PqvN421JBdc
    #     https://www.youtube.com/watch?v=K_9tX4eHztY
    #     https://www.youtube.com/watch?v=YcFt1Fcesss

    nbUrls = int(input(" Combien d'URL souhaitez vous telecharger ? : "))

    tabURLS = []
    for i in range (nbUrls) :
        url_saisie = input(f"Saisissez l'url {i} :")
        tabURLS.append(url_saisie)
    
    print(tabURLS)

    for url in tabURLS:

        youtube_video = YouTube(url)
        youtube_video.register_on_progress_callback(on_download_progress)

        streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
        audio_stream = streams[0]

        # Telechargement
        print(f"Téléchargement {youtube_video.title}...")
        audio_stream.download("audio")

        # audio_filename = os.path.join("audio", video_stream.default_filename)
        # video_filename = os.path.join("video", video_stream.default_filename)
        # output_filename = video_stream.default_filename














#fonction a fair 
#information d un flux 
# telecharger audio 
# telecharger video 