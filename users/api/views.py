from rest_framework.views import APIView
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserRegisterSerializer

class RegisterView(APIView):
    def post(self, request):
      serializer = UserRegisterSerializer(data=request.data)
      
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=status.HTTP_200_OK, data={
          'message':'success',
          'user':serializer.data
        })
      
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      



