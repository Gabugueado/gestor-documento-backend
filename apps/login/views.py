from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.authentication import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated

class UserInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # El usuario conectado se encuentra en request.user
        return Response({
            'username': user.username,
            'email': user.email,
            # Agrega otros campos del usuario que desees exponer
        }, status=status.HTTP_200_OK)
