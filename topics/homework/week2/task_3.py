# Initial steps/scenarios
steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login"]  # Duplicate of steps_1

# Convert each scenario's steps to frozensets
scenario_1 = frozenset(steps_1)
scenario_2 = frozenset(steps_2)
scenario_3 = frozenset(steps_3)

# Dictionary of scenarios with frozensets
dic_scenarios = {
    "Test Case 1": scenario_1,
    "Test Case 2": scenario_2,
    "Test Case 3": scenario_3
}


# Function to check if a new test scenario already exists
def check_scenario(test_name, new_steps, existing_scenarios):
    new_scenario = frozenset(new_steps)

    for key, scenario in existing_scenarios.items():
        if new_scenario == scenario:
            print("Test Case", test_name, "matches", key)
            return

    print("No match found for Test Case", test_name)


# Example usage
new_steps = ["open browser", "navigate to page", "click login"]  # Same steps as Test Case 1
check_scenario("Test Case 4", new_steps, dic_scenarios)  # Output: Should indicate that it matches Test Case 1