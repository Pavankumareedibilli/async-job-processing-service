from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ReportJob
from .tasks import generate_report
from .serializers import ReportJobSerializer


class GenerateReportView(APIView):

    def post(self, request):

        job = ReportJob.objects.create()

        generate_report.delay(str(job.id))

        return Response({
            "job_id": job.id,
            "status": job.status
        }, status=status.HTTP_202_ACCEPTED)


class ReportStatusView(APIView):

    def get(self, request, job_id):

        try:
            job = ReportJob.objects.get(id=job_id)
        except ReportJob.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)

        serializer = ReportJobSerializer(job, context={"request": request})

        return Response(serializer.data)