def observe():
    """Observe the current state."""
    print("Observing...")
    return {"status": "incomplete"}


def decide(observation):
    """Decide what action to take based on observation."""
    if observation["status"] == "complete":
        return "stop"
    return "act"


def act(action):
    """Perform the decided action."""
    print("Taking action...")
    
    # Example: change the state after some iterations
    return {"status": "complete"}


def observe_decide_act(max_iterations=10):
    """
    Observe → Decide → Act loop.
    Maximum iterations = 10.
    Returns 'success' if completed, otherwise 'failure'.
    """

    state = {"status": "incomplete"}

    for iteration in range(1, max_iterations + 1):
        print(f"\nIteration {iteration}")

        # 1. Observe
        observation = observe()

        # 2. Decide
        decision = decide(observation)

        if decision == "stop":
            print("Task completed.")
            return "success"

        # 3. Act
        state = act(decision)

        # Update observation state
        if iteration == 5:
            state["status"] = "complete"

        # Check completion
        if state["status"] == "complete":
            print("Task completed.")
            return "success"

    # Maximum iterations exceeded
    print("Maximum iterations exceeded.")
    return "failure"


# Run the loop
result = observe_decide_act(max_iterations=10)

print("\nFinal Result:", result)