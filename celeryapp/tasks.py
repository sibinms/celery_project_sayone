import logging
from celeryproject.celery import app

logger = logging.getLogger(__name__)


@app.task
def sample_task():
    logger.info("sample periodic celery task")

