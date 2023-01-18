#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author}")
    except IndexError:
        pass
