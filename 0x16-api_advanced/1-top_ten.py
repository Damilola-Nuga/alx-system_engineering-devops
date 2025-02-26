#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": (
            "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
        )
    }
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Handle invalid subreddit
    if response.status_code != 200:
        print("None")
        return

    try:
        results = response.json().get("data", {})
        children = results.get("children", [])
        if not children:
            print("None")
            return

        for c in children:
            print(c.get("data", {}).get("title", ""))
    except ValueError:
        print("None")
