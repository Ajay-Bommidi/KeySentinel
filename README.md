# 🔑 Simple Keylogger - Ethical Key Tracking Tool

## 🚀 Introduction
The **Simple Keylogger** is a lightweight and interactive keystroke logging tool designed for ethical and authorized use. It captures and logs keystrokes, saving them to a file for analysis. This project focuses on **security research, parental control, and personal key tracking**, ensuring transparency and ethical usage.
![Screenshot 2025-03-10 204232](https://github.com/user-attachments/assets/1c8df97c-4430-4896-834c-86998a0b5c6e)

## 🎯 Features
- **🔵 Real-time Key Logging**: Captures keystrokes dynamically with a color-coded interface.
- **📝 Log File Generation**: Stores keystrokes with timestamps in a secure log file.
- **🎨 Interactive CLI**: Engaging, stylish command-line interface with color-coded key logs.
- **🛡️ Ethical & Secure**: Stops logging when `ESC` is pressed; encourages responsible usage.
- **🔐 Encryption (Optional)**: Logs can be encrypted for enhanced security.

## ⚠️ Legal & Ethical Notice
This tool is designed **strictly for ethical purposes**, such as:
- Personal keystroke analysis.
- Parental monitoring (with consent).
- Security testing with proper authorization.

**Unauthorized use of keyloggers is illegal. Ensure you have proper permission before deploying this tool.**

## 🛠 Installation
Ensure you have Python installed, then clone the repository and install dependencies:
```sh
sudo python3 -m venv myenv
source myenv/bin/activate
```

```sh
# Clone the repository
sudo git clone https://github.com/Ajay-Bommidi/KeySentinel.git
cd KeySentinel
```
# Install required dependencies
```sh
pip install -r requirements.txt
```

## 🚀 Usage
Run the keylogger from the terminal:

```sh
python KeySentinel.py
```

### 📝 How It Works
1. The tool starts capturing keystrokes in real time.
2. Keystrokes are logged to a file (`log.txt`) with timestamps.
3. Press `ESC` to stop logging and exit.

## 📌 Example Output
```
🔑 Simple Keylogger - Ethical Key Tracking
-----------------------------------------
Logging started...

[12:35:10] User pressed: H
[12:35:11] User pressed: e
[12:35:12] User pressed: l
[12:35:13] User pressed: l
[12:35:14] User pressed: o

Log saved to log.txt
```

## 🔧 Customization
- Modify `log.txt` filename in `KeySentine.py` for a different storage location.
- Add encryption support to secure log files.
- Implement GUI logging using Tkinter for better usability.

## 💡 Future Enhancements
- **Graphical User Interface (GUI)** for an improved user experience.
- **Encrypted Log Storage** for enhanced security.
- **Cloud Sync Support** for remote monitoring (Ethical use only).

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo, create issues, and submit pull requests.

## ⚖️ License
This project is licensed under the MIT License.
