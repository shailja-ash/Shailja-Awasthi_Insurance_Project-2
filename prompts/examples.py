examples = [

    {
        "input": "I’m 32, married, one kid, earning 18L. What insurance do I need?",
        "output": """
Based on your profile:
(1) Term Life: ₹1Cr cover
(2) Health: ₹10L family floater
(3) Critical Illness rider: ₹25L
Total annual premium: ~₹34,800.
Highest priority gap: no life cover.
"""
    },

    {
        "input": "Compare HDFC Ergo and Star Health for a 10L family plan.",
        "output": """
HDFC Ergo Optima Secure — Premium ₹16,800, CSR 95%.
Star Family Health Optima — Premium ₹18,400, CSR 88%.
Recommendation: HDFC Ergo.
"""
    },

    {
        "input": "How much would a 50L term plan cost me?",
        "output": """
ICICI iProtect — ₹6,200/yr
HDFC Click2Protect — ₹6,800/yr
Max Life Smart Secure Plus — ₹6,450/yr
"""
    }

]