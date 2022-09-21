#!/usr/bin/python3
""" Function that queries the Reddit API and returns the number of
subscribers for a given subreddit """
import requests


def number_of_subscribers(subreddit):
    """ If not a valid subreddit, return 0 """
    try:
        api_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        response = requests.get(
            api_url, headers={"User-Agent": "Mozilla/5.0"})
        return response.json()['data']['subscribers']
    except Exception:
        return 0
