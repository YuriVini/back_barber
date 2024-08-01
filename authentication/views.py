from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status

from .serializers import UserRegisterSerializer, UserLoginSerializer
from .validations import register_validation, login_validation

class ResgisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(
        query_serializer=UserRegisterSerializer,
    )

    def post(self, request, *args, **kwargs):
        try:
            user_data = register_validation(request.data)
            serializer = UserRegisterSerializer(data=user_data)
            
            if serializer.is_valid(raise_exception=True):
                user = serializer.create(user_data)
                if user:
                    return Response({"data": "user created!"}, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(data=error, status=error.code)

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(
        query_serializer=UserLoginSerializer,
    )
    
    def post(self, request, *args, **kwargs):
        try:
            data = login_validation(request.data)
            
            return Response(data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data=error)

login = LoginView.as_view()
register = ResgisterView.as_view()