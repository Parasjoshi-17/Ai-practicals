"""Practical 18: Railway enquiry chatbot using predefined rules."""
patterns = {
    "greeting": ["hello", "hi", "hey"],
    "train": ["train", "trains", "number"],
    "schedule": ["time", "timing", "schedule", "departure", "arrival"],
    "ticket": ["ticket", "booking", "book", "reservation"],
    "fare": ["fare", "price", "cost"],
    "platform": ["platform"],
    "pnr": ["pnr", "status"],
    "cancel": ["cancel", "cancellation", "refund"],
}
responses = {
    "greeting": "Hello! Welcome to Railway Enquiry.",
    "train": "Please provide the route or train number and check the official railway enquiry service.",
    "schedule": "Train schedules can change. Check the official railway enquiry service for live timings.",
    "ticket": "Tickets can be booked through the official railway booking service.",
    "fare": "Fare depends on train, class and route. Check the official booking service.",
    "platform": "Platform information may change; check station displays or official live enquiry.",
    "pnr": "Use the official PNR enquiry service for the latest status.",
    "cancel": "Cancellation and refund rules depend on ticket type and timing; check official railway rules.",
}

def identify_intent(message):
    words = message.lower().split()
    for intent, keywords in patterns.items():
        if any(k in words for k in keywords):
            return intent
    return "unknown"

print("Railway Enquiry Chatbot (type bye to exit)")
while True:
    message = input("You: ").strip()
    if message.lower() in {"bye", "exit", "quit"}:
        print("Bot: Thank you for using Railway Enquiry.")
        break
    intent = identify_intent(message)
    print("Bot:", responses.get(intent, "Sorry, I did not understand. Please rephrase your query."))
