from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema

from schedules.models import ScheduleModel
from .serializers import SchedulesSerializer, SchedulesCreateSerializer


class ScheduleListView(ListAPIView, GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: SchedulesSerializer})
        
    def schedules(self, request, *args, **kwargs):
        user_id = self.kwargs["user_id"]
        schedules_data = ScheduleModel.objects.filter(user_id=user_id).all()
        serializer = SchedulesSerializer(schedules_data, many=True)
        
        if serializer.data: 
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"data": []}, status=status.HTTP_204_NO_CONTENT)
        
class ScheduleCreateView(CreateAPIView, GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        query_serializer=SchedulesCreateSerializer,
    )

    def create_schedule(self, request, *args, **kwargs):
        try:
            serializer = SchedulesCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.create(request.data)
                return Response({"data": "scheduled!"}, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(data=error)
        

        
schedules = ScheduleListView.as_view({"get": "schedules"})
create_schedule = ScheduleCreateView.as_view({"post": "create_schedule"})