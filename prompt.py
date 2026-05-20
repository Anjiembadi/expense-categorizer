from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["expense_description"],
    template="""
You are an expense categorization assistant.

Given the expense description below, classify it and return ONLY a valid JSON object.

Expense Description: {expense_description}

Return this exact JSON structure:
{{
  "expense_category": "<category>",
  "expense_type": "<Essential | Non-Essential | Luxury>",
  "confidence_note": "<brief reason>"
}}

Categories to choose from:
Food & Dining, Groceries, Transport, Utilities, Healthcare,
Entertainment, Shopping, Education, Travel, Miscellaneous

Rules:
- If ambiguous (e.g. "paid bill"), keep category broad like "Utilities" or "Miscellaneous"
- Do NOT return anything outside the JSON object
- Do NOT add markdown, backticks, or explanation
"""
)