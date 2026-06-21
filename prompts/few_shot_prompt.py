from langchain_core.prompts import (
    FewShotPromptTemplate,
    PromptTemplate
)

from prompts.example_selector import example_selector


example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="""
User: {input}

Assistant: {output}
"""
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="""
You are an expert insurance advisor.
Use the examples below as guidance.
""",
    suffix="""
User: {input}

Assistant:
""",
    input_variables=["input"]
)