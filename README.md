# 🧠 Munder Difflin Multi-Agent System Project

Welcome to the starter code repository for the **Munder Difflin Paper Company Multi-Agent System Project**!  
This repository provides all the tools and code you need to design, build, and test a modular multi-agent system that supports core business operations at a fictional paper company.

---

## 📌 Project Overview

📄 Please refer to [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) for a detailed description of the project goals and background.

## 🧭 Instructions

🛠️ Follow the step-by-step guidance in [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md) to complete the assignment.

## 🧪 Evaluation Criteria

📊 See [PROJECT_RUBRIK.md](PROJECT_RUBRIK.md) for details on how your solution will be graded.

## 📚 Solution Documentation

🔍 Find a complete breakdown of the architecture, agent roles, and design decisions in [SOLUTION_DOCUMENTATION.md](SOLUTION_DOCUMENTATION.md).

---

## 📦 What’s Included

The `project.zip` starter archive contains:

- `📄 project_starter.py`: Starter Python script where you’ll implement your agents.
- `📊 quotes.csv`: Historical quote data for your quoting logic.
- `📥 quote_requests.csv`: Customer request data for processing.
- `🧪 quote_requests_sample.csv`: Sample test scenarios.

---

## 🏢 Project Context

You've been hired as an AI consultant by **Munder Difflin Paper Company**, who wants to modernize its internal workflows.

They need a smart, modular **multi-agent system** that automates:

- 🧾 Inventory checks and restocking
- 💬 Quote generation based on real-world data
- 🚚 Order fulfillment and transaction processing

Your constraints:

- Use **no more than 5 agents**
- Agents must communicate entirely via **text-based interactions**
- Frameworks like `smolagents`, `pydantic-ai`, or `npcsh` are encouraged
- You'll be working with real tools like `sqlite3`, `pandas`, and **LLM prompting**

---

## 💻 Workspace Instructions

All starter files are available in your Udacity VS Code workspace.

📦 Be sure to install an agent framework before running the code.

---

## ⚙️ Local Setup Instructions

### 1️⃣ Install Dependencies

Ensure Python 3.8+ is installed. Then run:

```bash
pip install -r requirements.txt
```

### 2️⃣ Set API Key

Create a `.env` file and add your OpenAI-compatible API key:

```bash
UDACITY_OPENAI_API_KEY=your_openai_key_here
```

🔐 This project uses the proxy:  
`https://openai.vocareum.com/v1`

---

## ▶️ How to Run the Project

Once you’ve defined your agents (starting at `# "YOUR MULTI AGENT STARTS HERE"` in `template.py`):

1. Run the `run_test_scenarios()` function at the bottom of the script.
2. It will simulate customer request scenarios.
3. Your system should coordinate inventory checks, quote generation, and order processing.

📤 Output Includes:

- 🧠 Agent responses
- 💰 Cash balance updates
- 📦 Inventory changes
- 📑 Final financial report
- 📁 `test_results.csv` with logs

---

## 💡 Tips for Success

✅ Start with a **flow diagram** to plan agent roles.  
✅ Test each agent tool before combining them.  
✅ Always include **dates** in internal communications.  
✅ Provide **volume discounts** in quotes.  
✅ Use **exact item names** from the database.

---

## 📤 Submission Checklist

Make sure your submission includes:

1. ✅ Final `project_starter.py` or `template.py`
2. 🧩 Workflow diagram of agent architecture
3. 📝 `README.txt` or `design_notes.txt` explaining your approach
4. 📊 Test output files (e.g. `test_results.csv`)

---

🚀 Good luck building your intelligent agent team!
