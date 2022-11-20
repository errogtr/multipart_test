### Description
This is a minimal working example of the Werkzeug issue <insert_url>.

It contains a Flask app which parses a multipart request containing an "attachment" file enriched with an "ID"
custom header. The app returns `200` if the header is present and another status code otherwise.

### Setup
To create a minimal virtual environment run
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### Webapp calls
To run the flask app copy the commands
```shell
$ export FLASK_APP=api/__init__:create_app
$ python3 -m flask run -p 5000
```
To send a simple request open a new terminal and run
```shell
$ curl -X POST -F 'attachment=@foo.bar;headers="ID:0000"' http://localhost:5000/process
```
this should print the response
```shell
STATUS 200 result {'ID': '0000'}
```
If instead the attachment header is omitted, the result is
```shell
$ curl -X POST -F 'attachment=@foo.bar' http://localhost:5000/process
STATUS 9999 ID not found
```
For the meaning of the response status in this case, see next section.

### Integration test
To run the unique integration test in the `tests` folder, run
```shell
python3 -m pytest tests
```
The test is expected to be successful, while at the moment an assertion error is raised
```shell
FAILED tests/test_app.py::test_app - assert 9999 == 200
```
The value `9999` is chosen to make sure that the test fails exactly
because the custom headers is lost somewhere in the request handling by
the mocked Flask client.

