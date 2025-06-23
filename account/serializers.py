from django.forms import ValidationError
from .models import  User
from rest_framework import serializers

    
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail  # or your email backend

from django.utils.encoding import smart_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['email','name','tc','password','password2']
    
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        
        if password != password2:
            raise serializers.ValidationError("Password not match")
        
        return attrs
    
    def create(self, validated_data):
        # Remove password2 before passing to model
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)
    
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = User
        fields = ['email','password']
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email']
        
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 255)
    password2 = serializers.CharField(max_length = 255)
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        
        if password != password2:
            raise serializers.ValidationError("Password not match")
        
        return attrs


User = get_user_model()

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            reset_link = f"http://localhost:3000/reset-password/{uid}/{token}"  # Change to your frontend URL

            # Optionally: Send email
            send_mail(
                subject="Reset your password",
                message=f"Click the link to reset your password: {reset_link}",
                from_email="noreply@example.com",
                recipient_list=[user.email],
                fail_silently=False,
            )

        # Always return success even if user doesn't exist — for security
        return attrs



class ConfirmPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255)
    password2 = serializers.CharField(max_length=255)
    token = serializers.CharField()
    uid = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        uid = attrs.get('uid')
        token = attrs.get('token')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match")

        try:
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
        except (User.DoesNotExist, DjangoUnicodeDecodeError):
            raise ValidationError("Invalid UID")

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise ValidationError("Token is invalid or expired")

        attrs['user'] = user  # pass user to view
        return attrs
