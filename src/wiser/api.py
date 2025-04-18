import requests


def wiser_get(url, token):
    return requests.get(url, headers={"Authorization": f"Bearer {token}"})

def wiser_patch(url, token, data):
    return requests.patch(url, json=data, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    })
