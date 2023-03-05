import requests
from requests import HTTPError

def get_app_ids():
    steam_appid_endpoint = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    headers = {'Accept': 'application/json'}

    try:
        response = requests.get(steam_appid_endpoint, headers=headers)
        response.raise_for_status()

    except HTTPError as http_err:
        print(f'An HTTP error has occurred: {http_err}')

    except Exception as err:
        print(f'An error has occurred: {err}')

    else:
        app_ids = response.content
        with open('steam_app_ids.json', 'wb') as file:
            file.write(app_ids)

if __name__ == '__main__':
    get_app_ids()