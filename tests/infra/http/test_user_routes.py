from http import HTTPStatus

from starlette.testclient import TestClient

# from faker import Faker
#
# fake = Faker()


def test_user_routes_get_users() -> None:
    # print('client', client)
    sut = client.get('/users')
    assert sut.status_code == HTTPStatus.OK
    print('sut', sut.json())
    # assert sut.json() == []
