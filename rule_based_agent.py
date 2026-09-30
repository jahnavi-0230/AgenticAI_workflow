def rule_based_agent(temprature):
    if temprature > 100:
        return "cool"
        else:
            return "idle"

  #Test cases 
  temprature = [80, 100, 101, 120]

  for temp in temprature:
    action = rule_based_agent(temp)

    print(f"Temprature: {temp}")
    print(f"Agent action: {action}")
    print("_" = 30)
