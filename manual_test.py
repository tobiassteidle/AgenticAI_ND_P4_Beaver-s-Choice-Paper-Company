from project_starter import MultiAgentWorkflow

multi_agent_workflow = MultiAgentWorkflow()

sample_request = """
    Are the following paper supplies available for the upcoming ceremony?
    - 2000 sheets of A4 glossy paper
    - 1500 sheets of A3 matte paper
    - 1000 sheets of cardstock in assorted colors
    
    Please confirm the availability and provide the expected delivery date.
"""

sample_request2 = """
I would like to request the following paper supplies for the ceremony: 
- 1000 sheets of A4 glossy paper
I need these supplies delivered by April 15, 2025. Thank you. (Date of request: 2025-04-01)
"""


response = multi_agent_workflow.run(sample_request2)

print(response)
