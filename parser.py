import json
from pydantic import BaseModel

class ExpenseOutput(BaseModel):
    expense_category: str
    expense_type: str
    confidence_note: str

def parse_output(raw_text: str) -> ExpenseOutput:
    try:
        clean = raw_text.strip().strip("```json").strip("```").strip()
        data = json.loads(clean)
        return ExpenseOutput(**data)
    except Exception as e:
        return ExpenseOutput(
            expense_category="Miscellaneous",
            expense_type="Unknown",
            confidence_note=f"Could not parse response: {str(e)}"
        )