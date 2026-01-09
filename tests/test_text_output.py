import logviewer


def test_text_contains_headers_and_highlight(tmp_path):
    p = tmp_path / "t.log"
    p.write_text("2025-03-01T00:00:00 event=login user=u1\nno match here\n")
    out = logviewer.search_logs(str(p), "login", context=0, fmt="text")
    assert "LOG SEARCH REPORT" in out
    assert "Line 1" in out
    assert "<<login>>" in out
