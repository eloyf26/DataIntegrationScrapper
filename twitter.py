import tweepy
import re

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'', text)

def get_tweets (names_arr):
    # bearer_token = "AAAAAAAAAAAAAAAAAAAAAN%2FrhwEAAAAAxWzzpKXFRTdnfa0QD6DnMKRWheo%3DmLftaCklYzgSQK8UsoEokYli24jCTW2WstyJx05q9muJFyg3My"
    # api_key = "cf8HBZgWozeKZSKNYm0Pw9RLU"
    # api_secret = "0dYpmQwswBMQrGGD0FCNqqP2Vk94ixBMOYxfVMZy600DAm5EkT"

    # access_token = "dataint123@gmail.com"
    # access_token_secret = "DVtweet1234"

    bearer_token = "AAAAAAAAAAAAAAAAAAAAALvViAEAAAAAeqD7f5TvaZYuGmy88c4cr6SEbZM%3DehLrsemoqRSc8EUQVCd6XFEZrYK2HFxgyoqDoZ75apLvPzjDU1"

    api_key = "Rvbku5TcDaKznwWTrCTHGP1Np"
    api_secret = "JciEJzigs15DvKMkbdNSGemml8vKY0ryD06tL2Hpd4pTYZUYmy"

    access_token = "1577967285679132674-rimcs4oZlU1mYRT1nyL6r371PhHQlh"
    access_token_secret = "X8FCG0UVMUtWZEJWz1vHyGnq9nR2qBdZhJxpzAYktr77a"

    client = tweepy.Client(bearer_token)

    all_tweets = []

    for place in names_arr:

        place_tweets = []

        title = f'\"{place[0]}\"'
        query = f'{title} -is:retweet lang:es'

        #print (query)

        place_tweets.append(place[0])

        response = client.search_recent_tweets(query, max_results = 10, tweet_fields = ['public_metrics'])
        # print(tweet.text)

        # print(response.meta)

        tweets = response.data

        recap_tweets = []
        # Each Tweet object has default ID and text fields
        try:
            for tweet in tweets:
                single_tweet = []
                #print("-----------------------------------------------------------------------")
                single_tweet.append(tweet.id)
                single_tweet.append(deEmojify(tweet.text))
                likes = tweet['public_metrics']['like_count']
                single_tweet.append(likes)
                retweets = tweet['public_metrics']['retweet_count']
                single_tweet.append(retweets)

                recap_tweets.append(single_tweet)

            place_tweets.append(recap_tweets)
            all_tweets.append(place_tweets)
        except:
            single_tweet = [None, "No recent tweets found", None, None]
            recap_tweets.append(single_tweet)
            place_tweets.append(recap_tweets)
            all_tweets.append(place_tweets)

    return all_tweets