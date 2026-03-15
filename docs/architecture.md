# System Architecture

The service processes long-running report generation tasks asynchronously.

Flow:

Client → Django API → Redis Queue → Celery Worker → CSV File Generated

Components:

* Django REST API: Accepts requests and creates jobs.
* Redis: Acts as a message broker.
* Celery Worker: Processes background tasks.
* Database: Stores job metadata.
* File Storage: Stores generated CSV reports.
