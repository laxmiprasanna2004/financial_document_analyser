## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier
from tools import search_tool, FinancialDocumentTool

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description="""
    Analyze the provided financial document carefully.
    Answer the user's query: {query} using only verified data from the document.
    If additional data is needed, clearly state the limitation.
    
    Provide:
    - Summary of key financial metrics
    - Revenue and profitability analysis
    - Notable trends
    - Potential risks based on actual data
    """,

    expected_output="""
    - Clear summary
    - Evidence-based analysis
    - No fabricated information
    - Transparent assumptions
    """,

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="""
    Based strictly on the financial document,
    provide a neutral investment perspective.
    
    Do not fabricate numbers.
    Do not recommend specific products unless supported by data.
    Highlight both risks and opportunities.
    
    User query: {query}
    """,

    expected_output="""
    - Evidence-based interpretation
    - Balanced investment considerations
    - Clear risk disclaimer
    - No speculative or fabricated claims
    """,

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="""
    Identify genuine financial risks found in the document.
    
    Consider:
    - Liquidity risk
    - Credit risk
    - Market exposure
    - Operational risk
    
    Do not exaggerate.
    Only report risks supported by document data.
    """,

    expected_output="""
    - Structured risk categories
    - Data-backed explanation
    - Practical mitigation suggestions
    - No invented risk models
    """,

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)
verification = Task(
    description="""
    Carefully review the file and determine whether it is a financial document.
    
    Identify:
    - Type of document
    - Key sections
    - Financial indicators
    
    If it is not financial, state that clearly.
    """,

    expected_output="""
    - Clear classification
    - Evidence-based reasoning
    - No assumptions
    """,

    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False
)
    