# Beginner's Guide: Setting Up RFID-RC522 with LED on Raspberry Pi

 ## Youtube
  https://www.youtube.com/channel/UCoKwpQDB4NPGpygb1zmchOA

## Overview
This guide will walk you through setting up the RFID-RC522 module with an LED on a Raspberry Pi. You'll learn how to enable the SPI interface, install necessary libraries, connect the hardware, and run a Python script to read RFID tags and control an LED.

## Prerequisites
- Raspberry Pi with Raspbian OS installed
- RFID-RC522 module and tags 
- LED and a 220Ω resistor
- Jumper wires
- Breadboard (optional)


## Connect the Hardware

Connect the RFID RC522 module to the Raspberry Pi using the following pin connections:

RFID RC522 Pin	           Raspberry Pi Pin	           Pin Number
VCC	                      3.3V	                          1
GND                       GND                           	6
SDA                       GPIO 8 (SPI0_CE0_N)	           24
SCK	                      GPIO 11 (SPI0_SCLK)	           23
MOSI	                     GPIO 10 (SPI0_MOSI)	           19
MISO	                     GPIO 9 (SPI0_MISO)	            21
IRQ	                      Not connected	                 --
RST                       GPIO 25                        22

## Installation Required Libraries
   ```sh
pip install spidev
pip install mfrc522

##  Enable SPI Interface
1. Open a terminal and run the following command:
   ```sh
   sudo raspi-config
-Navigate to Interface Options.
-Select SPI and enable it.
-Exit and reboot the Raspberry Pi:
```sh
  sudo reboot
