#!/bin/bash

echo "--- Top 5 Most Active Users ---"
python3 -c "
import csv
with open('twitter_dataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    users = {}
    for row in reader:
        u = row['Username']
        users[u] = users.get(u, 0) + 1
    sorted_users = sorted(users.items(), key=lambda x: x[1], reverse=True)
    for user, count in sorted_users[:5]:
        print(f'  {count} {user}')
"
