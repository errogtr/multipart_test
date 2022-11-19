from pathlib import Path
import requests

if __name__ == "__main__":
    url = "http://localhost:5000/process"
    attachment_path = Path("foo.bar")
    test_file = ("attachment", (attachment_path.name,
                                attachment_path.open("rb"),
                                "application/json",
                                {"ID": "0"}
                                )
                 )
    response = requests.post(url=url, files=[test_file])
    print(f"{response.status_code} {response.reason}\n{response.text}")
