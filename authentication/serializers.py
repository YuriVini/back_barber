from rest_framework import serializers
from .models import UsersModel

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UsersModel
		fields = '__all__'
	def create(self, user_data):
		user_obj = UsersModel.objects.create(email=user_data['email'], username=user_data['username'], password=user_data['password'])
		user_obj.username = user_data['username']
		user_obj.save()
		return user_obj

class UserLoginSerializer(serializers.Serializer):
	class Meta:
		model = UsersModel
		fields = ('email', 'password')
		extra_kwargs = {
            'password': {'write_only': True}
        }
