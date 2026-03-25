#!/usr/bin/python3
import csv

# open the csv file and load all rows into a list
tweets = []

try:
    with open("twitter_dataset.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tweets.append(row)

    if len(tweets) == 0:
        print("The file has no data to work with.")
        exit()

except FileNotFoundError:
    print("Could not find twitter_dataset.csv, make sure the file is in the same folder.")
    exit()

print(f"Rows loaded: {len(tweets)}")


# step 1: go through the list and fix or remove bad rows
def fix_tweets(data):
    cleaned = []
    fixed = 0

    for tweet in data:
        if not tweet["Text"] or tweet["Text"].strip() == "":
            fixed += 1
            continue

        if not tweet["Likes"] or tweet["Likes"].strip() == "":
            tweet["Likes"] = "0"
            fixed += 1

        if not tweet["Retweets"] or tweet["Retweets"].strip() == "":
            tweet["Retweets"] = "0"
            fixed += 1

        cleaned.append(tweet)

    print(f"Total problems found and fixed: {fixed}")
    return cleaned


tweets = fix_tweets(tweets)
print(f"Rows after cleanup: {len(tweets)}")


# step 2: find the tweet with the most likes by looping through manually
def get_top_tweet(data):
    if len(data) == 0:
        print("List is empty, nothing to search.")
        return

    top = data[0]

    for tweet in data:
        if int(tweet["Likes"]) > int(top["Likes"]):
            top = tweet

    print("\n--- Top Tweet by Likes ---")
    print(f"Username: {top['Username']}")
    print(f"Likes: {top['Likes']}")
    print(f"Text: {top['Text']}")


get_top_tweet(tweets)


# step 3: use bubble sort to order tweets from highest to lowest likes
def sort_by_likes(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int(data[j]["Likes"]) < int(data[j + 1]["Likes"]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


sorted_tweets = sort_by_likes(tweets)
top10 = sorted_tweets[:10]

print("\n--- Top 10 Tweets ---")
for i, tweet in enumerate(top10):
    print(f"{i + 1}. {tweet['Username']} - Likes: {tweet['Likes']} - {tweet['Text'][:50]}")


# step 4: ask the user for a word and find all tweets that contain it
def keyword_search(data):
    word = input("\nType a word to search for: ")

    if word.strip() == "":
        print("You did not type anything.")
        return

    results = []

    for tweet in data:
        if word.lower() in tweet["Text"].lower():
            results.append(tweet)

    print(f"\n{len(results)} tweets found containing '{word}'")

    if len(results) == 0:
        print("No tweets matched your search.")
    else:
        for tweet in results:
            print(f"- {tweet['Username']}: {tweet['Text'][:80]}")


keyword_search(tweets)
