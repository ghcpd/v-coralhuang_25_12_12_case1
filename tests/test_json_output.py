import json
import logviewer


def test_json_structure(tmp_path):
    p = tmp_path / "t.log"
    p.write_text("2025-03-01T00:00:00 event=login user=u1\n")
    out = logviewer.search_logs(str(p), "login", fmt="json")
    data = json.loads(out)
    assert "summary" in data
    assert "results" in data
    assert isinstance(data["results"], list)
    r = data["results"][0]
    assert "line" in r and "text" in r and "highlighted" in r
    assert "<<login>>" in r["highlighted"]
