from rest_framework import serializers
from .models import ReportJob


class ReportJobSerializer(serializers.ModelSerializer):

    download_url = serializers.SerializerMethodField()

    class Meta:
        model = ReportJob
        fields = [
            "id",
            "status",
            "created_at",
            "completed_at",
            "download_url",
        ]

    def get_download_url(self, obj):

        if obj.file:
            request = self.context.get("request")
            return request.build_absolute_uri(obj.file.url)

        return None