from langchain.tools import tool


@tool
def policy_comparison(
    policy1_name: str,
    policy1_premium: int,
    policy2_name: str,
    policy2_premium: int
) -> str:
    """
    Compare two insurance policies and recommend the lower premium option.
    """

    if policy1_premium < policy2_premium:
        recommendation = policy1_name
    else:
        recommendation = policy2_name

    return (
        f"{policy1_name}: ₹{policy1_premium:,} per year\n"
        f"{policy2_name}: ₹{policy2_premium:,} per year\n\n"
        f"Recommended Policy: {recommendation}"
    )