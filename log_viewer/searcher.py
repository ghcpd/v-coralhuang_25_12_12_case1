import re
import datetime

class LogSearcher:
    def __init__(self, context_lines=2):
        self.context_lines = context_lines

    def search(self, lines, keyword):
        matches = []
        for line_no, line in lines:
            if keyword in line:
                start = max(1, line_no - self.context_lines)
                end = min(len(lines), line_no + self.context_lines)
                context = [lines[i - 1][1] for i in range(start, end + 1)]
                matches.append({
                    'line_number': line_no,
                    'line': line,
                    'context': context
                })
        return matches

    def get_summary(self, lines, matches):
        total_lines = len(lines)
        num_matches = len(matches)
        timestamps = []
        for _, line in lines:
            # Find timestamp, assume ISO format
            match = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', line)
            if match:
                try:
                    ts = datetime.datetime.fromisoformat(match.group())
                    timestamps.append(ts)
                except ValueError:
                    pass
        earliest = min(timestamps) if timestamps else None
        latest = max(timestamps) if timestamps else None
        return {
            'total_lines': total_lines,
            'num_matches': num_matches,
            'earliest_ts': earliest.isoformat() if earliest else None,
            'latest_ts': latest.isoformat() if latest else None
        }