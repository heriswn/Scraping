import requests

url = 'https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&cd=HBgJSWR1bCBBZGhhGCRhNTBiZjllZS03MGRmLTQxMzYtYmExNy1jMzA5NjRmZWJhMTcAAA%3D%3D&q=%22Idul%20Adha%22&vertical=trends&count=20&query_source=trend_click&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel'

header = {
    'authority': 'twitter.com',
    'method': 'GET',
    'path': '/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&cd=HBgJSWR1bCBBZGhhGCRhNTBiZjllZS03MGRmLTQxMzYtYmExNy1jMzA5NjRmZWJhMTcAAA%3D%3D&q=%22Idul%20Adha%22&vertical=trends&count=20&query_source=trend_click&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cookie': 'dnt=1; kdt=wqq6M78epdmcxrY57YtVWgk5a7VKxdxM94e7NN5C; remember_checked_on=1; _sl=1; ct0=3f294a39c57a1b87e0cc6608334c7f84; gt=1410854972044890113; _twitter_sess=BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'x-csrf-token': '3f294a39c57a1b87e0cc6608334c7f84',
    'x-guest-token': '1410854972044890113',
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'en',
    #'content-length': '14604',
    #'content-type': 'application/json;charset=utf-8'
}

r = requests.get(url, headers=header).json()
tweets = r['globalObjects']
print(tweets)