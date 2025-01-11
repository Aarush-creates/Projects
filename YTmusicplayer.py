import streamlit as app
import requests

API_KEY = "AIzaSyAZcJ6gHDPdYbRPKQB_1TqD157h-FSQUI4"
BASE_URL = "https://www.googleapis.com/youtube/v3"

def fetch_videos(search_prompt):
    url = f"{BASE_URL}/search?part=snippet&maxResults=20&q={search_prompt}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        app.error(f"Failed to fetch data: {response.status_code}")
        return []

def app_interface():
    app.markdown(
        """<style>
        body {
            background-color: #121212;
            color: white;
            font-family: Arial, sans-serif;
        }
        .stButton > button {
            background-color: #1db954;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 50px;
            font-size: 14px;
        }
        .stButton > button:hover {
            background-color: #535353;
        }
        .stTextInput > div > input {
            background-color: #1db954;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
        }
        .stTextInput > div > label {
            color: #1db954;
        }
        </style>""",
        unsafe_allow_html=True
    )

    app.title("Spopify Music Player but with Youtube")

    if "queue" not in app.session_state:
        app.session_state.queue = []
    if "current_index" not in app.session_state:
        app.session_state.current_index = 0
    if "is_playing" not in app.session_state:
        app.session_state.is_playing = False

    search_prompt = app.text_input("Search for a song:")
    if search_prompt:
        videos = fetch_videos(search_prompt)
        if 'items' in videos:
            results = videos['items']
            app.subheader("Search Results")
            for idx, video in enumerate(results):
                if video['id']['kind'] == "youtube#video":
                    title = video['snippet']['title']
                    video_id = video['id']['videoId']
                    if app.button(f"{title}", key=f"result_{idx}"):
                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                        app.session_state.queue.append({"title": title, "url": video_url})
                        app.session_state.current_index = len(app.session_state.queue) - 1
                        app.session_state.is_playing = True

    app.subheader("Your Playlist")
    for idx, track in enumerate(app.session_state.queue):
        if app.button(f"{track['title']}", key=f"queue_{idx}"):
            app.session_state.current_index = idx
            app.session_state.is_playing = True

    col_prev, col_play, col_next = app.columns([1, 1, 1])
    with col_prev:
        if app.button("Previous"):
            if app.session_state.current_index > 0:
                app.session_state.current_index -= 1
                app.session_state.is_playing = True
    with col_play:
        if app.button("Play / Pause"):
            app.session_state.is_playing = not app.session_state.is_playing
    with col_next:
        if app.button("Next"):
            if app.session_state.current_index < len(app.session_state.queue) - 1:
                app.session_state.current_index += 1
                app.session_state.is_playing = True

    if app.button("Clear Playlist"):
        app.session_state.queue = []
        app.session_state.current_index = 0
        app.session_state.is_playing = False

    if app.session_state.queue:
        current_song = app.session_state.queue[app.session_state.current_index]
        app.markdown(f"<h3 style='color: #1DB954;'>Now Playing: {current_song['title']}</h3>", unsafe_allow_html=True)
        if app.session_state.is_playing:
            app.video(current_song["url"])
        else:
            app.write("Paused")

if __name__ == "__main__":
    app_interface()
