from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from dotenv import load_dotenv
load_dotenv()

web_agent=Agent(
    name='web agent',
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions='always include sources',
)
fin_agent=Agent(
    name='finance agent',
    role='show financial data',
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions='display the information in the form of tables',
)
team_agent=Agent(
    team=[web_agent,fin_agent],
    model=Groq(id='llama-3.3-70b-versatile'),
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)
team_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA",stream=True)
