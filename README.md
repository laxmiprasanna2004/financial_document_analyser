# financial_document_analyser
# Financial Multi-Agent System using CrewAI
## 🐞 Bugs Identified and Fixes

### Bug 1: LLM Not Initialized Properly
Issue:
`llm = llm` was used without definition.

Fix:
Initialized LLM properly:
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4", temperature=0.7)
### Bug 2: Missing API Key
Issue:
OpenAI API key was not loaded.

Fix:
Added dotenv configuration:
from dotenv import load_dotenv
load_dotenv()
### Bug 3: Crew Not Executed
Issue:
crew.kickoff() was not called.

Fix:
Added execution block in main.py
## ⚙️ Setup Instructions

### Step 1: Clone Repository
git clone https://github.com/your-username/repo-name.git
cd repo-name

### Step 2: Create Virtual Environment
python -m venv venv
source venv/bin/activate  (Mac/Linux)
venv\Scripts\activate     (Windows)

### Step 3: Install Dependencies
pip install -r requirements.txt

### Step 4: Add Environment Variables
Create .env file:
OPENAI_API_KEY=your_api_key_here

### Step 5: Run the Project
python main.py
## 🚀 Usage

Modify the query inside main.py:

query = "Should I invest in Tesla stock?"

Run:
python main.py

The agent will analyze and return a response.
## 📡 API Documentation

### Agent Class
Parameters:
- role: Defines agent identity
- goal: Defines objective
- tools: List of tools assigned
- verbose: Enables reasoning logs

### Task Class
Parameters:
- description: Task details
- agent: Assigned agent

### Crew Class
Methods:
- kickoff(): Executes workflow
## 🖥 Example Output

Senior Financial Analyst is analyzing the query...
Using search tool...
Final Recommendation:
Based on current market trends...
