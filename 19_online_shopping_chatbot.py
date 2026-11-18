"""Practical 19: Online shopping assistant chatbot using rule-based patterns."""
patterns = {
    "greeting": ["hello", "hi", "hey"],
    "product": ["product", "item", "available", "catalogue"],
    "price": ["price", "cost", "rate"],
    "order": ["order", "track", "tracking"],
    "payment": ["payment", "pay", "upi", "card"],
    "delivery": ["delivery", "shipping", "deliver"],
    "return": ["return", "replace", "exchange"],
    "refund": ["refund", "moneyback"],
}
responses = {
    "greeting": "Hello! I can help with shopping enquiries.",
    "product": "Please search the product catalogue for current availability.",
    "price": "Product prices are shown on the product page and may change.",
    "order": "Please use your order ID in the order-tracking section.",
    "payment": "Available payment methods are shown at checkout.",
    "delivery": "Delivery estimates are displayed during checkout.",
    "return": "Please review the store's return and exchange policy.",
    "refund": "Refund timelines depend on the payment method and store policy.",
}

def identify_intent(message):
    words = message.lower().split()
    for intent, keywords in patterns.items():
        if any(k in words for k in keywords):
            return intent
    return "unknown"

print("Online Shopping Assistant (type bye to exit)")
while True:
    message = input("You: ").strip()
    if message.lower() in {"bye", "exit", "quit"}:
        print("Bot: Happy shopping. Goodbye!")
        break
    intent = identify_intent(message)
    print("Bot:", responses.get(intent, "Sorry, I did not understand. Please rephrase."))
