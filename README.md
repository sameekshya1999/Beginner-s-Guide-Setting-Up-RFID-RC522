# Beginner's Guide: Setting Up RFID-RC522 with LED on Raspberry Pi

 ## Youtube
  https://www.youtube.com/channel/UCoKwpQDB4NPGpygb1zmchOA

## Overview
This guide will walk you through setting up the RFID-RC522 module with an LED on a Raspberry Pi. You'll learn how to enable the SPI interface, install necessary libraries, connect the hardware, and run a Python script to read RFID tags and control an LED.

## Connect the Hardware

Connect the RFID RC522 module to the Raspberry Pi using the following pin connections:



| RFID RC522 Pin | Raspberry Pi Pin       | Pin Number |
|----------------|------------------------|------------|
| SDA            | SPICE0                 | 24         |
| SCK            | SPISCLK                | 23         |
| MOSI           |SPIMOSI                 | 19         |
| MISO           |SPIMISO                 | 21         |
| IRQ            | Not connected          | --         |
| GND            | GND                    | 6          |
| RST            | GPIO 25                | 22         |
| VCC            | 3.3V                   | 1          |




## Installation Required Libraries
   ```sh
pip install spidev
pip install mfrc522
```

## Prerequisites
- Raspberry Pi with Raspbian OS installed
- RFID-RC522 module and tags 
- LED and a 220Ω resistor
- Jumper wires
- Breadboard (optional)

##  Enable SPI Interface
1. Open a terminal and run the following command:
   ```sh
   sudo raspi-config
   ```
-Navigate to Interface Options.

-Select SPI and enable it.

-Exit and reboot the Raspberry Pi:

```sh
  sudo reboot
```
