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
from tools.premium_estimator import premium_estimator


def test_premium_estimator():

    result = premium_estimator.invoke(
        {
            "age": 32,
            "coverage_amount": 5000000,
            "tenure": 30,
            "smoker": False
        }
    )

    assert result is not None