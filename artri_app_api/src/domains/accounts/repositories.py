from src.models import User


class UserRepository:
    @staticmethod
    def create(*, username, email, password, first_name, last_name, birth_date, weight, height):
        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            weight=weight,
            height=height,
        )
