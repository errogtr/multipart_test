from flask import current_app, request, make_response


@current_app.route("/process", methods=["POST"])
def process_request_api():
    attachment = request.files.get("attachment")
    content = attachment.stream.read().decode()
    headers = attachment.headers
    try:
        result = next({k: v} for k, v in headers.items() if k == "ID")
        response = make_response(f"STATUS 200 result {result}\n")
    except StopIteration:
        status = 9999
        response = make_response(f"STATUS {status} ID not found\n", status)
    return response
