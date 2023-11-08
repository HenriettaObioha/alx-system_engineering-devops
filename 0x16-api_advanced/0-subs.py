#!/usr/bin/python3
<<<<<<< HEAD
"""Function to query subscribers on a given Reddit subreddit."""
=======
"""Function that queries subscribers on a given Reddit subreddit."""
>>>>>>> 227e74ab74b712ed197bd092b7d5003d1fdd48dd
import requests


def number_of_subscribers(subreddit):
<<<<<<< HEAD
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
=======
    """Returns the total number of subscribers ona a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
	"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
	return 0
    results = response.json().get("data")
    return resilts.get("subscribers")
>>>>>>> 227e74ab74b712ed197bd092b7d5003d1fdd48dd
