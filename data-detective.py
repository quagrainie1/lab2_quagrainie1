#!/usr/bin/python3
import csv

# Load tweets from CSV file into a list
tweets = []

try:
    with open("twitter_dataset.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tweets.append(row)

    if len(tweets) == 0:
        print("The CSV file is empty. No data to process.")
        exit()

except FileNotFoundError:
    print("Error: twitter_dataset.csv not found. Please add the file and try again.")
    exit()

print(f"Total rows loaded: {len(tweets)}")


# Quest 1: Clean the data
# Remove tweets with missing Text, replace missing Likes/Retweets with 0
def clean_data(data):
    cleaned = []
    fixed = 0

    for tweet in data:
        # Skip tweet if Text is missing
        if not tweet["Text"] or tweet["Text"].strip() == "":
            fixed += 1
            continue

        # Replace missing Likes with 0
        if not tweet["Likes"] or tweet["Likes"].strip() == "":
            tweet["Likes"] = "0"
            fixed += 1

        # Replace missing Retweets with 0
        if not tweet["Retweets"] or tweet["Retweets"].strip() == "":
            tweet["Retweets"] = "0"
            fixed += 1

        cleaned.append(tweet)

    print(f"Bad rows fixed or removed: {fixed}")
    return cleaned


tweets = clean_data(tweets)
print(f"Rows after cleaning: {len(tweets)}")


# Quest 2: Find the tweet with the highest number of Likes
# No max() used - manually loop and track the highest
def find_most_liked(data):
    if len(data) == 0:
        print("No data available.")
        return

    most_liked = data[0]

    for tweet in data:
        if int(tweet["Likes"]) > int(most_liked["Likes"]):
            most_liked = tweet

    print("\n--- Most Liked Tweet ---")
    print(f"Username: {most_liked['Username']}")
    print(f"Likes: {most_liked['Likes']}")
    print(f"Text: {most_liked['Text']}")


find_most_liked(tweets)


# Quest 3: Sort tweets by Likes using Bubble Sort (no .sort() or sorted())
# Bubble sort repeatedly swaps adjacent elements if they are in the wrong order
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int(data[j]["Likes"]) < int(data[j + 1]["Likes"]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


sorted_tweets = bubble_sort(tweets)
top10 = sorted_tweets[:10]

print("\n--- Top 10 Most Liked Tweets ---")
for i, tweet in enumerate(top10):
    print(f"{i + 1}. {tweet['Username']} - Likes: {tweet['Likes']} - {tweet['Text'][:50]}")


# Quest 4: Search tweets by keyword entered by the user
# Loops through all tweets and appends matches to a new list
def search_tweets(data):
    word = input("\nEnter a search word: ")

    if word.strip() == "":
        print("No search word entered.")
        return

    results = []

    for tweet in data:
        if word.lower() in tweet["Text"].lower():
            results.append(tweet)

    print(f"\nFound {len(results)} tweets containing '{word}'")

    if len(results) == 0:
        print("No matching tweets found.")
    else:
        for tweet in results:
            print(f"- {tweet['Username']}: {tweet['Text'][:80]}")


search_tweets(tweets)