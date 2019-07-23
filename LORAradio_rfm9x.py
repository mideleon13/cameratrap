"""
The following code is tests the Lora Mesh Network for Lora Radio RFM9x modules.
"""
# Import Python System Libraries
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
 
 
# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Configure LoRa Radio
#Pins for CS and RESET differ for two working Lora modules right now. 
CS = DigitalInOut(board.D27)
RESET = DigitalInOut(board.D22)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None
 
while True:
    packet = None
    # check for incoming message 
    packet = rfm9x.receive()
    if packet is None:
        print('Waiting for message', 15, 20, 1)
    else:
        # Display incoming message
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        print('RX: ', 0, 0, 1)
        print(packet_text, 25, 0, 1)
        time.sleep(1)
 
        # Send Message
        message = bytes("Button A!\r\n","utf-8")
        rfm9x.send(message)
        print('This is an incoming message.', 25, 15, 1)
   
    time.sleep(0.1)
