def act_loop(action, max_iterations=10):
    log = []
    done = False
    iteration = 1

    valid_actions = ["search", "calculate", "finish"]

    while iteration <= max_iterations:

        # OBSERVE
        observation = f"Observed environment at iteration {iteration}"
        log.append(observation)

        # DECIDE
        decision = f"Decision made at iteration {iteration}"
        log.append(decision)

        # ACT - validate action
        if action not in valid_actions:
            error_message = f"Invalid action: {action}"
            log.append(f"Error: {error_message}")

            return {
                "status": "error",
                "error": error_message,
                "iteration": iteration,
                "done": done,
                "steps": log
            }

        # Perform action
        action_result = f"Action '{action}' performed successfully"
        log.append(action_result)

        # Check for success
        if action == "finish":
            done = True
            log.append("Task completed successfully")

            return {
                "status": "success",
                "done": done,
                "steps": log
            }

        # IMPORTANT: increment iteration
        iteration += 1

    # Maximum iterations reached
    log.append("Maximum iterations exceeded")

    return {
        "status": "failure",
        "done": done,
        "steps": log
    }


# Test
result = act_loop("search", max_iterations=3)

print("Status:", result["status"])
print("Done:", result["done"])
print("Full Log:")

for step in result["steps"]:
    print(step)