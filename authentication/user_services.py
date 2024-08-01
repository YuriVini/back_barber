from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import UsersModel

class UserService():
    def get_tokens_for_user(self, user):
        model_user = UsersModel.objects.filter(email=user["email"]).get()
        refresh = RefreshToken.for_user(model_user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }