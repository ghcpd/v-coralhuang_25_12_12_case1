class TextFormatter:
    def format(self, matches, summary, keyword):
        output = "SEARCH RESULTS\n"
        output += "==============\n"
        for match in matches:
            highlighted_line = match['line'].replace(keyword, f'**{keyword}**')
            output += f"Line {match['line_number']}: {highlighted_line}\n"
            if match['context']:
                output += "Context:\n"
                for ctx in match['context']:
                    output += f"  {ctx}\n"
            output += "\n"
        output += "SUMMARY\n"
        output += "=======\n"
        output += f"Total lines scanned: {summary['total_lines']}\n"
        output += f"Number of matches: {summary['num_matches']}\n"
        if summary['earliest_ts']:
            output += f"Earliest timestamp: {summary['earliest_ts']}\n"
        if summary['latest_ts']:
            output += f"Latest timestamp: {summary['latest_ts']}\n"
        return output