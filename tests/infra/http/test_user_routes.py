from http import HTTPStatus

from faker import Faker

fake = Faker()


def test_user_routes_get_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': 'get_users'}


def test_user_routes_post_users(client):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    sut = client.post(
        '/users',
        json={'email': email, 'username': username, 'password': password},
    )

    assert sut.status_code == HTTPStatus.CREATED
    assert isinstance(sut.json()['id'], int)
    assert isinstance(sut.json()['created_at'], str)
    assert isinstance(sut.json()['updated_at'], str)
    assert sut.json()['email'] == email
    assert sut.json()['username'] == username
    assert not hasattr(sut, 'id')


def test_user_routes_post_users_exception(client):
    username = None
    email = None
    password = None
    sut = client.post(
        '/users',
        json={'email': email, 'username': username, 'password': password},
    )

    assert sut.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert sut.json()['detail'][0]['loc'][1] == 'email'
    assert sut.json()['detail'][1]['loc'][1] == 'password'
    assert sut.json()['detail'][2]['loc'][1] == 'username'
