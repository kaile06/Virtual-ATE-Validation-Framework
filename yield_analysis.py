import subprocess
import time
import csv
import random
import pandas as pd
import matplotlib.pyplot as plt

sensor_inputs = [
    "ARMED_DOOR_OPEN", "ARMED_MOTION", "DISARMED_DOOR_OPEN", 
    "STATIC_NOISE", "SHORT_CIRCUIT_SIGNAL", "CORRUPTED_DATA"
]

#results list is created before the for loop to collect all 1000 results
results = []
print("Running 1,000 Automated Test Loops...")

for i in range(1000):
    test_input = random.choice(sensor_inputs)

    #record the start and end time to monitor the speed and accuracy of code
    #when test time is too long it is likely struggling to process invalid data
    start_time = time.perf_counter()
    #enter random input into simulator, capture the output and make it readable text
    res = subprocess.run(['./simulator', test_input], capture_output=True, text=True)
    end_time = time.perf_counter()

    #remove /r from MSYS2 terminal output and /n from simulator.c
    response = res.stdout.strip()
    exec_time_ms = (end_time - start_time) * 1000

    #groups the test number, input, output, test time into a row
    #saves row into "results=[]" list to be logged into CSV file
    results.append([i, test_input, response, exec_time_ms])

# 'with' ensures file auto closes when code end running even if fatal error
# newline='' ensures no blank rows from windows, so pandas won't receive invalid data
with open("yield_report.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test_ID", "Input_Signal", "DUT_Response", "Response_Time_ms"])
    writer.writerows(results)

# load csv file into pandas DataFrame
df = pd.read_csv("yield_report.csv")
yield_counts = df['DUT_Response'].value_counts()

# create a bar chart of safe-state response against frequency
yield_counts.plot(kind='bar')
plt.title('Yield Analysis')
plt.xlabel('Safe-State Response')
plt.ylabel('Frequency')
#adjusts spacing so title, axis labels and data fit perfect within image boundary
plt.tight_layout() 
plt.savefig('yield_histogram.png')
print("Histogram generated!")
