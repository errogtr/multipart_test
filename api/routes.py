from flask import current_app, request, make_response


@current_app.route("/process", methods=["POST"])
def process_request_api():
    attachment = request.files.get("attachment")
    headers = attachment.headers
    try:
        result = next({k: v} for k, v in headers.items() if k == "ID")
        status_code = 200
    except StopIteration:
        result = {"ID": "not found"}
        status_code = 9999
    result.update(status=status_code)
    return make_response(result)
