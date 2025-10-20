import requests
import base64
import spotify_secrets


def get_tracks(access_token, q, limit = 1, offset = 0):
    endpoint = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'q': q,
        'type': 'track',
        'limit': limit,
        'offset': offset
    }

    # Make the GET request
    response = requests.get(endpoint, headers=headers, params=params)
    return response

def get_track_by_isrc(access_token, isrc):
    endpoint = f'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'q': f'isrc:{isrc}',
        'type': 'track',
        'limit': 1
    }

    # Make the GET request
    response = requests.get(endpoint, headers=headers, params=params)
    return response

# Fully AI generated function with some changes for our use
def get_token():
    # FILL THIS WITH YOUR VALUES
    client_id = spotify_secrets.name
    client_secret = spotify_secrets.secret

    # Encode client ID and client secret in base64
    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode())

    # Spotify API token endpoint
    token_url = 'https://accounts.spotify.com/api/token'

    # Set up headers and payload for the POST request
    headers = {
        'Authorization': f'Basic {client_creds_b64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    # Make the request
    response = requests.post(token_url, headers=headers, data=data)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve access token:", response.text)
    else:
        token_info = response.json()
        access_token = token_info['access_token']
        print("Access token:", access_token)

    return access_token

