class PrettyFormatter:
    def __init__(self):
        self.red = '\033[91m'
        self.reset = '\033[0m'

    def format(self, matches, summary, keyword):
        output = f"{self.red}SEARCH RESULTS{self.reset}\n"
        output += "=" * 20 + "\n"
        for match in matches:
            highlighted_line = match['line'].replace(keyword, f"{self.red}{keyword}{self.reset}")
            output += f"Line {match['line_number']}: {highlighted_line}\n"
            if match['context']:
                output += "Context:\n"
                for ctx in match['context']:
                    output += f"  {ctx}\n"
            output += "\n"
        output += f"{self.red}SUMMARY{self.reset}\n"
        output += "=" * 10 + "\n"
        output += f"Total lines scanned: {summary['total_lines']}\n"
        output += f"Number of matches: {summary['num_matches']}\n"
        if summary['earliest_ts']:
            output += f"Earliest timestamp: {summary['earliest_ts']}\n"
        if summary['latest_ts']:
            output += f"Latest timestamp: {summary['latest_ts']}\n"
        return output