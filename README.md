# Lab 2 - Social Media Data Detective

## Overview
This project analyzes a large Twitter dataset using Python and Bash. It cleans messy data, finds viral tweets, sorts by likes, and searches by keyword.

## File Structure
```
lab2_quagrainie1/
├── data-detective.py       # Main Python script with all 4 quests
├── feed-analyzer.sh        # Bash script to find top 5 most active users
├── twitter_dataset.csv     # Dataset used for testing
└── README.md               # Project documentation
```

## How to Run

### Python Script
python3 data-detective.py
When prompted, enter a search word for Quest 4.

### Shell Script
bash feed-analyzer.sh

## How It Works
- **Quest 1:** Cleans missing or empty fields in the dataset
- **Quest 2:** Finds the most liked tweet using a manual loop
- **Quest 3:** Sorts tweets by likes using Bubble Sort
- **Quest 4:** Searches tweets by a user-entered keyword

## How the Sorting Algorithm Works
The sorting algorithm used is Bubble Sort. It works by repeatedly comparing two adjacent tweets and swapping them if the left one has fewer likes than the right one. This process repeats until the entire list is ordered from highest to lowest likes.
