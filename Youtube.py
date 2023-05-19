import os
import json
import googleapiclient.discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import credentials


# Set up OAuth credentials
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
client_secrets_file = "C:/Users/AbrarZaved/Downloads/client_secrets.json"  # Path to your client secrets JSON file
token_file = "C:/Users/AbrarZaved/Downloads/token.json"  # Path to store token JSON file

def authenticate():
    creds = None
    # The file token.json stores the user's access and refresh tokens,
    # and is created automatically when the authorization flow completes for the first time.
    if os.path.exists(token_file):
        creds = credentials.Credentials.from_authorized_user_file(token_file, scopes)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, "w") as token:
            token.write(creds.to_json())

    return creds

def remove_duplicate_videos(playlist_id):
    # Authenticate using OAuth
    creds = authenticate()

    # Create a YouTube Data API client
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

    # Retrieve the playlist items
    playlist_items = []
    next_page_token = None
    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        playlist_items.extend(response["items"])
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    # Remove duplicate videos
    video_ids = set()
    for item in playlist_items:
        video_id = item["snippet"]["resourceId"]["videoId"]
        if video_id in video_ids:
            request = youtube.playlistItems().delete(
                id=item["id"]
            )
            request.execute()
            print(f"Removed duplicate video: {video_id}")
        else:
            video_ids.add(video_id)

    print("Duplicate videos removed successfully.")

# Replace 'YOUR_PLAYLIST_ID' with the actual ID of your YouTube playlist
playlist_id = "PLp93SWhbVKK6oAYWsP-siEu9IJ0XSeBWi"
remove_duplicate_videos(playlist_id)
