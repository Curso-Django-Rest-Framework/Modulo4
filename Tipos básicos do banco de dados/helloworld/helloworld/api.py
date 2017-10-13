from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        return Response(status=200, data={'mensagem': request.data})
