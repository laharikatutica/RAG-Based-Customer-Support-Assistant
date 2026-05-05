from hitl.escalation import create_ticket

def process(state):
    qa = state["qa"]
    query = state["user_query"]

    response = qa.run(query)

    state["answer_draft"] = response
    state["retrieved_chunks"] = ["dummy"]

    return state

def route_node(state):
    if state["route"] == "fallback":
        state["final_response"] = "No relevant info found"
    elif state["route"] == "clarify":
        state["final_response"] = "Please clarify your question"
    else:
        state["final_response"] = state["answer_draft"]

    return state

def escalate_node(state):
    ticket = create_ticket(state)
    state["final_response"] = f"Escalated: {ticket}"
    return state