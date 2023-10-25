from pytube import YouTube, Playlist

def get_video_info(video_url):
    try:
        yt = YouTube(video_url)
        title = yt.title
        author = yt.author
        length = yt.length
        return {
            "title": title,
            "author": author,
            "length": length
        }
    except Exception as e:
        return {"error": str(e)}

def download_video(video_url, output_path=".\midias"):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        return f"Downloaded: {yt.title}"
    except Exception as e:
        return f"Error: {str(e)}"
    
 
def get_pvideo_info(video_url):
    try:
        yt = YouTube(video_url)
        title = yt.title
        author = yt.author
        length = yt.length
        return {
            "title": title,
            "author": author,
            "length": length
        }
    except Exception as e:
        return {"error": str(e)}   

def download_playlist(playlist_url, output_path=".\midias"):
    try:
        playlist = Playlist(playlist_url)
        for video_url in playlist.video_urls:
            download_video(video_url, output_path)
        return f"Downloaded {len(playlist.video_urls)} videos from the playlist: {playlist.title}"
    except Exception as e:
        return f"Error: {str(e)}"

# Exemplo de uso:
video_url = input("Digite o link do vídeo: ")
playlist_url = input("Digite o link da playlst: ")

# Obtém informações do vídeo
video_info = get_video_info(video_url)
print("Informações do vídeo:")
print(video_info)

# executa para baixar um vídeo
download_result = download_video(video_url)
print(download_result)

# executa para baixar uma playlist
pvideo = get_pvideo_info(video_url)
playlist_download_result = download_playlist(playlist_url)
print(playlist_download_result)
print("Informações da playlist:")
print(video_info)