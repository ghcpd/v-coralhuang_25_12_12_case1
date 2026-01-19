"""Original log viewer - primitive implementation for comparison."""

def search_logs_original(filepath, keyword):
    """
    Original simple implementation.
    Returns raw matching lines without structure or formatting.
    """
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        return f"Error reading file: {e}"
    
    matches = []
    for line in lines:
        if keyword.lower() in line.lower():
            matches.append(line)
    
    # Very basic output - just raw lines
    if not matches:
        return "No matches found"
    
    output = f"Matches for '{keyword}':\n"
    for match in matches:
        output += match
    
    return output


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python log_viewer_original.py <log_file> <keyword>")
        sys.exit(1)
    
    result = search_logs_original(sys.argv[1], sys.argv[2])
    print(result)
