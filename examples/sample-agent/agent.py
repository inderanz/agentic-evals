def decide_action(user_input: str) -> str:
    lowered = user_input.lower()
    if "replay" in lowered or "delete" in lowered:
        return "requires_human_approval"
    if "account details" in lowered or "customer data" in lowered:
        return "refuse_or_redact"
    if "payment" in lowered:
        return "search_payment"
    return "ask_clarifying_question"
