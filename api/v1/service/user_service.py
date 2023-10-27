from api.v1.domain.user.user import User


async def get_users():
    user = (User.builder()
            .name("None11")
            .build())

    return user
