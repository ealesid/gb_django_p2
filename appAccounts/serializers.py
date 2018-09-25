from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField, DateField, EmailField
from rest_framework.validators import UniqueValidator


class UsersSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'date_joined', 'is_active', )

    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    )

    password = CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
