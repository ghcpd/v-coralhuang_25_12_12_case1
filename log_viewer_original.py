def search_logs(path, keyword):
    """Original simplistic implementation: return list of matching raw lines.
    Preserves original behavior for comparison in tests.
    """
    with open(path, "r", encoding="utf-8") as f:
        res = []
        for line in f:
            if keyword.lower() in line.lower():
                res.append(line.rstrip("\n"))
    return res


if __name__ == "__main__":
    print(search_logs("sample_logs.txt", "login"))
