from django.contrib.auth.hashers import make_password
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from api.models import TempAuth, User
from api.serializers.userserializer import (EmailSerializer,
                                            TempAuthRegistrationSerializer)
from api_yamdb.settings import EMAIL_HOST_USER


def send_msg(email, code):
    subject = 'Отправка кода потверждения'
    body = f'''
        {code}
    '''
    send_mail(
        subject, body,
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=True
    )


@api_view(['POST'])
def send_code(request):
    serializer = EmailSerializer(data=request.data)
    if not serializer.is_valid():
        email = request.data.get("email")
        raise serializer.ValidationError(
            f'this email {email} is not available'
        )
    email = serializer.validated_data.get('email')
    confirmation_code = make_password('')

    TempAuth.objects.create(
        email=email,
        confirmation_code=confirmation_code)
    try:
        send_msg(email, confirmation_code)
    except BadHeaderError:
        return Response('Invalid header found.')
    return Response(serializer.data, )


@api_view(['POST'])
def get_jwt_token(request):
    serializer = TempAuthRegistrationSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        raise serializers.ValidationError(
            'Invalid email or confirmation code'
        )
    email = serializer.validated_data.get('email')
    code = serializer.validated_data.get('conf_code')
    if TempAuth.objects.filter(
        email=email,
        conf_code=code
    ).exists():
        username = email.split('@')[0]
        user = User.objects.create(
            email=email,
            username=username,
            confirmation_code=code
        )
        code_registration = get_object_or_404(
            TempAuth,
            email=email,
            confirmation_code=code
        )
        code_registration.delete()
        access_token = AccessToken.for_user(user)
        return Response({'token': f'{access_token}'})
    user = get_object_or_404(User, email=email, confirmation_code=code)
    access_token = AccessToken.for_user(user)
    return Response({'token': f'{access_token}'})
