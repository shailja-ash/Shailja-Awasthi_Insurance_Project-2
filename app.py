from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#add tools
from tools.needs_assessment import needs_assessment
from tools.policy_comparison import policy_comparison
from tools.premium_estimator import premium_estimator

from prompts.few_shot_prompt import few_shot_prompt


from prompt_loader import load_system_prompt
from data.products import PRODUCTS

from logs.logger import log_interaction
print("APP.PY LOADED")
load_dotenv()



SYSTEM_PROMPT = load_system_prompt(PRODUCTS)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1
)

print("========== SYSTEM PROMPT ==========")
#print(SYSTEM_PROMPT)
print("===================================")



insurance_chain = few_shot_prompt | llm.with_retry() | StrOutputParser()

def askllm(user_prompt):

    user_text = user_prompt.lower()   
    print("USER INPUT:", user_prompt)

    if "compare" in user_text:
        print("COMPARE TOOL CALLED")

        tool_response = policy_comparison.invoke(
            {
                 
                "policy1_name": "HDFC Ergo",
                "policy1_premium": 16800,
                "policy2_name": "Star Health",
                "policy2_premium": 18400
            }
        )
        log_interaction(
             session_id="demo-session",
             user_input=user_prompt,
            response=tool_response
        )
        return tool_response

    elif "premium" in user_text:

        tool_response = premium_estimator.invoke(
            {
                "age": 32,
                "coverage_amount": 5000000,
                "tenure": 30,
                "smoker": False
            }
        )
        log_interaction(
             session_id="demo-session",
             user_input=user_prompt,
            response=tool_response
        )
        return tool_response

    elif "insurance" in user_text:

        tool_response =  needs_assessment.invoke(
            {
                "age": 32,
                "income": 1800000,
                "dependents": 1,
                "existing_cover": 5000000
            }
        )
        log_interaction(
             session_id="demo-session",
             user_input=user_prompt,
            response=tool_response
        )
        return tool_response

    try:
        response = insurance_chain.invoke(
            {
                "input": user_prompt
            }
        )

        log_interaction(
            session_id="demo-session",
            user_input=user_prompt,
            response=response
        )
        return response

    except Exception as e:

        print(f"Error occurred: {e}")

        return (
            "Sorry, I'm temporarily unable to process your request. "
            "Please try again in a few moments."
        )



