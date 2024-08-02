from rest_framework import serializers

from schedules.models import ScheduleModel

class SchedulesSerializer(serializers.Serializer):
	day_of_week = serializers.CharField()
	barber_name = serializers.CharField()
	hour = serializers.CharField()
	type = serializers.CharField()

class SchedulesCreateSerializer(serializers.Serializer):
	day_of_week = serializers.CharField()
	barber_name = serializers.CharField()
	hour = serializers.CharField()
	type = serializers.CharField()
	user_id = serializers.CharField()

	def create(self, user_data):
		schedule_data = ScheduleModel.objects.create(day_of_week=user_data['day_of_week'], barber_name=user_data['barber_name'], hour=user_data['hour'], type=user_data['type'])
		schedule_data.save()
		return schedule_data