# test_agent.py
from agent_sdk import Agent, Tool # Replace with your actual SDK's imports
from github_skill import get_repo_stats

# 1. Wrap your function into a Tool Claude can understand
repo_tool = Tool(
    name="get_repo_stats",
    description="Fetches the description and star count for a public GitHub repository. Input MUST be in 'owner/repo' format.",
    func=get_repo_stats
)

# 2. Spin up a local mock agent 
mock_agent = Agent(
    model="claude-3", 
    tools=[repo_tool]
)

# 3. Fire a prompt at it!
print("Asking Claude...")
response = mock_agent.run("Can you tell me how many stars the 'psf/requests' library has on GitHub?")

print("\n--- Claude's Response ---")
print(response)