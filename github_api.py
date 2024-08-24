import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def get_maintainers(owner, repo):
    """Fetches maintainers of a GitHub repository."""

    url = f"https://api.github.com/repos/{owner}/{repo}/collaborators"
    headers = {
        "Authorization": f"token {config['GITHUB']['api_token']}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes

    maintainers = [user['login'] for user in response.json() if user['permissions']['admin']]
    return maintainers
