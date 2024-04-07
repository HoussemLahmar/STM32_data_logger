# STM32 Data Logging Firmware

## Description
This firmware enables data logging from an STM32 microcontroller to a computer via UART communication. It continuously reads analog sensor data and transmits it to the computer upon receiving a specific character ('$').

## Dependencies
- `main.h`: Header file containing necessary declarations.
- `stdio.h`: Standard input-output library.
- `ADC_HandleTypeDef`: Handle structure for ADC peripheral.
- `UART_HandleTypeDef`: Handle structure for UART peripheral.

## Initialization
- Initializes the microcontroller, system clock, GPIOs, ADC, and UART peripherals.
- Configures the ADC to read analog sensor values from specified channels.
- Configures the UART for serial communication with the computer.

## Main Loop
- Enters an infinite loop to continuously read data and transmit it via UART.
- Waits for the '$' character to trigger data transmission.
- Reads analog sensor values from ADC channels and converts them to temperature values.
- Transmits the temperature values to the computer in a formatted string.
- Handles error cases when invalid characters are received.

## ADC Reading Function
- `ReadAnalogChannel`: Reads analog sensor values from specified ADC channels, calculates the average, and converts it to temperature.

## UART Initialization Function
- `MX_USART1_UART_Init`: Initializes UART1 for bidirectional communication with the computer.

## System Clock Configuration
- Configures the system clock using the PLL with specified parameters.

## GPIO Initialization
- Configures GPIO pins for UART communication.

## Note
Ensure proper hardware setup and configuration matching the pin connections, clock settings, and peripherals available on the STM32 microcontroller. Proper error handling and debugging capabilities should be implemented for troubleshooting purposes.
