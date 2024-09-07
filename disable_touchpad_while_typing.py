#!/usr/bin/env python3

import subprocess
import time
import signal

# Set the threshold for typing inactivity (in seconds)
IDLE_TIMEOUT = 1
TYPING_TIMEOUT = 0.5  # Time in seconds to wait before disabling the touchpad after the last keypress

# Global flag to manage script state
running = True

def get_touchpad_id():
    try:
        # Get list of input devices
        result = subprocess.run(['xinput', 'list'], capture_output=True, text=True)
        devices = result.stdout

        # Find touchpad device ID
        for line in devices.split('\n'):
            if 'Touchpad' in line:  # Adjust if necessary to match your device name
                id_str = line.split('id=')[1].split()[0]
                return int(id_str)
    except Exception as e:
        print(f"Error getting touchpad ID: {e}")
    return None

def toggle_touchpad(id, enable):
    try:
        if enable:
            subprocess.run(['xinput', '--enable', str(id)], check=True)
        else:
            subprocess.run(['xinput', '--disable', str(id)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error toggling touchpad: {e}")

def signal_handler(sig, frame):
    global running
    running = False
    print("Script interrupted. Exiting...")

def main():
    global running
    touchpad_id = get_touchpad_id()
    if touchpad_id is None:
        print("Touchpad not found.")
        return

    last_activity_time = time.time()

    # Set up signal handling for graceful exit
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Ensure touchpad is enabled at startup
    toggle_touchpad(touchpad_id, enable=True)

    while running:
        current_time = time.time()
        idle_time = current_time - last_activity_time

        # Check if idle time exceeds the threshold
        if idle_time > TYPING_TIMEOUT:
            # Enable touchpad if idle
            toggle_touchpad(touchpad_id, enable=True)
        else:
            # Disable touchpad if typing
            toggle_touchpad(touchpad_id, enable=False)

        # Update the last activity time
        last_activity_time = current_time
        time.sleep(IDLE_TIMEOUT)

if __name__ == "__main__":
    main()
