import json
import logviewer
import log_viewer_original


def test_semantic_matches(tmp_path):
    p = tmp_path / "t.log"
    p.write_text("1 login\n2 nothing\n3 login\n")
    enhanced = logviewer.search_logs(str(p), "login", fmt="json")
    data = json.loads(enhanced)
    orig = log_viewer_original.search_logs(str(p), "login")
    # compare raw texts
    enhanced_raws = [r["text"] for r in data["results"]]
    assert enhanced_raws == orig
