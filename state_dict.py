def observe(state):
    """Observe the current state."""
    print(f"Observing... Step {state['steps']}")
    return state


def decide(observation):
    """Decide the next action."""
    if observation["done"]:
        return "stop"

    return "act"


def act(state):
    """Perform the action and update the state."""
    print("Taking action...")

    state["steps"] += 1

    # Example condition for completing the task
    if state["steps"] >= 5:
        state["done"] = True

    return state


def observe_decide_act(max_iterations=10):
    # State dictionary
    state = {
        "done": False,
        "steps": 0
    }

    for iteration in range(1, max_iterations + 1):
        print(f"\nIteration {iteration}")

        # 1. Observe
        observation = observe(state)

        # 2. Decide
        decision = decide(observation)

        if decision == "stop":
            return "success", state

        # 3. Act
        state = act(state)

        # Check if completed
        if state["done"]:
            return "success", state

    # Maximum iterations exceeded
    return "failure", state


# Run
result, state = observe_decide_act(max_iterations=10)

print("\nFinal Result:", result)
print("Final State:", state)