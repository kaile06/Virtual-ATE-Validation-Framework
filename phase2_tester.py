import subprocess

def run_test(input_state):
    # Calls the compiled C executable and passes the input state
    result = subprocess.run(['./simulator', input_state], capture_output=True, text=True)
    return result.stdout.strip()

print("--- Running Automated Fault Injection Tests ---\n")

test_cases = [
    "ARMED_DOOR_OPEN",
    "DISARMED_DOOR_OPEN",
    "STATIC_NOISE_999",
    "BUFFER_OVERRUN_ATTEMPT_WITH_EXCESSIVE_STRING_LENGTH"
]

for test in test_cases:
    response = run_test(test)
    print(f"Sent: {test[:20]:<20} -> DUT Response: {response}")