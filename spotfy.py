from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re
import mysql.connector


#set up client credentials
sp=spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id='replace with your client id', #clinetID

    client_secret='replace with  your client secret' #clientsecrectkey
))

db_config={'host': 'localhost',  'user':'root' ,'password': 'root','database': 'spotify_db'}
connection=mysql.connector.connect(**db_config)
cursor=connection.cursor()



#full track url

file_path="links.text"
with open(file_path,'r') as file:
    track_urls=file.readlines()
for track_url in track_urls:
    track_url=track_url.strip()
    try:
        track_id=re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)
        track=sp.track(track_id)

        track_data={
            'track': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'popularity': track['popularity'],
            'Duration(minutes)': track['duration_ms']/60000,
                    }

        query="""insert into spotify_tracks (track_name,artist, album,popularity ,
            duration_minutes) values (%s,%s,%s,%s,%s)
            """
        cursor.execute(query,(track_data['track'],
               track_data['artist'],
               track_data['album'],
               track_data['popularity'],
               track_data['Duration(minutes)']))

        df = pd.DataFrame(track_data)

        df.to_csv('track_data.csv', index=False)

        connection.commit()

    except Exception as error:
        print(f"Error: {error}")


print(f"\nTrack name: {track_data['track']}")
print(f"Artist : {track_data['artist']}")
print(f"Album : {track_data['album']}")
print(f"Popularity: {track_data['popularity']}")
print(f"Duration(minutes): {track_data['Duration(minutes)']}")


features=['Popularity','Duration(minutes)']
values=[track_data['popularity'],track_data['Duration(minutes)']]
plt.figure(figsize=(10,10))
plt.bar(features,values,color='yellow')
plt.title(f"track popularity '{track_data['track']}'")
plt.ylabel('value')
plt.show()


