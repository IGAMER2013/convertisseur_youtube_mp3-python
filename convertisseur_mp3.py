from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def telecharger_convertir_youtube_vers_mp3(url_youtube):
    repertoire_sortie = "/Users/jorisvillaseque/Desktop"
    print(f"Téléchargement de la vidéo depuis {url_youtube}")
    yt = YouTube(url_youtube)
    video = yt.streams.get_highest_resolution()

    chemin_fichier_sortie = video.download(repertoire_sortie)

    print(f"Conversion de {chemin_fichier_sortie} en mp3")
    clip = AudioFileClip(chemin_fichier_sortie)

    chemin_fichier_sortie_sans_extension = os.path.splitext(chemin_fichier_sortie)[0]
    clip.write_audiofile(f"{chemin_fichier_sortie_sans_extension}.mp3")

    print(f"Suppression du fichier vidéo téléchargé {chemin_fichier_sortie}")
    os.remove(chemin_fichier_sortie)

    print(f"Conversion terminée avec succès. Vérifiez le fichier à {chemin_fichier_sortie_sans_extension}.mp3")

if __name__ == "__main__":
    url_youtube = input("Entrez l'URL de YouTube: ")
    telecharger_convertir_youtube_vers_mp3(url_youtube)
