# github_skill.py
import requests

def get_repo_stats(repo_name: str) -> str:
    """Fetches the description and star count for a GitHub repository (e.g., 'torvalds/linux')."""
    url = f"https://api.github.com/repos/{repo_name}"
    
    # We add headers to ask GitHub for a JSON response
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        stars = data.get("stargazers_count", 0)
        desc = data.get("description", "No description provided.")
        return f"Repo '{repo_name}' has {stars} stars. Description: {desc}"
    elif response.status_code == 404:
        return f"Could not find a repository named '{repo_name}'."
    else:
        return f"Error fetching data: HTTP {response.status_code}"