# jalali-clock-server

A minimal local HTTP server that returns the current **Jalali (Shamsi/Persian) date** as plain text — designed for use with the [Windhawk Taskbar Clock Customization](https://windhawk.net/mods/taskbar-clock-customization) mod.

No changes to Windows regional settings required.

---

## How it works

The server listens on `http://localhost:5765/jalali` and returns a string like:

```
شنبه 31 خرداد 1405
```

Windhawk's `%web<n>%` pattern polls a URL at your configured interval and injects the result into the tray clock.

---

## Setup

### 1. Install dependency

```bash
pip install jdatetime
```

### 2. Run the server

```bash
python jalali_clock_server.py
```

### 3. Configure Windhawk

In **Taskbar Clock Customization → Settings**:

- Add a **Web content** entry with URL: `http://localhost:5765/jalali`
- Set your desired refresh interval (e.g. 60 seconds)
- In your **Top line** or **Bottom line** format, use `%web1%` (or whichever number you assigned)

Example top line:
```
%web1%  %time%
```

Result:
```
شنبه 31 خرداد 1405  07:12 AM
```

---

## Auto-start on Windows

To run it silently on login, create a shortcut to:

```
pythonw jalali_clock_server.py
```

Place it in `shell:startup` (`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`).

---

## Customization

Edit `jalali_clock_server.py`:

- **Digits**: Use `str.translate()` to convert to Eastern Arabic numerals if you prefer `٣١` over `31`
- **Format**: Change `get_jalali_string()` to return `now.strftime("%Y/%m/%d")` for numeric format like `1405/03/31`
- **Port**: Change `PORT = 5765` to any free port

### Numeric format example

```python
def get_jalali_string():
    now = jdatetime.datetime.now()
    return now.strftime("%Y/%m/%d")
# → 1405/03/31
```
