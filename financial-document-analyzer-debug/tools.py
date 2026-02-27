## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import tools
from crewai_tools.tools.serper_dev_tool import SerperDevTool

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool():
    async def read_data_tool(self,path:str="data/sample.pdf")->str:
        loader=PyPDFLoader(path)
        docs=loader.load()

        full_report = ""

        for data in docs:
            # Clean and format the financial document data
            content = data.page_content.strip()
            
            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report

## Creating Investment Analysis Tool
class InvestmentTool:
    async def analyze_investment_tool(self, financial_document_data: str) -> str:
        
        # Clean formatting
        processed_data = " ".join(financial_document_data.split())

        # Example simple analysis (basic placeholder logic)
        if "profit" in processed_data.lower():
            return "Company shows profit indicators. Investment looks promising."
        elif "loss" in processed_data.lower():
            return "Company shows loss indicators. High risk investment."
        else:
            return "Insufficient financial indicators found."

## Creating Risk Assessment Tool
class RiskTool:
    async def create_risk_assessment_tool(self, financial_document_data: str) -> str:

        data = financial_document_data.lower()

        risk_keywords = ["debt", "loss", "decline", "liability"]

        risk_score = sum(keyword in data for keyword in risk_keywords)

        if risk_score >= 2:
            return "High Risk Investment"
        elif risk_score == 1:
            return "Moderate Risk Investment"
        else:
            return "Low Risk Investment"