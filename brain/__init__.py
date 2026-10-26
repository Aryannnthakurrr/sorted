import sys

# Windows consoles default to cp1252, which can't print ₹ and the emoji in reminders.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure") and (_stream.encoding or "").lower() not in ("utf-8", "utf8"):
        _stream.reconfigure(encoding="utf-8", errors="replace")
