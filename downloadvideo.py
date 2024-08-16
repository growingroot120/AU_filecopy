import requests

# URL of the video
video_url = 'https://mediarnsws.skyracing.com.au/Race_Replay/2024/07/20240720ROSR05_V.mp4?hdnts=exp=1722201677~acl=/*~hmac=3d6e746a2ab260003f7f5a8c9179c43856dbfab43e6fdf6a1cb73fdeae47ae59'

# File name to save the video
video_file_name = 'race_replay.mp4'

# Send a HTTP GET request to the video URL
response = requests.get(video_url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Open a file to write the video content
    with open(video_file_name, 'wb') as file:
        # Iterate over the response content in chunks
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print(f"Video downloaded successfully and saved as {video_file_name}")
else:
    print("Failed to download the video")

