#!/bin/bash

echo "--- Top 5 Most Active Users ---"
python3 -c "
import csv
with open('twitter_dataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    users = {}
    for row in reader:
        u = row['Username']
        if u not in users:
            users[u] = 0
        users[u] = users[u] + 1
    top = []
    for user, count in users.items():
        top.append((count, user))
    for i in range(len(top)):
        for j in range(0, len(top) - i - 1):
            if top[j][0] < top[j+1][0]:
                top[j], top[j+1] = top[j+1], top[j]
    for count, user in top[:5]:
        print(f'  {count} {user}')
"
