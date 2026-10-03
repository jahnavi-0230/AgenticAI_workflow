def observe(state):
    """Observe the current state."""
    print(f"Observing... Step {state['steps']}")
    return state


def decide(state):
    """Decide what action to take."""
    if state["done"]:
        return "stop"

    return "act"


def act(state):
    """Perform the action and update the state."""
    print("Taking action...")

    state["steps"] += 1

    # Example condition
    if state["steps"] >= 5:
        state["done"] = True

    return state


def observe_decide_act(max_iterations=10):

    # Initial state
    state = {
        "done": False,
        "steps": 0
    }

    for iteration in range(1, max_iterations + 1):

        print(f"\nIteration {iteration}")

        # OBSERVE
        observation = observe(state)

        # DECIDE
        decision = decide(observation)

        # SUCCESS condition
        if decision == "stop":
            return {
                "status": "success",
                "state": state
            }

        # ACT
        state = act(state)

        # Check completion
        if state["done"]:
            return {
                "status": "success",
                "state": state
            }

    # FAILURE after maximum iterations
    return {
        "status": "failure",
        "state": state
    }


# Run the loop
result = observe_decide_act(max_iterations=10)

print("\nFinal Result:")
print(result)