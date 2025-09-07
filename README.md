# database_spotify_project
# Spotify Track Data Collector 🎵

This project extracts track details from the **Spotify API** using [Spotipy](https://spotipy.readthedocs.io/) and stores them into a **MySQL database**.  
It also saves the data into a **CSV file** and visualizes track popularity & duration with **Matplotlib**.

---

## 📌 Features
- Fetches track info (name, artist, album, popularity, duration) from Spotify API.
- Stores track data in a MySQL database (`spotify_tracks` table).
- Saves data into a `track_data.csv` file (tabular format).
- Generates a simple bar chart showing **popularity vs duration**.

---

## 🛠️ Requirements

Make sure you have these installed:

- Python 3.8+
- Spotify Developer Account ([Get credentials](https://developer.spotify.com/dashboard/))
- MySQL Server

### Python Libraries
Install dependencies with:

bash
pip install spotipy pandas matplotlib mysql-connector-python
⚙️ Setup
Clone the repository

bash
Copy code
git clone https://github.com/yourusername/spotify-track-collector.git
cd spotify-track-collector
Update Spotify API Credentials
Open the script and replace:

python
Copy code
client_id='replace with your client id'
client_secret='replace with your client secret'
---------------------------------------------------------------------------------
Setup MySQL Database
Create a database and table:

sql
Copy code
CREATE DATABASE spotify_db;

USE spotify_db;

CREATE TABLE spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
);
--------------------------------------------------------------------------------------
Prepare track links
Add Spotify track links (one per line) inside links.text file. Example:

arduino
Copy code
https://open.spotify.com/track/3tjFYV6RSFtuktYl3ZtYcq
https://open.spotify.com/track/5HCyWlXZPP0y6Gqq8TgA20
▶️ Run the Project
bash
Copy code
python spotify.py
This will:

Insert track data into MySQL

Save all track data in track_data.csv

Show a bar chart for the last processed track

📊 Example Output (CSV)
Track Name	Artist	Album	Popularity	Duration (minutes)
Arabic Kuthu	Anirudh Ravichander	Arabic Kuthu - Halamithi Habibo	78	4.15
Another Song	Artist Name	Album Name	65	3.52

📸 Visualization
The script generates a simple bar chart comparing:

Popularity

Duration (minutes)
