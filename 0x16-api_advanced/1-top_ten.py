#!/usr/bin/python3
"""
Titles of the first 10 hot posts listed for
a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0"
            }
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        posts = data["data"]["children"]

        for i in range(10):
            title = posts[i]["data"]["title"]
            print(title)
    else:
        print(None)
