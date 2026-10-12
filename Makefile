CC=gcc
TARGET=simulator

# main task is to build simulator
all: $(TARGET)

#recompile project if these files were edited
$(TARGET): simulator.c dut.c
#take two C files and output (-o) a finished simulator program
	$(CC) -o $(TARGET) simulator.c dut.c