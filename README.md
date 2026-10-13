# Virtual-ATE-Validation-Framework

The Virtual ATE Validation Framework is a software-based project that connects hardware limits with automated testing. First, build a basic C program to simulate a physical device in this case it is a home safety alarm, using fixed memory to keep it safe from crashing. Next, write a Python script that automatically sends both normal commands and intentional errors to this C-based DUT program to make sure it handles bad data correctly. Finally, the Python script runs this test 1,000 times, saves the speed and error data using Pandas, and creates a simple bar chart to show the final results using Matplotlib.

![Yield Analysis Histogram](yield_histogram.png)
