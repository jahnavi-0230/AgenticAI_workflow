def act_loop(max_iterations=10):
    log = []
    done = False

    for iteration in range(1, max_iterations + 1):

        # Observe
        observation = f"Observed environment at iteration {iteration}"
        log.append(observation)

        # Decide
        decision = f"Decision made at iteration {iteration}"
        log.append(decision)

        # Act
        action = f"Action performed at iteration {iteration}"
        log.append(action)

        # Success condition
        if iteration == 3:
            done = True
            log.append("Task completed successfully")

            return {
                "status": "success",
                "done": done,
                "steps": log
            }

    # Failure after maximum iterations
    log.append("Maximum iterations exceeded")

    return {
        "status": "failure",
        "done": done,
        "steps": log
    }


# Run the ACT loop
result = act_loop()

# Return / print the full log
print("Status:", result["status"])
print("Done:", result["done"])
print("Full Log:")

for step in result["steps"]:
    print(step)