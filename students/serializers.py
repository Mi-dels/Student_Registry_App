from .models import Students
from rest_framework import serializers


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