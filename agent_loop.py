def agent_loop():
    log = []

    for step in range(1, 3):

        # Step 1: Observe
        if step == 1:
            observation = "User wants to calculate 10 + 20"
            log.append({
                "step": step,
                "action": "observe",
                "output": observation
            })

        # Step 2: Act
        elif step == 2:
            result = 10 + 20
            output = f"The answer is {result}"
            log.append({
                "step": step,
                "action": "act",
                "output": output
            })

    return {
        "status": "success",
        "steps": log
    }


# Run the 2-step agent loop
result = agent_loop()

print("Predicted Output:")
print(result)