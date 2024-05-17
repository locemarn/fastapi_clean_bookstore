# import re
#
#
# class UserEntity:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password
#
#     @classmethod
#     def __is_valid_email(cls, value) -> str | None:
#         regex = re.compile(
#             r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
#         )
#         r = re.fullmatch(regex, value)
#         return r
#
#     @property
#     def username(self):
#         return self._username
#
#     @property
#     def email(self):
#         return self._email
#
#     @property
#     def password(self):
#         return self._password
#
#     @username.setter
#     def username(self, value):
#         if type(value) is not str:
#             raise TypeError('username must be a string')
#
#         if not str(value):
#             raise ValueError('username cannot be empty')
#
#         self._username = value
#
#     @email.setter
#     def email(self, value):
#         if type(value) is not str:
#             raise TypeError('Email must be a string')
#
#         if not str(value):
#             raise ValueError('Email cannot be empty')
#
#         if not self.__is_valid_email(value):
#             raise ValueError('Invalid email address')
#
#         self._email = value
#
#     @password.setter
#     def password(self, value):
#         if type(value) is not str:
#             raise TypeError('Password must be a string')
#
#         if not str(value):
#             raise ValueError('Password cannot be empty')
#
#         self._password = value
