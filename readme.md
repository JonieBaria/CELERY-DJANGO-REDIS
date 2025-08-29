run: celery -A scrapingapp worker --loglevel=info --pool=eventlet --concurrency=4
