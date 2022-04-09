from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    class meta:
        model = 'Doctor'
        fields = ['name', 'ssn', 'status', 'created_at', 'updated_at']


