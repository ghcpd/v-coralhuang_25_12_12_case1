import re
from .text import highlight_keyword


CSI = "\033["
RESET = CSI + "0m"
BOLD = CSI + "1m"
RED = CSI + "31m"
YELLOW = CSI + "33m"


def _colorize_keyword(text, keyword):
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)

    def repl(m):
        return f"{RED}{BOLD}{m.group(0)}{RESET}"

    return pattern.sub(repl, text)


def format_pretty(matches, keyword, total_lines):
    header = BOLD + "LOG SEARCH RESULTS" + RESET + "\n"
    header += "==================\n"
    header += f"Matches: {len(matches)}\n"
    header += f"Total lines scanned: {total_lines}\n"

    ts_list = [m.get("timestamp") for m in matches if m.get("timestamp")]
    if ts_list:
        earliest = min(ts_list)
        latest = max(ts_list)
        header += f"Earliest: {earliest.isoformat()}\n"
        header += f"Latest: {latest.isoformat()}\n"
    else:
        header += "Earliest: UNKNOWN\n"
        header += "Latest: UNKNOWN\n"

    header += "\n"
    body = ""
    for m in matches:
        body += f"Line {m['line_number']}: "
        highlighted = _colorize_keyword(m['line'], keyword)
        body += highlighted + "\n"
        if m.get("context"):
            for ln, txt in m["context"]:
                if ln != m["line_number"]:
                    body += f"  {ln}: {txt}\n"
    return header + body
