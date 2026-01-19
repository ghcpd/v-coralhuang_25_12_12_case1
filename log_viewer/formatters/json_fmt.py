import json

class JsonFormatter:
    def format(self, matches, summary):
        data = {
            'matches': matches,
            'summary': summary
        }
        return json.dumps(data, indent=2)