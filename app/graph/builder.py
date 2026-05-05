from langgraph.graph import StateGraph
from graph.nodes import process, route_node
from graph.routing import decide_route
from graph.state import GraphState

def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("process", process)
    builder.add_node("route", route_node)

    builder.set_entry_point("process")
    builder.add_edge("process", "route")

    return builder.compile()