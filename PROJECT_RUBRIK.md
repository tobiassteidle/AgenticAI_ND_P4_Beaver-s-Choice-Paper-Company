# Evaluation Criteria

Use this project evaluation guide to understand and assess the project requirements.

## Agent Workflow Diagram

| **Criteria**                                                                                               | **Submission Requirements**                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Illustrate the architecture of the multi-agent system, including agent responsibilities and orchestration. | - The workflow diagram includes all agents in the multi-agent system (maximum of five).<br>- Each agent has clearly defined responsibilities that do not overlap with others.<br>- The orchestration logic and data flow between agents is clear.  |
| Illustrate the interactions between agents and their tools, specifying the purpose of each tool.           | - The diagram depicts tools assigned to specific agents.<br>- Each tool's purpose and the helper function(s) it uses from the starter code are specified.<br>- The diagram shows interactions (e.g., input/output) between agents and their tools. |

## Multi-Agent System Implementation

| **Criteria**                                                                                                  | **Submission Requirements**                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Implement the multi-agent system with distinct orchestrator and worker roles, matching the submitted diagram. | - The architecture matches the agent workflow diagram.<br>- An orchestrator agent is present to delegate tasks.<br>- Distinct worker agents handle:<br>&nbsp;&nbsp;&nbsp;- Inventory management (e.g., stock checking, reorder decisions)<br>&nbsp;&nbsp;&nbsp;- Quoting (e.g., prices, discounts)<br>&nbsp;&nbsp;&nbsp;- Sales finalization (e.g., orders, database updates)<br>- One of the recommended frameworks is used (`smolagents`, `pydantic-ai`, `npcsh`). |
| Implement tools for agents using provided helper functions.                                                   | - Tools follow the conventions of the selected framework.<br>- All the following functions are used in at least one tool:<br>`create_transaction`, `get_all_inventory`, `get_stock_level`, `get_supplier_delivery_date`, `get_cash_balance`, `generate_financial_report`, `search_quote_history`.                                                                                                                                                                    |

## Evaluation and Reflection

| **Criteria**                                                    | **Submission Requirements**                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Evaluate the system using the dataset and document the results. | - The system is tested using `quote_requests_sample.csv`.<br>- Results are submitted in `test_results.csv` (or equivalent).<br>- Must demonstrate:<br>&nbsp;&nbsp;&nbsp;- ≥3 requests change the cash balance.<br>&nbsp;&nbsp;&nbsp;- ≥3 quote requests are fulfilled.<br>&nbsp;&nbsp;&nbsp;- Some requests remain unfulfilled (e.g., insufficient stock), with explanation or implication. |
| Reflect on the architecture, implementation, and evaluation.    | - Report explains the agent workflow diagram and architecture decisions.<br>- Discussion of `test_results.csv` and system strengths.<br>- Includes ≥2 suggestions for improvement or new features.                                                                                                                                                                                          |

## Industry Best Practices

| **Criteria**                                                           | **Submission Requirements**                                                                                                                                                                                       |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Provide transparent and explainable outputs for customer interactions. | - Customer-facing outputs contain all relevant request info.<br>- Reasoning for decisions is included where appropriate (e.g., discount, unfulfillable order).<br>- No sensitive internal data or PII is exposed. |
| Write clean, readable, modular, and well-commented code.               | - Naming conventions followed (`snake_case`, `PascalCase`).<br>- Includes comments and docstrings.<br>- Logic is modularized into separate components.                                                            |

## Suggestions to Make Your Project Stand Out

- Create a **customer agent** that uses request context to negotiate with the system.
- Implement a **terminal animation** that visualizes how the request is processed by different agents.
- Add a **business advisor agent** that reviews transactions and suggests operational improvements.

