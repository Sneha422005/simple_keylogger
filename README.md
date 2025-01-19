# Simple_Keylogger
A basic Python keylogger script that records and logs keystrokes to a file. This project demonstrates how to use the `pynput` library to capture keyboard input.

---

## Features
- Records all key presses, including special keys like `Enter`, `Shift`, and `Backspace`.
- Saves the captured keystrokes to a log file (`key_log.txt`).
- Stops logging when the `Esc` key is pressed.

---

## Prerequisites
1. **Python**:
   - Ensure Python 3.x is installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Required Library**:
   - Install the `pynput` library using the following command:
     ```bash
     pip install pynput
     ```

---

## How to Run
1. **Clone or Download the Script**:
   - Save the `keylogger.py` script to your local system.

2. **Run the Script**:
   - Open a terminal in the script's directory.
   - Execute the script using:
     ```bash
     python keylogger.py
     ```

3. **Stop Logging**:
   - Press the `Esc` key to terminate the script.

4. **Check the Log**:
   - The recorded keystrokes are saved in a file named `key_log.txt` in the same directory as the script.

---

## Usage Notes
- **Ethical Use Only**:
  - This script is intended for educational purposes or personal use.
  - Ensure you have proper consent if testing on devices that are not your own.
- **Legal Disclaimer**:
  - Unauthorized use of this script on systems without permission may violate local laws and regulations.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
