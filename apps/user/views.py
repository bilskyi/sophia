from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from .emails import send_otp_via_email
from .serializers import *
from .models import User
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
import jwt, datetime


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(validated_data=serializer.validated_data)

        send_otp_via_email(serializer.data['email'])

        login(request, user)

        return Response({
            'status': 200,
            'message': 'Registration was successful, check your email',
            'data': serializer.data
        })


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        password = serializer.data['password']

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


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)

        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'status': 200,
            'message': 'user logged out'
        }

        return response
    

class VerifyOTPView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = VerifyUserOTPSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = request.user.email
            otp = serializer.data['otp']

            user = User.objects.filter(email=email)
            if not user.exists() or user[0].otp != otp:
                return Response({
                    'status': 400,
                    'message': 'Something went wrong',
                    'data': 'Invalid data'
                })
            
            user = user.first()
            user.is_verified = True
            user.save()
            return Response({
                "status": 200,
                "message": "You have successfully confirmed your account",
                "data": serializer.data
            })
        

class ResendOTPView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        email = request.user.email
        if request.user.is_verified:
            return Response({
                'status': '200',
                'message': 'User has already been verified'
            })
    
        send_otp_via_email(email)
        
        return Response({
            "status": 200,
            "message": "The OTP verification code was send",
        })