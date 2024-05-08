from sqlalchemy import select

from src.domain.models.user_model import UserModel


def test_create(session):
    new_user = UserModel(
        username='test', email='test@email.com', password='secret'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(UserModel).where(UserModel.username == 'test')
    )
    assert user.username == 'test'
