import os
import tweepy
import numpy as np


def get_tweets (names_arr):
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAN%2FrhwEAAAAAxWzzpKXFRTdnfa0QD6DnMKRWheo%3DmLftaCklYzgSQK8UsoEokYli24jCTW2WstyJx05q9muJFyg3My"

    api_key = "cf8HBZgWozeKZSKNYm0Pw9RLU"
    api_secret = "0dYpmQwswBMQrGGD0FCNqqP2Vk94ixBMOYxfVMZy600DAm5EkT"

    access_token = "dataint123@gmail.com"
    access_token_secret = "DVtweet1234"



    client = tweepy.Client(bearer_token)

    all_tweets = []

    for place in names_arr:

        place_tweets = []

        title = f'\"{place[0]}\"'
        query = f'{title} -is:retweet lang:es'

        print (query)

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
                # print("-----------------------------------------------------------------------")
                single_tweet.append(tweet.id)
                single_tweet.append(tweet.text)
                likes = tweet['public_metrics']['like_count']
                single_tweet.append(likes)
                retweets = tweet['public_metrics']['retweet_count']
                single_tweet.append(retweets)

                recap_tweets.append(single_tweet)

            place_tweets.append(recap_tweets)
            all_tweets.append(place_tweets)
        except:
            all_tweets.append("No recent tweets found")

    return all_tweets

