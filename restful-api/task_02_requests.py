#!/usr/bin/python3
import requests
import csv

URL = "https://www.w3schools.com/python/ref_requests_get.asp"

def fetch_and_print_posts():
    obj = requests.get(URL)
    print(f"Status code: {obj.status_code}")
    
    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = []
        for post in posts:
            structured_posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(structured_posts)
