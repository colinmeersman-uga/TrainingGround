# scratchpad.py
from github_skill import get_repo_stats

print("--- Testing a real repo ---")
print(get_repo_stats("pallets/flask"))

print("\n--- Testing a fake repo ---")
print(get_repo_stats("this-is-a-fake-user/definitely-not-real-123"))