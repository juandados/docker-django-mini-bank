from rest_framework import serializers
from bancos.models import Banco

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ('name', 'date_created')
        read_only_fields = ('date_created', 'date_modified') 
