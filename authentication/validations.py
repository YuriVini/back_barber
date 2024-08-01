from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from authentication.user_services import UserService

from .models import UsersModel

def register_validation(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()

    if not username or not password or not email:
        raise ValidationError('Campos obrigatórios', 403)

    validate_email = EmailValidator('E-mail inválido', 403)

    validate_email(email)

    if not email or UsersModel.objects.filter(email=email).exists():
        raise ValidationError('E-mail já cadastrado', 403)

    if not password or len(password) < 8:
        raise ValidationError('Escolha uma senha maior, mínimo de 8 caracteres', 403)

    if not username:
        raise ValidationError('Campo de usuário obrigatório', 403)
    return data

def login_validation(data):
    email = data['email'].strip()
    password = data['password'].strip()

    if not email or not password:
        raise ValidationError('Campos obrigatórios', 403)

    if not UsersModel.objects.filter(email=email).exists():
        raise ValidationError('E-mail não cadastrado', 403)
    
    if password != UsersModel.objects.filter(email=email).get().password:
        raise ValidationError('Senha incorreta', 403)
    
    tokens = UserService().get_tokens_for_user(data)
    
    return tokens