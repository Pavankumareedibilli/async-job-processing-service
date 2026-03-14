# Register your models here.

from django.contrib import admin
from .models import ReportJob


@admin.register(ReportJob)
class ReportJobAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "created_at", "completed_at")