# Demonstration of Before/After Output

## Original Tool Output

When searching for "Alice" in the sample logs with the original tool:

```
$ python log_viewer_original.py sample_logs.txt Alice

Matches for 'Alice':
2025-03-01T10:21:30 INFO [u1] Alice logged in from 1.2.3.4
2025-03-01T10:23:10 DEBUG [u1] Alice viewed page /home
2025-03-01T10:24:15 INFO [u1] Alice accessed API /users
2025-03-01T10:27:30 WARNING [u1] Alice attempted unauthorized access
2025-03-01T10:32:45 INFO [u1] Alice downloaded report
2025-03-01T10:35:00 INFO [u1] Alice logged out
```

### Problems with Original Output:
- No line numbers
- No context about how many matches found
- No structure or formatting
- Hard to parse and interpret
- No summary information
- No metadata about the search
- Cannot be processed programmatically (JSON)

---

## Enhanced Tool - Text Format

```
$ python log_viewer_enhanced.py sample_logs.txt Alice

======================================================================
SEARCH RESULTS
======================================================================

SUMMARY
------
Total Matches: 6
Total Lines Scanned: 17
Time Range: 2025-03-01 10:21:30 to 2025-03-01 10:37:30

RESULTS
------

Match #1
Line 1: 2025-03-01T10:21:30 INFO [u1] Alice logged in from 1.2.3.4
Keyword: 'Alice'

Match #2
Line 3: 2025-03-01T10:23:10 DEBUG [u1] Alice viewed page /home
Keyword: 'Alice'

Match #3
Line 4: 2025-03-01T10:24:15 INFO [u1] Alice accessed API /users
Keyword: 'Alice'

Match #4
Line 7: 2025-03-01T10:27:30 WARNING [u1] Alice attempted unauthorized access
Keyword: 'Alice'

Match #5
Line 12: 2025-03-01T10:32:45 INFO [u1] Alice downloaded report
Keyword: 'Alice'

Match #6
Line 15: 2025-03-01T10:35:00 INFO [u1] Alice logged out
Keyword: 'Alice'

======================================================================
```

### Improvements:
- ✓ Clear section headers (SUMMARY, RESULTS)
- ✓ Line numbers included for each match
- ✓ Total match count in summary
- ✓ Total lines scanned
- ✓ Timestamp range extracted automatically
- ✓ Structured format that's easy to read

---

## Enhanced Tool - JSON Format

```
$ python log_viewer_enhanced.py sample_logs.txt Alice --json

{
  "summary": {
    "total_matches": 6,
    "total_lines_scanned": 17,
    "time_range": {
      "earliest": "2025-03-01T10:21:30",
      "latest": "2025-03-01T10:37:30"
    }
  },
  "results": [
    {
      "line_number": 1,
      "line_content": "2025-03-01T10:21:30 INFO [u1] Alice logged in from 1.2.3.4",
      "keyword": "Alice"
    },
    {
      "line_number": 3,
      "line_content": "2025-03-01T10:23:10 DEBUG [u1] Alice viewed page /home",
      "keyword": "Alice"
    },
    {
      "line_number": 4,
      "line_content": "2025-03-01T10:24:15 INFO [u1] Alice accessed API /users",
      "keyword": "Alice"
    },
    {
      "line_number": 7,
      "line_content": "2025-03-01T10:27:30 WARNING [u1] Alice attempted unauthorized access",
      "keyword": "Alice"
    },
    {
      "line_number": 12,
      "line_content": "2025-03-01T10:32:45 INFO [u1] Alice downloaded report",
      "keyword": "Alice"
    },
    {
      "line_number": 15,
      "line_content": "2025-03-01T10:35:00 INFO [u1] Alice logged out",
      "keyword": "Alice"
    }
  ]
}
```

### Improvements:
- ✓ Fully structured JSON format
- ✓ Programmatically parseable
- ✓ Complete metadata (line numbers, keywords, content)
- ✓ Summary integrated with results
- ✓ Can be piped to jq or other tools
- ✓ Easy to import into other tools

---

## Enhanced Tool - Pretty Console Output

```
$ python log_viewer_enhanced.py sample_logs.txt Alice --pretty

(Output includes ANSI color codes for terminal display)
- Section headers in blue
- Match counts highlighted in yellow
- Line numbers in yellow
- Keyword highlighting with green background
- Overall improved visual structure

```

### Improvements:
- ✓ Color-coded for better readability
- ✓ All the benefits of text format
- ✓ Enhanced visual presentation
- ✓ Maintains structure for quick scanning

---

## Feature Comparison

| Feature | Original | Enhanced (Text) | Enhanced (JSON) | Enhanced (Pretty) |
|---------|----------|-----------------|-----------------|-------------------|
| Line numbers | ✗ | ✓ | ✓ | ✓ |
| Total matches | ✗ | ✓ | ✓ | ✓ |
| Context lines | ✗ | ✓ (optional) | ✓ (optional) | ✓ (optional) |
| Structured output | ✗ | ✓ | ✓ | ✓ |
| Timestamps | ✗ | ✓ | ✓ | ✓ |
| Programmatic access | ✗ | ~ (text parsing) | ✓ | ✗ |
| Color output | ✗ | ✗ | ✗ | ✓ |
| Metadata | ✗ | ✓ | ✓ | ✓ |
