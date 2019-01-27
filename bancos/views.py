from bancos.models import Banco
from rest_framework import views 
from bancos.serializers import BancoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#class AddBancoView(views.APIView):
#    serializer_class=BancoSerializer
#    def post(self, request, *args, **kwargs):
#        try:
#            banco_serializer = BancoSerializer(data=request.data)
#            if banco_serializer.is_valid():
#                banco_serializer.save()
#                return Response(banco_serializer.data, status=status.HTTP_201_CREATED)
#            else:
#                return Response(banco_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#        except Exception as e:
#            return Response({"error": True, "value_error": e.args}, status=status.HTTP_400_BAD_REQUEST)

class AddBancoView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
