from flask import jsonify


def make(error=None, message=None, response=None, code=200):
    assert error is not None
    response_dict = dict(error=error)
    if error:
        assert type(message) is str
        response_dict['message'] = message
    else:
        assert type(response) is dict
        response_dict['response'] = response
    response_dict = jsonify(response_dict)
    return response_dict, code
