from langchain.tools import tool


@tool
def premium_estimator(
    age: int,
    coverage_amount: int,
    tenure: int,
    smoker: bool
) -> str:
    """
    Estimate insurance premium based on age, coverage, tenure and smoking status.
    """

    base_rate = 0.01

    annual_premium = coverage_amount * base_rate

    if age > 40:
        annual_premium *= 1.2

    if smoker:
        annual_premium *= 1.3

    monthly_premium = annual_premium / 12

    return (
        f"Coverage Amount: ₹{coverage_amount:,}\n"
        f"Tenure: {tenure} years\n"
        f"Annual Premium: ₹{annual_premium:,.0f}\n"
        f"Monthly Premium: ₹{monthly_premium:,.0f}"
    )