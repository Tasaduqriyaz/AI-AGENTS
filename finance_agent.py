from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
load_dotenv()

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions='use tables to display information.',
    debug_mode=True,
)
agent.print_response("Summarize and the compare the analyst recommendations and fundamentals for TSLA and NVDA"
                     )
