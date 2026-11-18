"""Practical 20: Banking enquiry chatbot using rule-based patterns."""
patterns = {
    "greeting": ["hello", "hi", "hey"],
    "balance": ["balance", "amount"],
    "account": ["account", "open", "opening"],
    "loan": ["loan", "emi", "interest"],
    "card": ["card", "debit", "credit"],
    "transfer": ["transfer", "neft", "rtgs", "imps"],
    "hours": ["hours", "timing", "working"],
    "block": ["block", "lost", "stolen"],
}
responses = {
    "greeting": "Hello! Welcome to Banking Enquiry.",
    "balance": "For security, check your balance only through the bank's official app, ATM or website.",
    "account": "Please visit the bank or official website for account-opening requirements.",
    "loan": "Loan eligibility, interest rates and EMI depend on the bank's current terms.",
    "card": "Contact your bank through its verified channel for card services.",
    "transfer": "Use the bank's official app or website for fund transfers and current limits.",
    "hours": "Please check your bank branch's official listing for working hours.",
    "block": "If your card is lost or stolen, immediately contact the bank using its verified emergency number.",
}

def identify_intent(message):
    words = message.lower().split()
    for intent, keywords in patterns.items():
        if any(k in words for k in keywords):
            return intent
    return "unknown"

print("Banking Enquiry Chatbot (type bye to exit)")
while True:
    message = input("You: ").strip()
    if message.lower() in {"bye", "exit", "quit"}:
        print("Bot: Thank you. Goodbye!")
        break
    intent = identify_intent(message)
    print("Bot:", responses.get(intent, "Sorry, I did not understand. Contact your bank through official channels."))
