from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(validated_data=serializer.validated_data)
        login(request, user)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('User not found!')

        login(request, user)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
                'jwt': token,
            }

        return response


class UserView(APIView):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            raise AuthenticationFailed('Unauthenticated')

        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        logout(request)

        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'status': 200
        }

        return response