from rest_framework import serializers
from .models import * 




class NatalFirstTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Natal_First_Time_Table
        fields = '__all__'                                             

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Registration_Table
        fields = '__all__' 

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Setting_Table
        fields = '__all__' 
