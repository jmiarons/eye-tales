from flask import jsonify


def make(error, message, code=200):
    response_dict = dict(error=error)
    assert type(message) is str
    response_dict['message'] = message
    response_dict = jsonify(response_dict)
    return response_dict, code
