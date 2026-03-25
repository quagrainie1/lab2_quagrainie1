import csv

tweets = []

with open("twitter_dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tweets.append(row)

print(f"Total rows loaded: {len(tweets)}")

# Quest 1: Data Cleaning
def clean_data(data):
    cleaned = []
    fixed = 0

    for tweet in data:
        # remove tweet if Text is missing
        if not tweet["Text"] or tweet["Text"].strip() == "":
            fixed += 1
            continue

        # replace missing Likes or Retweets with 0
        if not tweet["Likes"] or tweet["Likes"].strip() == "":
            tweet["Likes"] = "0"
            fixed += 1

        if not tweet["Retweets"] or tweet["Retweets"].strip() == "":
            tweet["Retweets"] = "0"
            fixed += 1

        cleaned.append(tweet)

    print(f"Bad rows fixed or removed: {fixed}")
    return cleaned

tweets = clean_data(tweets)
print(f"Rows after cleaning: {len(tweets)}")











# Quest 2: Find the viral post (no max() allowed)
def find_most_liked(data):
    most_liked = data[0]

    for tweet in data:
        if int(tweet["Likes"]) > int(most_liked["Likes"]):
            most_liked = tweet

    print("\n--- Most Liked Tweet ---")
    print(f"Username: {most_liked['Username']}")
    print(f"Likes: {most_liked['Likes']}")
    print(f"Text: {most_liked['Text']}")

find_most_liked(tweets)





# Quest 3: Custom bubble sort, top 10 most liked
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




   # Quest 4: Search tweets by keyword
def search_tweets(data):
    word = input("\nEnter a search word: ")
    results = []

    for tweet in data:
        if word.lower() in tweet["Text"].lower():
            results.append(tweet)

    print(f"\nFound {len(results)} tweets containing '{word}'")
    for tweet in results:
        print(f"- {tweet['Username']}: {tweet['Text'][:80]}")

search_tweets(tweets) 