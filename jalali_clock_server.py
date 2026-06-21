"""
jalali_clock_server.py
A tiny local HTTP server that returns the current Jalali (Shamsi) date
as plain text — for use with Windhawk Taskbar Clock Customization %web<n>%.

Usage:
    python jalali_clock_server.py

Then set Windhawk web feed URL to: http://localhost:5765/jalali
The mod will refresh it on its own interval.

Install dep:
    pip install jdatetime
"""

import jdatetime
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 5765

WEEKDAYS_FA = {
    0: "دوشنبه",
    1: "سه‌شنبه",
    2: "چهارشنبه",
    3: "پنج‌شنبه",
    4: "جمعه",
    5: "شنبه",
    6: "یکشنبه",
}

MONTHS_FA = [
    "", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
]


def get_jalali_string():
    now = jdatetime.datetime.now()
    weekday = WEEKDAYS_FA[now.weekday()]
    day = now.day
    month_name = MONTHS_FA[now.month]
    year = now.year
    return f"{weekday} {day} {month_name} {year}"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # silence access logs

    def do_GET(self):
        if self.path in ("/jalali", "/"):
            text = get_jalali_string().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(text)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(text)
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Jalali clock server running at http://localhost:{PORT}/jalali")
    print("Press Ctrl+C to stop.")
    server.serve_forever()
