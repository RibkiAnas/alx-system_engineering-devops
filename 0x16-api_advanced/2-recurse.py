#!/usr/bin/python3
"""
Returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of
    all hot articles for a given subreddit.
    """
    if after is None and len(hot_list) > 0:
        return hot_list

    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0"
            }

    if after is not None:
        url += "?after=" + after

    res = requests.get(url,
                       headers=headers,
                       allow_redirects=False)

    data = res.json()

    if res.status_code != 200 or data.get("error") == 404:
        return None
    posts = data["data"]["children"]
    after = data["data"]["after"]

    for post in posts:
        hot_list.append(post["data"]["title"])
        return recurse(subreddit, hot_list, after)
