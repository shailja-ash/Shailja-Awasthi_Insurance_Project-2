# Coverwise Insurance Advisor

A GenAI-powered insurance advisor chatbot built using OpenAI GPT-4o-mini, Streamlit, and Pydantic Structured Outputs.

The chatbot helps users understand, compare, and select insurance plans based on their needs while enforcing domain-specific guardrails and returning validated structured responses.

---

# Features

* Health Insurance recommendations
* Term Insurance information
* Car Insurance guidance
* Home Insurance guidance
* Guardrails to restrict responses to insurance-related questions only
* Prompt engineering using external Markdown prompt templates
* Product catalog maintained separately from application code
* Streamlit-based conversational interface
* OpenAI GPT-4o-mini integration
* Structured JSON outputs using Pydantic
* Response schema validation

# Additional Features

* FastAPI backend with REST APIs
* Swagger/OpenAPI documentation
* Semantic Example Selection using FAISS and OpenAI Embeddings
* LangChain FewShotPromptTemplate
* Needs Assessment Tool
* Policy Comparison Tool
* Premium Estimator Tool
* Structured JSON logging
* Retry logic with graceful fallback handling
* LangSmith observability and tracing

---

# Requirement Coverage

| Requirement                     | Status |
| ------------------------------- | ------ |
| LangChain-based architecture    | ✅      |
| FastAPI backend                 | ✅      |
| Streamlit frontend              | ✅      |
| Few-shot prompting              | ✅      |
| Semantic example selection      | ✅      |
| Needs Assessment Tool           | ✅      |
| Policy Comparison Tool          | ✅      |
| Premium Estimator Tool          | ✅      |
| Pydantic structured outputs     | ✅      |
| Retry logic                     | ✅      |
| Fallback handling               | ✅      |
| Structured JSON logging         | ✅      |
| LangSmith tracing               | ✅      |
| Environment-based configuration | ✅      |
| Swagger/OpenAPI documentation   | ✅      |
| Session memory (Streamlit)      | ✅      |


# Project Structure

STREAMLIT_DEMO/
│
├── api.py
├── app.py
├── prompt_loader.py
├── stremlit_demo.py
├── requirements.txt
├── .env
├── README.md
│
├── data/
│   └── products.py
│
├── prompts/
│   ├── insurance_system_prompt.md
│   ├── examples.py
│   ├── example_selector.py
│   └── few_shot_prompt.py
│
├── tools/
│   ├── needs_assessment.py
│   ├── policy_comparison.py
│   └── premium_estimator.py
│
├── logs/
│   ├── logger.py
│   └── interactions.jsonl
│
├── screenshots/
│   ├── langsmith_traces.png
│
└── tests/
├── test_needs_assessment.py
├── test_policy_comparison.py
└── test_premium_estimator.py

---

# Folder Description

| File / Folder                      | Purpose                                   |
| ---------------------------------- | ----------------------------------------- |
| data/products.py                   | Stores insurance product catalog          |
| prompts/insurance_system_prompt.md | Externalized system prompt                |
| prompt_loader.py                   | Loads prompt templates from markdown      |
| app.py                             | OpenAI integration and chatbot logic      |
| streamlit_demo.py                  | Streamlit chat interface                  |
| .env                               | Stores API keys and environment variables |
| ReadMe.md                          | Project documentation                     |


# Architecture

User
↓
Streamlit UI / FastAPI API
↓
Request Processing
↓
Tool Routing Layer
↓
Semantic Example Selector (FAISS + OpenAI Embeddings)
↓
FewShotPromptTemplate
↓
GPT-4o-mini
↓
Pydantic Validation
↓
Structured Response
↓
JSON Logging
↓
LangSmith Tracing


# API Endpoints

| Endpoint | Method | Description                                       |
| -------- | ------ | ------------------------------------------------- |
| /chat    | POST   | Accepts user message and returns chatbot response |
| /reset   | POST   | Placeholder endpoint for future backend session         reset.                Current conversational memory is maintained in                     Streamlit session state.                     |
| /health  | GET    | Returns application health status and uptime      |
| /        | GET    | Home endpoint                                     |


---

# Unit Testing

The project includes unit tests for all custom tools:

* test_needs_assessment.py
* test_policy_comparison.py
* test_premium_estimator.py

Tests validate:

* Coverage recommendation logic
* Policy comparison results
* Premium estimation calculations
* Expected output structure


# Supported Insurance Products

## Health Insurance

* Bronze Health Plan
* Silver Health Plan
* Gold Health Plan

## Term Insurance

* Life Secure Term Plan

## Car Insurance

* Car Protect Plan

## Home Insurance

* Home Secure Plus

---

# Structured Output Validation

The application uses OpenAI Structured Outputs and Pydantic models to ensure responses follow a predictable schema.



## Response Schema

```python
class InsuranceBotResponse(BaseModel):
    answer_type: Literal[
        "recommendation",
        "comparison",
        "information",
        "clarifying_question",
        "out_of_scope",
    ]

    product_category: Literal[
        "health",
        "term",
        "car",
        "home",
        "none",
    ]

    greeting: str
    final_response: str
    recommended_plan: Optional[str]
    reasons: List[str]
    coverage: Optional[str]
    premium: Optional[str]
```

## Benefits

* Strong schema validation
* Consistent response structure
* Type-safe AI outputs
* Easier frontend integration
* Better error handling
* Reduced risk of malformed responses

---

# Technical Highlights

* OpenAI GPT-4o-mini integration
* Streamlit chat interface
* Pydantic structured outputs
* OpenAI response parsing
* Prompt externalization using Markdown
* Product catalog externalization
* Session-based conversation memory
* Environment variable management using python-dotenv


---

# LangSmith Observability

LangSmith was used to trace:

- Prompt execution
- Few-shot example selection
- Tool execution
- LLM responses

Trace screenshots are available under:

screenshots/

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd STREAMLIT_DEMO
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file in the project root.

```text
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=Insurance-Copilot
```

---

# Run the Application

```bash
streamlit run stremlit_demo.py
```

The application will launch locally in your browser.


# Run the Swagger and use the url to open via browser
```bash
uvicorn api:app --reload
http://127.0.0.1:8000/docs
```

---
# Example Questions

## Health Insurance

* I am 25 years old and single. Which health insurance should I buy?
* I am married and have two children. Which health plan is suitable?
* Compare Bronze and Gold Health Plans.
* What are the available health insurance plans?

## Car Insurance

* I recently purchased a new car. Which insurance should I take?
* Tell me about the Car Protect Plan.

## Home Insurance

* What does Home Secure Plus cover?
* Do you provide home insurance?

## Term Insurance

* What term insurance plans do you offer?
* Tell me about Life Secure Term Plan.

---

# Guardrails

The chatbot only answers questions related to:

* Health Insurance
* Term Insurance
* Car Insurance
* Home Insurance

For unrelated questions, the chatbot responds appropriately and prevents out-of-scope discussions.

Examples:

* Who is the Prime Minister of India?
* Write a Python program.
* Give me stock market advice.

These queries are intentionally rejected.

---

# Evaluation Approach

The chatbot can be evaluated on:

* Recommendation accuracy
* Product selection correctness
* Guardrail effectiveness
* Response formatting
* Structured output compliance
* Hallucination prevention

Evaluation

The chatbot was evaluated using an automated rubric-based evaluation framework.

Evaluation Coverage

The evaluation suite tests:

Insurance recommendations
Product comparisons
Information requests
Clarifying questions
Out-of-scope queries
Guardrail compliance
Structured JSON response validation
Scoring Criteria

Each test case is scored against:

Valid structured JSON output
Correct answer type classification
Correct product category identification
Correct plan recommendation
Coverage accuracy
Premium accuracy
Required content presence
Forbidden content absence
Greeting compliance
Out-of-scope handling
Evaluation Files
evaluate_coverwise_rubric.py
coverwise_eval_cases.json
evaluation_report.json
Running Evaluation
python evaluate_coverwise_rubric.py
Generated Report

Running the evaluation generates:

evaluation_report.json

The report includes:

Total test cases
Passed and failed cases
Overall accuracy percentage
Detailed scoring breakdown
Guardrail effectiveness checks
Structured output validation results

---

# Tech Stack

* Python 3.9
* LangChain
* OpenAI API
* GPT-4o-mini
* FastAPI
* Streamlit
* Pydantic
* FAISS
* OpenAI Embeddings
* LangSmith
* python-dotenv
* Uvicorn
* JSON Logging
* Git & GitHub

