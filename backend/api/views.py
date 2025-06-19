from django.shortcuts import render
from api import serializer as api_serializer
from rest_framework_simplejwt.views import TokenObtainPairView
from userauths.models import User, Profile
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import random
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = api_serializer.RegisterSerializer


class ChangePasswordAPIView(generics.CreateAPIView):
    serializer_class = api_serializer.UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user_id = request.data["user_id"]
        old_password = request.data["old_password"]
        new_password = request.data["new_password"]

        user = User.objects.get(id=user_id)
        if user is not None:
            if check_password(old_password, user.password):
                user.set_password(new_password)
                user.save()
                return Response(
                    {"message": "Password changed successfully", "icon": "success"}
                )
            else:
                return Response(
                    {"message": "Old password is incorrect", "icon": "warning"}
                )
        else:
            return Response({"message": "User does not exists", "icon": "error"})


class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = api_serializer.UserSerializer

    def get_object(self):
        email = self.kwargs["email"]  # api/v1/password-email-verify/desphixs@gmail.com/

        user = User.objects.filter(email=email).first()

        if user:
            uuidb64 = user.pk
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh.access_token)

            user.refresh_token = refresh_token
            user.otp = generate_random_otp()
            user.save()

            link = f"http://localhost:5173/create-new-password/?otp={user.otp}&uuidb64={uuidb64}&refresh_token={refresh_token}"

            # context = {"link": link, "username": user.username}

            # subject = "Password Rest Email"
            # text_body = render_to_string("email/password_reset.txt", context)
            # html_body = render_to_string("email/password_reset.html", context)

            # msg = EmailMultiAlternatives(
            #     subject=subject,
            #     from_email=settings.FROM_EMAIL,
            #     to=[user.email],
            #     body=text_body,
            # )

            # msg.attach_alternative(html_body, "text/html")
            # msg.send()

            print("link ======", link)
        return user


def generate_random_otp(length=7):
    otp = "".join([str(random.randint(0, 9)) for _ in range(length)])
    return otp
