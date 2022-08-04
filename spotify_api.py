import requests
import datetime
from pprint import pprint as pp


class SpotifyAPI:
    token_url = "https://accounts.spotify.com/api/token"

    def perform_auth(self):
        """
        Generates access token and writes it in a file
        :return: access token in "token.txt"
        """
        token_data = {
            "grant_type": "client_credentials"
        }
        token_headers = {"Authorization": "Basic Y2Q2M2NhMjJiM2Q0NGRkMDkwNmJiYWUzZWJhNTZmMTY6NzI4NjRiZWIxMmY3NDJiZjkzZmQ1N2I0MjkwMzgyNjU="}
        r = requests.post(SpotifyAPI.token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            raise Exception("could not authenticate client.")
        data = r.json()
        access_token = data['access_token']
        with open("token.txt", "w") as txt_file:
            txt_file.write(access_token)

    def search(self, query, search_type='artist'):
        """
        Performs a search with Spotify API
        :param query: string
        :param search_type: artist,track
        :return: json
        """
        with open("token.txt", "r") as txt_file:
            access_token = txt_file.read()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        params = {"q": query, "type": search_type.lower()}
        endpoint = "https://api.spotify.com/v1/search"
        r = requests.get(endpoint, headers=headers, params=params).json()
        pp(r)
        try:
            info = {"album_name": r["tracks"]["items"][0]["album"]["name"],
                    "release_date": r["tracks"]["items"][0]["album"]["release_date"]}

        except KeyError:
            self.perform_auth()
            return self.search(query, search_type)

        return info


spotify = SpotifyAPI()
pp(spotify.search("NF", search_type='track'))
