from api.v1.decorator.builder import builder


@builder
class User:
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __str__(self):
        return f'User(name={self.name}, email={self.email})'

    @classmethod
    def get_users(cls):
        return [{"user_id": 1}, {"user_id": 2}]
