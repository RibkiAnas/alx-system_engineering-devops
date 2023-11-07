#!/usr/bin/python3
"""
number of subs for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0"
            }
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        subs = data["data"]["subscribers"]
        return subs
    else:
        return 0
