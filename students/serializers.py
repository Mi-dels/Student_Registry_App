from .models import Students, UserProfile
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction


# User = get_user_model()


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = [ "url" , "id", "firstname","lastname","email" , "age", "gender", "department", "created_at"]

    def validate_email(self,value):
        value = value.lower()
        if not (value.endswith('@gmail.com') or value.endswith('@yahoo.com')):
            raise serializers.ValidationError("We only accept Gmail or Yahoo Email Accounts.")
        return value


    def validate_age(self,value):
        if value < 18:
            raise serializers.ValidationError("Only students aged 18 and above are eligble for this record")
        return value







class MyCustomSignupSerializer(RegisterSerializer):
    # These are the extra fields you want for the Profile
    phone_number = serializers.CharField(max_length=15, required=False)
    bio = serializers.CharField(required=False, allow_blank=True)

    # Wrap the save in a 'transaction' to ensure if one table fails, 
    # the other doesn't save either (no "ghost" users).
    @transaction.atomic
    def save(self, request):
        # 1. Standard dj-rest-auth magic saves 'username', 'email', 'password' 
        # into the core Django User table for you.
        user = super().save(request)
        
        # 2. Extract your extra fields from the validated data
        phone = self.validated_data.get('phone_number', '')
        bio = self.validated_data.get('bio', '')
        
        # 3. Create the row in your UserProfile table and link it to the user
        UserProfile.objects.create(user=user, phone_number=phone, bio=bio)
        
        return user

    #     if username and password:
    #         user = authenticate(username=username, password=password)

    #         if user is None:
    #             raise serializers.ValidationError("Invalid Credentials")
        





