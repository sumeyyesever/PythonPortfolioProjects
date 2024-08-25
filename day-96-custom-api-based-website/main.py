import random
from flask import Flask, render_template
import requests
import os
from datetime import datetime

app = Flask(__name__)

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]

response = requests.post('https://api.artsy.net/api/tokens/xapp_token',
                         data={'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET})

token = response.json()['token']

# With the access token, we can now make requests to the Artsy API.
headers = {
    'X-Xapp-Token': token
}

size = 100
data_response = requests.get(f'https://api.artsy.net/api/artworks?size={size}', headers=headers)

artworks_data = data_response.json()
artworks_array_before = artworks_data["_embedded"]["artworks"]
artworks_array = random.sample(artworks_array_before, len(artworks_array_before))


def art_info():
    current_day = datetime.now().timetuple().tm_yday
    index = current_day % len(artworks_array)

    artwork_title = artworks_array[index]["title"]
    artwork_date = artworks_array[index]["date"]
    artwork_museum = artworks_array[index]["collecting_institution"]
    artwork_img_url = artworks_array[index]["_links"]["thumbnail"]["href"]
    artwork_permalink_url = artworks_array[index]["_links"]["permalink"]["href"]
    artwork_artist_url = artworks_array[index]["_links"]["artists"]["href"]
    artist_response = requests.get(artwork_artist_url, headers=headers)
    artist_data = artist_response.json()
    artist_info = artist_data["_embedded"]["artists"][0]
    artist_name = artist_info["name"]
    artist_birthday = artist_info["birthday"]
    artist_deathday = artist_info["deathday"]
    info_array = [artwork_title, artwork_date, artwork_museum, artwork_img_url, artwork_permalink_url,
                  artist_name, artist_birthday, artist_deathday]
    return info_array


@app.route("/")
def home():
    information_array = art_info()
    return render_template("index.html", url=information_array[3], name=information_array[0],
                           date=information_array[1], museum=information_array[2], permalink=information_array[4],
                           artist=information_array[5], artist_birth=information_array[6], artist_death=information_array[7])


if __name__ == "__main__":
    app.run(debug=True)


