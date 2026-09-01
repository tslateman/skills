import requests


def get(url, headers=None, timeout=30):
    return requests.get(url, headers=headers, timeout=timeout)


def post(url, json=None, headers=None, timeout=30):
    return requests.post(url, json=json, headers=headers, timeout=timeout)
