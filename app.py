from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# GitHub API Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "owner/repo"  # Replace with your repository (e.g., "username/repository")

@app.route('/github-stats', methods=['GET'])
def github_stats():
    url = f"https://api.github.com/repos/{REPO_NAME}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return jsonify({
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "issues": data.get("open_issues_count", 0)
    })

# YouTube API Configuration
YOUTUBE_API_KEY = os.getenv("AIzaSyASpTib6NHFqpCy5EZoSgAbmrxG-z8_NDo")
CHANNEL_ID = "UCy4exXeg1PckAaWuPM6kjEw"  # Replace with your YouTube channel ID

@app.route('/youtube-stats', methods=['GET'])
def youtube_stats():
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    stats = data["items"][0]["statistics"]
    return jsonify({
        "views": stats.get("viewCount", 0),
        "subscribers": stats.get("subscriberCount", 0),
        "videos": stats.get("videoCount", 0)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
