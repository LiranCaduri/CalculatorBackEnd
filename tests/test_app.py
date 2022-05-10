from App import cache

error_msg = """ERORR:
            Please enter only TWO valid numbers and ONE operator
            or ONE number and ONE operator to continue a Calculation!"""

division_zero_msg = "Error: Division in 0"


def test_index_addition(client):
    body = {
        "operator": "+",
        "number1": "10",
        "number2": "10"
    }

    response = client.post('/', data=body)
    assert response.status_code == 200
    assert response.json["answer"] == '20.0'

    body["number1"] = "k"
    response = client.post('/', data=body)

    assert response.json["error"] == error_msg


def test_index_substruct(client):
    body = {
        "operator": "-",
        "number1": "10",
        "number2": "10"
    }

    response = client.post('/', data=body)
    assert response.status_code == 200
    assert response.json["answer"] == '0.0'

    body["number1"] = "k"
    response = client.post('/', data=body)

    assert response.json["error"] == error_msg


def test_index_multiply(client):
    body = {
        "operator": "*",
        "number1": "10",
        "number2": "10"
    }

    response = client.post('/', data=body)
    assert response.status_code == 200
    assert response.json["answer"] == '100.0'

    body["number1"] = "k"
    response = client.post('/', data=body)

    assert response.json["error"] == error_msg


def test_index_division(client):
    body = {
        "operator": "/",
        "number1": "10",
        "number2": "10"
    }

    response = client.post('/', data=body)
    assert response.status_code == 200
    assert response.json["answer"] == '1.0'

    body["number2"] = "0"
    response = client.post('/', data=body)
    assert response.json["error"] == division_zero_msg

    body["number1"] = "k"
    body["number2"] = "10"
    response = client.post('/', data=body)

    assert response.json["error"] == error_msg


def test_index_one_number_addition(client):
    body = {
        "operator": "+",
        "number1": "20",
    }

    cache["last_answer"] = 0  # reset last answer to continue testing

    response = client.post('/', data=body)
    assert response.status_code == 200
    assert response.json["answer"] == '20.0'

    body["number1"] = "k"
    response = client.post('/', data=body)

    assert response.json["error"] == error_msg


def test_index_one_number_substruct(client):
    body = {
        "operator": "-",
        "number1": "10",
    }

    response = client.post('/', data=body)
    assert response.status_code == 200
    assert response.json["answer"] == '10.0'

    body["number1"] = "k"
    response = client.post('/', data=body)

    assert response.json["error"] == error_msg


def test_index_one_number_multiply(client):
    body = {
        "operator": "*",
        "number1": "10"
    }

    response = client.post('/', data=body)
    assert response.status_code == 200
    assert response.json["answer"] == '100.0'

    body["number1"] = "k"
    response = client.post('/', data=body)

    assert response.json["error"] == error_msg


def test_index_division(client):
    body = {
        "operator": "/",
        "number1": "10",
    }

    response = client.post('/', data=body)
    assert response.status_code == 200
    assert response.json["answer"] == '10.0'

    body["number2"] = "0"
    response = client.post('/', data=body)
    assert response.json["error"] == division_zero_msg

    body["number1"] = "k"
    body["number2"] = "10"
    response = client.post('/', data=body)

    assert response.json["error"] == error_msg
