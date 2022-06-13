from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class ProductCreateController(APIView):
    def post(self,request):
        try:
            return Response(data={'status':'ok'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)