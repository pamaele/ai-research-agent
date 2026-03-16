from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool


load_dotenv()

class Response(BaseModel):
    topic: str
    summary: str
    source: list[str]
    tools_used: list[str]
    tokens_in: int
    tokens_out: int


llm = ChatOpenAI(model="gpt-4o-mini")
parser = PydanticOutputParser(pydantic_object=Response)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Follow these steps strictly:
            1. Research the user query using search or wiki tools.
            2. ALWAYS use the 'save_text_to_file' tool to save the gathered information to a file.
            3. Finally, wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools
)


agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("What can i help you research: ")
raw_response = agent_executor.invoke({"query" : query})


try:
    texto_salida = raw_response["output"]
    
  
    texto_salida = texto_salida.replace("```json", "").replace("```", "").strip()
    
    structured_response = parser.parse(texto_salida)
    
    print("\n--- RESULTADO FINAL ---")
    print(structured_response)
    
except Exception as e:
    print(f"Error parsing response: {e}")
    print(f"Raw Response: {raw_response}")