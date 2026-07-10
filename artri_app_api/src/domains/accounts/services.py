from .repositories import UserRepository


class RegistrationService:
    @staticmethod
    def register(validated_data):
        return UserRepository.create(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            birth_date=validated_data.get('birth_date', None),
            weight=validated_data.get('weight', None),
            height=validated_data.get('height', None),
        )
