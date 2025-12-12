def search_logs(path, keyword):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [line for line in lines if keyword in line]