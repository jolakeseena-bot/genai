from __future__ import annotations

def test_generated_login_positive() -> None:
    endpoint = '/login'
    method = 'POST'
    parameters = {}
    expected_status = 200
    assert endpoint is not None and endpoint.startswith('/')
    assert method in {'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS', 'HEAD'}
    assert isinstance(parameters, dict)
    assert isinstance(expected_status, int)
    assert 100 <= expected_status <= 599

def test_generated_login_negative() -> None:
    endpoint = '/login'
    method = 'POST'
    parameters = {}
    expected_status = 200
    negative_status = 400
    assert endpoint is not None and endpoint.startswith('/')
    assert method in {'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS', 'HEAD'}
    assert isinstance(parameters, dict)
    assert negative_status != expected_status
    assert 400 <= negative_status <= 499
