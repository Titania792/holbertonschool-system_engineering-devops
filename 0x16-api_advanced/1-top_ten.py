#!/usr/bin/python3
""" Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit """
import requests


def top_ten(subreddit):
    """ If not a valid subreddit, print None """
    try:
        api_url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
            subreddit)
        response = requests.get(
            api_url, headers={"User-Agent": "Mozilla/5.0"})
        response = response.json()['data']['children']
        for title in response:
            print(title['data']['title'])
    except Exception:
        print(None)
