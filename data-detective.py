import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """
    clean_tweets = []
    for tweet in tweets:
        if not tweet.get('Text') or tweet['Text'].strip() == '':
            continue
        if not tweet.get('Likes') or tweet['Likes'].strip() == '':
            tweet['Likes'] = '0'
        if not tweet.get('Retweets') or tweet['Retweets'].strip() == '':
            tweet['Retweets'] = '0'
        tweet['Likes'] = int(tweet['Likes'])
        tweet['Retweets'] = int(tweet['Retweets'])
        clean_tweets.append(tweet)
    return clean_tweets

def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """
    if not tweets:
        return None
    viral_tweet = tweets[0]
    for tweet in tweets[1:]:
        if tweet['Likes'] > viral_tweet['Likes']:
            viral_tweet = tweet
    return viral_tweet

def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list 
    by 'Likes' in descending order. NO .sort() allowed!
    """
    sorted_tweets = tweets[:]
    n = len(sorted_tweets)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_tweets[j]['Likes'] < sorted_tweets[j + 1]['Likes']:
                sorted_tweets[j], sorted_tweets[j + 1] = sorted_tweets[j + 1], sorted_tweets[j]
    return sorted_tweets

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    keyword_lower = keyword.lower()
    matching_tweets = []
    for tweet in tweets:
        if keyword_lower in tweet['Text'].lower():
            matching_tweets.append(tweet)
    return matching_tweets

if __name__ == "__main__":
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    clean_dataset = clean_data(dataset)
    print(f"Cleaned dataset has {len(clean_dataset)} tweets.\n")
    viral = find_viral_tweet(clean_dataset)
    if viral:
        print(f"Most viral tweet ({viral['Likes']} likes):")
        print(f"  {viral['Text']}\n")
    sorted_tweets = custom_sort_by_likes(clean_dataset)
    print("Top 10 tweets by likes:")
    for i, tweet in enumerate(sorted_tweets[:10]):
        print(f"  {i+1}. ({tweet['Likes']} likes) {tweet['Text'][:60]}...")
    print()
    keyword = input("Enter a keyword to search: ")
    results = search_tweets(clean_dataset, keyword)
    print(f"Found {len(results)} tweets containing '{keyword}'.")