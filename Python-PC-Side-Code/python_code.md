# Python Data Logging Script for STM32 Microcontroller

## Description
This Python script facilitates data logging from an STM32 microcontroller to a computer via serial communication. It continuously queries the STM32 for data and logs it to a CSV file on the computer.

## Libraries Used
- `serial.tools.list_ports`: Detects available COM ports.
- `serial`: Enables serial communication.
- `time`: Handles time-related operations.
- `signal`: Manages signal handling.
- `platform`: Provides system and Python implementation information.

## Parameters
- `logging_interval_seconds`: Interval for data logging.
- `baudrate`: Baud rate for serial communication with the STM32.

## Program Information
Prints details about the program, including OS information and Python version.

## COM Port Detection
Detects available COM ports and searches for the one associated with STMicroelectronics (assumed to be the STM32).

## File Name Generation
Creates a unique log file name based on the current date and time.

## CSV File Header Creation
Writes the header for the CSV file specifying the data columns.

## Serial Port Opening
Opens the serial port using PySerial with the detected COM port and specified baud rate.

## Signal Handling
Defines a signal handler function to handle SIGINT (Ctrl+C) for graceful termination.

## Main Loop
- Enters an infinite loop to continuously query the STM32 for data.
- Sends a '$' character to the STM32 to request data.
- Reads the response, processes it, and logs the data to the CSV file.
- Pauses for the specified logging interval before repeating the process.

## Exiting the Loop and Closing the Serial Port
- Exits the loop and closes the serial port when SIGINT is received.

This script enables real-time data logging from an STM32 microcontroller to a CSV file on a computer, providing a flexible and customizable solution for data acquisition applications.
