import serial.tools.list_ports
import serial   # PySerial needs to be installed in your system
import time     # for Time
import signal   # Import signal module using the import keyword
import platform

# Modify these parameters according to your STM32 setup
logging_interval_seconds = 1
baudrate = 115200  # Modify baud rate according to your STM32 setup

log_count = 1
sentry = True  # used to control the While loop querying the STM32 and writing to file

# Print Info about the Program
print('+----------------------------------------------------------------+')
print('|  STM32 Python Serial Port Data Logging to CSV file Software    |')
print('+----------------------------------------------------------------+')
print('| Requires Pyserial installed on your System                     |')
print('| use CTRL + C to exit from the software                         |')
print('| log file name created using date and time                      |')
print('+----------------------------------------------------------------+\n')

print('OS full name           -> ' + platform.system() + '-' + platform.release()) # Which OS,Which OS Version
print('Python Implementation  -> ' + platform.python_implementation() +' Version ' + platform.python_version()) # Which Python,Which Version

print('Detecting available COM ports...')

# Detect available COM ports on Windows
available_ports = serial.tools.list_ports.comports()

for port in available_ports:
    print("Found COM port:", port.device)
    if "STMicroelectronics" in port.manufacturer:
        COMport = port.device
        print("STM32 found on port:", COMport)
        break
else:
    print("STM32 not found on any available COM port.")
    exit()

print('Baud Rate     ->', baudrate)

# Generate file name using Current Date and Time
current_local_time = time.localtime()  # Get Current date time
filename = time.strftime("%d_%B_%Y_%Hh_%Mm_%Ss", current_local_time)  # 24hour clock format
filename = 'stm32_' + filename + '_daq_log.csv'
print(f'\nCreated Log File -> {filename}')

print(f'\nLogging interval = {logging_interval_seconds} Seconds\n')

# Create a csv File header
with open(filename, 'w+') as csvFile:
    csvFile.write('No,Date,Time,AN1,AN2,AN3,AN4\n')

# Open the Serial Port using Pyserial
SerialObj = serial.Serial(COMport, baudrate)

# Signal Handler for SIGINT: CTRL + C
def SignalHandler_SIGINT(SignalNumber, Frame):
    print ('CTRL+C Pressed, Signal Caught')
    global sentry  # Global required since we want to modify sentry from inside the function
    sentry = False  # Turn sentry into false so it exits the while loop
    print ('sentry =', sentry)

signal.signal(signal.SIGINT, SignalHandler_SIGINT)  # Register the Signal Handler

# Infinite loop that queries the STM32 for data by sending '$' character                
while sentry:
    BytesWritten = SerialObj.write(b'$')  # Transmit '$' to get temperature values from STM32
    time.sleep(0.10)
    ReceivedString = SerialObj.readline().decode().strip()  # Read the received line, decode it and remove whitespace
    tempvalueslist = ReceivedString.split('-')

    separator = ','
    log_time_date = time.localtime()  # Get log date time from PC
    log_time = time.strftime("%H:%M:%S", log_time_date)  # hh:mm:ss
    log_date = time.strftime("%d %B %Y", log_time_date)  # dd MonthName Year
    
    log_file_text1 = f"{log_count}{separator}{log_date}{separator}{log_time}{separator}"
    log_file_text2 = f"{separator.join(tempvalueslist)}\n"
    log_file_text = log_file_text1 + log_file_text2
    
    # Write to file .csv
    with open(filename, 'a') as LogFileObj:
        LogFileObj.write(log_file_text)
        
    print(log_file_text)
    log_count += 1  # Increment no of logs taken
    
    time.sleep(logging_interval_seconds)  # Change logging_interval_seconds to change sensing interval 

# Exit from the loop and close the Serial port when sentry = False
SerialObj.close()  # Close the port

print('Data logging Terminated')
print('====================================')
