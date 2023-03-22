# Fox-Box
Raspberry Pi Pico Fox

First saw this project in 'Arduino for Ham Radio' ARRL by Glen Popiel, KW5GP. However
chapter 8 'CW Beacon and Foxhunt Keyer' was written for an Arduino. 
I wanted to complete this project using a Raspberry Pi Pico.

This works by plugging the cable into a Boafeng radio, then turing the box on.
The light show the status cycle. Green for standby, blue for the PTT is pressed, 
Then the red for the morse code.

Features to add:
- use only one multicolor LED
- get the volumn control to properly adjust the output
- receive input from another rtransmitter before broadcasting. 
- Shrink the solder boards, use two smaller ones instead of on big board
- Mount a USB port for charging & programing
- use Pi Pico W for a Web interface.
- add LCD to display message being sent
