from log_viewer_original import search_logs as old_search
import logviewer

if __name__ == "__main__":
    keyword = "login"
    print("--- Original output (raw lines) ---")
    raw = old_search("sample.log", keyword)
    for r in raw:
        print(r)
    print()

    print("--- Enhanced text output ---")
    print(logviewer.search_logs("sample.log", keyword, context=1, fmt="text"))
    print()

    print("--- Enhanced JSON output ---")
    print(logviewer.search_logs("sample.log", keyword, fmt="json"))
