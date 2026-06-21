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

from tools.policy_comparison import policy_comparison


def test_policy_comparison():

    result = policy_comparison.invoke(
        {
            "policy1_name": "HDFC Ergo",
            "policy1_premium": 16800,
            "policy2_name": "Star Health",
            "policy2_premium": 18400
        }
    )

    assert result is not None