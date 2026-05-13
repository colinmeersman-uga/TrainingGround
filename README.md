# GitHub Repo Stats Skill & Local Testing Flow

This directory contains the code for a new agent skill that fetches statistics for public GitHub repositories. It also establishes a local testing workflow to verify the logic and AI integration before deploying the skill into the main Slackbot harness (`agent_listener.py`).

## 📁 Files Created

* **`github_skill.py`**: Contains the core Python logic. It makes a direct HTTP request to the GitHub API to fetch a repository's description and star count. It is completely decoupled from the Agent SDK and Slack.
* **`scratchpad.py`**: A manual testing script to verify the core logic works independently. It tests `github_skill.py` against both a valid and an invalid repository to ensure the raw Python code executes correctly.
* **`test_agent.py`**: An integration test script. This wraps the core logic in an Agent Tool format and runs a mock, local LLM to verify that the model understands the tool's description, knows when to use it, and can successfully parse the output.

## 🚀 How to Test Locally

**1. Test the Core Logic** Run the scratchpad to ensure the GitHub API request works:
```bash
python scratchpad.py
