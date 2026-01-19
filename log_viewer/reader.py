import os

class LogReader:
    def read_lines(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} not found")
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return [(i + 1, line.rstrip('\n')) for i, line in enumerate(lines)]