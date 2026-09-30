def goal_based_agent(current_temprature, goal_temprature=72):
    if current_temprature > goal_temprature:
        return "cool"

        elif current_temprature < goal_temprature:
            return"heat"

            else:
                return"idle"


tempratures = [110, 90, 72, 60, 40]

for temp in tempratures:
    action = goal_based_agent(temp)

    print(
        f"Temprature: {temp}F "
        f|"Goal: 72F "
        f|Action: {action}"
    )