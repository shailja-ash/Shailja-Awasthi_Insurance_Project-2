import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
from tools.needs_assessment import needs_assessment


def test_needs_assessment():

    result = needs_assessment.invoke(
        {
            "age": 32,
            "income": 1800000,
            "dependents": 1,
            "existing_cover": 5000000
        }
    )

    assert result is not None