from celery import shared_task
from django.utils import timezone
from django.core.files.base import ContentFile
from .models import ReportJob
import time


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 3})
def generate_report(self, job_id):

    try:
        job = ReportJob.objects.get(id=job_id)

        job.status = "PROCESSING"
        job.save()
        # stimulating heavy process here 
        time.sleep(5)

        rows = [
            ["Name", "Email", "Age"],
            ["Pavan", "pavan@gmail.com", 22],
            ["Ajay", "ajay@gmail.com", 30],
            ["Sai Local", "sai@test.com", 23],
        ]

        csv_content = ""

        for row in rows:
            csv_content += ",".join(map(str, row)) + "\n"

        file_name = f"report_{job_id}.csv"

        job.file.save(file_name, ContentFile(csv_content))

        job.status = "SUCCESS"
        job.completed_at = timezone.now()
        job.save()

    except Exception as e:

        job.status = "FAILED"
        job.save()

        raise e