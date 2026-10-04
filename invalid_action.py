def act_loop(action, max_iterations=10):
    log = []
    done = False

    valid_actions = ["search", "calculate", "finish"]

    for iteration in range(1, max_iterations + 1):

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

        # Perform valid action
        action_result = f"Action '{action}' performed successfully"
        log.append(action_result)

        # SUCCESS
        if action == "finish":
            done = True
            log.append("Task completed successfully")

            return {
                "status": "success",
                "done": done,
                "steps": log
            }

    # MAXIMUM ITERATIONS EXCEEDED
    log.append("Maximum iterations exceeded")

    return {
        "status": "failure",
        "done": done,
        "steps": log
    }


# Test with invalid action
result = act_loop("invalid_action")

print(result)