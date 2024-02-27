"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
            {
        "input": [2, [["AM", 7.00, 10.00], ["RS", 7.01, 10.00]]],
        "answer": ["AM"]
    },
    {
        "input": [3, [["SP", 4.90, 5.80], ["RJ", 4.70, 5.70], ["PR", 4.60, 5.60]]],
        "answer": ["*"]
    },
    {
        "input": [4, [["SC", 5.20, 5.72], ["MT", 4.22, 6.10], ["AL", 5.55, 6.20], ["GO", 4.30, 6.25]]],
        "answer": ["MT", "GO"]
    }

    ]
}
