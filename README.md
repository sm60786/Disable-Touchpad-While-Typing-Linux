# Disable-Touchpad-While-Typing-Linux

This Python script dynamically disables the touchpad while typing and re-enables it when typing stops.

## Installation

1. Clone this repository.
2. Make sure `xinput` is installed.
3. Save the script and make it executable.
4. Set up the script to run at startup.

## Usage

```bash
python disable_touchpad_while_typing.py

Setting Up the Script to Run at Startup
Save the Script:

Save the updated script as disable_touchpad_while_typing.py in your preferred directory.

Make the Script Executable:

bash
Copy code
chmod +x ~/disable_touchpad_while_typing.py
Configure the Script to Run at Startup:

Open Startup Applications:

Search for "Startup Applications" or use:

bash
Copy code
gnome-session-properties
Add a New Startup Program:

Click "Add."
Name: Disable Touchpad While Typing

Testing the Script
Before configuring it to run at startup, test the script manually to ensure it detects the touchpad and works as expected:

bash
Copy code
~/disable_touchpad_while_typing.py
Summary
The updated script dynamically detects the touchpad ID and manages its state based on typing activity, removing the need for hardcoding the ID. Adjust IDLE_TIMEOUT and TYPING_TIMEOUT to fit your preferences. If you need further modifications or have questions, feel free to ask!
Command: /usr/bin/python3 /home/your-username/disable_touchpad_while_typing.py
Comment: Python script to disable the touchpad while typing.
Save and Close

The script will now run automatically at login.
