from rest_framework import serializers

from api.models import Contact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'User'
        fields = ['name', 'email','type', 'status','created_at','updated_at']

class ClinicSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = 'Clinic'
        fields = ['name', 'ssn', 'status', 'created_at', 'updated_at', 'user']

class ContactSerialzer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta: 
        model = Contact
        fields = ['key', 'value', 'status', 'created_at', 'updated_at', 'user']

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    speciality = SpecialitySerializer()

    class Meta:
        model = 'Doctor'
        fields = ['name', 'ssn', 'status', 'created_at', 'updated_at', 'user', 'speciality']

class SpecialitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = 'Speciality'
        fields = ['name', 'description', 'parent', 'status', 'created_at', 'updated_at']
