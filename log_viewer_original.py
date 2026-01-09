# Original simplistic search function and the old generate_report kept for reference
import datetime


def generate_report(logs):
    # (copied unchanged)
    report = "USER ACTIVITY REPORT\n"
    report = report + "===================\n"
    total = 0
    user_set = []
    events = {}
    first_ts = None
    last_ts = None

    for log in logs:
        total = total + 1
        uid = log.get("user_id", "UNKNOWN")
        if uid not in user_set:
            user_set.append(uid)
        evt = log.get("event", "UNKNOWN")
        if evt not in events:
            events[evt] = 1
        else:
            events[evt] = events[evt] + 1

        ts_str = log.get("ts")
        if ts_str:
            try:
                ts = datetime.datetime.fromisoformat(ts_str)
            except Exception:
                ts = None
        else:
            ts = None

        if ts is not None:
            if first_ts is None:
                first_ts = ts
            if last_ts is None:
                last_ts = ts
            if ts < first_ts:
                first_ts = ts
            if ts > last_ts:
                last_ts = ts

    report = report + "Total logs: " + str(total) + "\n"
    report = report + "Unique users: " + str(len(user_set)) + "\n"
    report = report + "User IDs: "
    for u in user_set:
        report = report + u + ","
    report = report + "\n"

    report = report + "Events count:\n"
    for evt in events:
        report = report + "- " + evt + ": " + str(events[evt]) + "\n"

    if first_ts and last_ts:
        report = (
            report
            + "Time range: "
            + first_ts.isoformat()
            + " -> "
            + last_ts.isoformat()
            + "\n"
        )
    elif first_ts:
        report = report + "Time range: from " + first_ts.isoformat() + "\n"
    else:
        report = report + "Time range: UNKNOWN\n"

    report = report + "\nDETAILS\n"
    report = report + "-------\n"

    for u in user_set:
        report = report + "User: " + u + "\n"
        for log in logs:
            uid = log.get("user_id", "UNKNOWN")
            if uid == u:
                ts = log.get("ts", "UNKNOWN")
                evt = log.get("event", "UNKNOWN")
                name = log.get("user_name", "UNKNOWN")
                report = (
                    report
                    + "  - "
                    + str(ts)
                    + " "
                    + name
                    + " "
                    + evt
                    + "\n"
                )
        report = report + "\n"

    return report


# Simple baseline search function: returns raw matching lines (old behavior)
def search_logs(path, keyword):
    matches = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if keyword in line:
                matches.append(line.rstrip("\n"))
    return matches


if __name__ == "__main__":
    print("Original search (raw lines):")
    print(search_logs("sample.log", "login"))
