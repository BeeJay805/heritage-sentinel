# planner.py — search algorithm only. No mention of statues, cracks, or pigment allowed here.
from collections import deque

def bfs_search(start, goal, available_actions, apply_action):
    frontier = deque([(start, [])])
    visited = {start}
    while frontier:
        state, path = frontier.popleft()
        if state == goal:
            return path
        for neighbor in available_actions(state):
            if neighbor not in visited:
                frontier.append((neighbor, path + [state]))
                visited.add(neighbor)
        ...
    return None  # no valid sequence exists