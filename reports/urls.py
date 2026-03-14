from django.urls import path
from .views import GenerateReportView, ReportStatusView

urlpatterns = [
    path("generate/", GenerateReportView.as_view()),
    path("<uuid:job_id>/", ReportStatusView.as_view()),
]