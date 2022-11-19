from pathlib import Path
from werkzeug.datastructures import MultiDict, FileStorage, Headers


def test_app(client):
    endpoint = "process"
    attachment_path = Path("foo.bar")

    data = MultiDict()
    test_file = FileStorage(filename=attachment_path.name,
                            stream=attachment_path.open("rb"),
                            headers=Headers({"ID": "0"}))
    data.add("attachment", test_file)
    resp = client.post(path=endpoint, data=data)
    assert resp.status_code == 200
