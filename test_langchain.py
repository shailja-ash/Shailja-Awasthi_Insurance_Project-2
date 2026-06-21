from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from prompts.few_shot_prompt import few_shot_prompt

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1
)

prompt_text = few_shot_prompt.format(
    input="Compare two health insurance plans"
)

response = llm.invoke(prompt_text)

print(response.content)