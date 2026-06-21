from langchain.tools import tool


@tool
def needs_assessment(
    age: int,
    income: int,
    dependents: int,
    existing_cover: int
) -> str:
    """
    Analyze insurance needs and identify coverage gaps.
    """

    recommended_cover = income * 10

    gap = max(
        recommended_cover - existing_cover,
        0
    )

    return (
        f"Recommended cover: ₹{recommended_cover:,}. "
        f"Existing cover: ₹{existing_cover:,}. "
        f"Coverage gap: ₹{gap:,}."
    )