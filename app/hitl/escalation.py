import json

def create_ticket(state):
    ticket = {
        "query": state["user_query"],
        "reason": state["route"]
    }

    with open("ticket.json", "w") as f:
        json.dump(ticket, f)

    return ticket