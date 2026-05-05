def decide_route(state):
    if not state["retrieved_chunks"]:
        return "fallback"

    if len(state["retrieved_chunks"]) < 2:
        return "clarify"

    return "answer"