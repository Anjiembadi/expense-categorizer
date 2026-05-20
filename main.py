from prompt import prompt_template
from model import get_model
from parser import parse_output

def categorize_expense(description: str):
    model = get_model()
    prompt = prompt_template.format(expense_description=description)
    response = model.invoke(prompt)
    result = parse_output(response.content)
    return result

if __name__ == "__main__":
    test_cases = [
        "Paid monthly electricity bill",
        "bought groceries",
        "uber ride",
        "paid bill",
        "bought a Louis Vuitton bag",
        "Netflix subscription"
    ]
    for case in test_cases:
        out = categorize_expense(case)
        print(f"\nInput: {case}")
        print(f"Category: {out.expense_category}")
        print(f"Type: {out.expense_type}")
        print(f"Note: {out.confidence_note}")