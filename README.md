# 🇦🇲 VFS Appointment Slot Checker Bot

This project monitors visa appointment availability on [VFS Global](https://www.vfsglobal.com), specifically for users **applying from Armenia** to popular destinations such as:

- Italy
- France
- Germany
- Greece
- Spain

When a possible appointment slot is available, it notifies you via a **desktop notification** so you can act fast.

---

## ✅ Features

- 🔍 Checks VFS appointment pages stealthily using Chromium
- ⚡ Every 3-minute check for changes
- 🔔 Desktop notifications on available slots
- 💻 Cross-platform: works on **Ubuntu/Linux** and **Windows**
- 📦 Lightweight: only uses Playwright

---

## 📁 Folder Structure

```
vfs_checker/
├── run_bot.py         # Main runner script (auto-detects OS and country)
├── vfs_checker.py     # Appointment checker logic
├── requirements.txt   # Python dependencies
└── .venv/             # Local virtual environment (not committed)
```

---

## 🔧 How to Run the Bot (Step-by-Step)

These steps work on both **Ubuntu/Linux** and **Windows**.

---

### ✅ 1. Clone the Project

Open a terminal (Linux) or PowerShell/CMD (Windows) and run:

```bash
git clone https://github.com/YOUR_USERNAME/vfs_checker.git
cd vfs_checker
```

---

### ✅ 2. Create and Activate a Virtual Environment

#### 💻 On Ubuntu/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 🪟 On Windows:

```cmd
python -m venv .venv
.\.venv\Scriptsctivate
```

---

### ✅ 3. Install Dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
playwright install
```

> `playwright install` downloads the headless Chromium browser.

---

### ✅ 4. Run the Bot

Use the following command, replacing `italy` with your target country:

```bash
python run_bot.py italy
```

✅ **Supported country names**:
- `italy`
- `france`
- `germany`
- `greece`
- `spain`

---

### ✅ Example Output

```bash
🌍 Target country: Italy → code: ita
[2025-05-30 12:00:00] Checking https://visa.vfsglobal.com/arm/en/ita/login
✅ Appointment might be available!
```

If this appears, open the VFS website immediately and try to log in and book the appointment manually.

---

## 🔔 Desktop Notifications

### On Ubuntu/Linux:
Make sure `libnotify-bin` is installed:
```bash
sudo apt install libnotify-bin
```

### On Windows (Optional):
To use native notifications:
```bash
pip install win10toast
```
And update your `vfs_checker.py` to use:

```python
from win10toast import ToastNotifier
ToastNotifier().show_toast("VFS Slot Available!", "Slot detected for ITA!", duration=10)
```

---

## 📝 Optional: Save Your Dependencies

After setup, run this to generate `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## 🧠 Notes

- The script **does not auto-book** appointments — you must act manually.
- The `.venv/` folder is local only and should not be committed to GitHub.
- Appointment pages are dynamic; behavior may change depending on the VFS system.

---

## 📌 Coming Soon Ideas

- [ ] Telegram push alerts
- [ ] GUI selector for countries
- [ ] Auto-start on boot
