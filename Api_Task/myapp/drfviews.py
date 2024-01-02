from .models import *
from rest_framework.views import APIView
from .serializars import *
from rest_framework.response import Response
from rest_framework import status 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework .authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken


# session  authentication
class RegisterUser(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = UserSerializar(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created successfully'},status=status.HTTP_201_CREATED)
        else:
            user = User.objects.get(username=serializer.data['username'])
            # toke_obj  = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#--------------------------------------

class PersonAPI(APIView):
    def get(self,request,pk=None):
        if pk == None:
            per_data = Person.objects.all()
            serializer = PersonSerializar(per_data,many=True)
            return Response(serializer.data) 
        else:
            per_data = Person.objects.get(id = pk)
            serializer = PersonSerializar(per_data)
            return Response(serializer.data) 
            
    
    def post(self,request):
        serializer = PersonSerializar(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        per_data = Person.objects.get(id=pk)
        serializer = PersonSerializar(per_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated successfully'},status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def patch(self,request):
        per_data = Person.objects.get(id=pk)
        serializer = PersonSerializar(per_data,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated successfully'},status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,pk=None):
        per_data = Person.objects.get(id=pk)
        per_data.delete()
        return Response({'msg':'data deleted successfully'},status=status.HTTP_204_NO_CONTENT)
    
    
class ImageAPI(APIView):
        def get(self,request,pk=None):
            if pk == None:
                img_data = Image.objects.all()
                serializer = ImageSerializer(img_data,many=True)
                return Response(serializer.data) 
            else:
                img_data = Image.objects.get(id = pk)
                serializer = ImageSerializer(img_data)
                return Response(serializer.data) 
            
        
     