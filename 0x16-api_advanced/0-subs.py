#!/usr/bin/python3
""" Function that queries the Reddit API and returns the number of
subscribers for a given subreddit """
import requests


def number_of_subscribers(subreddit):
    """ If not a valid subreddit, return 0 """
    try:
        api_url = 'http://reddit.com/r/{}/about'.format(subreddit)
        response = requests.get(
            api_url, headers={"User-Agent": "Mozilla/5.0"})
        return response.json()['data']['suscribers']
    except Exception:
        return 0
