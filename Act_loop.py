# Observe -> Decide -> Act loop
# Runs for exactly 3 iterations

def observe(state):
    """Observe the current state."""
    print(f"👀 Observing: {state}")
    return state


def decide(observation):
    """Decide what action should be taken."""
    if observation < 50:
        return "increase"
    elif observation > 50:
        return "decrease"
    else:
        return "stop"


def act(state, action):
    """Perform the selected action."""
    if action == "increase":
        state += 20
        print("⚙️ Action: Increasing value")
    elif action == "decrease":
        state -= 20
        print("⚙️ Action: Decreasing value")
    elif action == "stop":
        print("🛑 Action: Stop")

    return state


# Initial state
state = 20

# ACT loop - exactly 3 iterations
for iteration in range(1, 4):

    print(f"\n========== Iteration {iteration} ==========")

    # 1. OBSERVE
    observation = observe(state)

    # 2. DECIDE
    decision = decide(observation)
    print(f"🧠 Decision: {decision}")

    # 3. ACT
    state = act(state, decision)

    print(f"📊 New State: {state}")

print("\n========== Loop Completed ==========")
print(f"Final State: {state}")