import requests

def get_user_details(user):
    r = requests.get('https://api.github.com/users/{user}'.format(user=user))

    response = r.json()
    details = {
        'name': response['name'],
        'username': response['login'],
        'followers': response['followers'],
        'following': response['following'],
        'repos': response['public_repos'],
    }
    return details