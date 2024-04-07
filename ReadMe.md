### Overview
This project facilitates data logging from an STM32 microcontroller to a computer using Python. It involves two main components: STM32-side code for data acquisition and Python PC-side code for logging and visualization. The STM32 code reads data from analog sensors and sends it over UART, while the Python script receives this data, logs it to a CSV file, and provides real-time visualization.

### Setup and Use
#### 1. Hardware Setup:
- Connect your STM32 microcontroller to the computer via a suitable communication interface (e.g., USB-to-serial converter).
- Ensure that analog sensors are connected to the STM32's ADC pins for data acquisition.

#### 2. Software Setup:
- **STM32 Code**:
  - Copy the provided STM32 code into your STM32 project's main application file.
  - Adjust the code to match your specific hardware setup, including pin configurations, clock settings, and peripherals used (e.g., ADC and UART).
  - Ensure proper initialization of ADC and UART peripherals and handle any errors that may occur during operation.

- **Python Script**:
  - Install Python on your computer if not already installed.
  - Copy the provided Python script into a Python file on your computer.
  - Install required Python libraries, such as `pyserial`, using pip if not already installed (`pip install pyserial`).
  - Modify the Python script to adjust parameters like logging interval, baud rate, and file naming according to your STM32 code and hardware setup.

#### 3. Running the Project:
- Open a command prompt or terminal.
- Navigate to the directory containing the Python script (`cd path/to/Python-PC-Side-Code`).
- Execute the Python script by running `python Python-STM32-CSV-Logger.py`.
- The script will automatically detect the COM port where the STM32 microcontroller is connected and start logging data to a CSV file.
- Ensure that the STM32 microcontroller is powered and running the flashed firmware for data acquisition.

### Note
- **Verify Hardware Connections**: Before running the project, double-check hardware connections and configurations to ensure proper communication between the STM32 microcontroller and the computer.
- **CSV File Verification**: Verify that the generated CSV file contains the expected data, ensuring successful logging from the STM32 microcontroller.
- **Error Handling and Debugging**: Implement proper error handling and debugging capabilities in both the STM32 firmware and Python script to facilitate troubleshooting.
- **Customization**: This project can be customized for logging various types of data, not just temperature. Modify the code as needed to suit your specific data logging requirements.
- **Contributions**: Contributions to improve and extend this project, especially for beginners, are welcome. Feel free to enhance the codebase and documentation to make it more accessible and versatile.
