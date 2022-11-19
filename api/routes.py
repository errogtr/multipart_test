from flask import current_app, request, make_response


@current_app.route("/process", methods=["POST"])
def process_request_api():
    attachment = request.files.get("attachment")
    headers = attachment.headers
    try:
        my_header = next({k: v} for k, v in headers.items() if k == "ID")
        response = make_response(my_header)
    except StopIteration:
        response = make_response({"ID": "not found"}, 400)
    return response
