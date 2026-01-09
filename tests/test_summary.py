import json
import logviewer
import log_viewer_original


def test_summary_counts(tmp_path):
    p = tmp_path / "t.log"
    p.write_text("a login\nnope\nlogin again\n")
    enhanced = logviewer.search_logs(str(p), "login", fmt="json")
    data = json.loads(enhanced)
    original = log_viewer_original.search_logs(str(p), "login")
    assert data["summary"]["matches"] == len(original)
    assert data["summary"]["total_lines"] == 3
