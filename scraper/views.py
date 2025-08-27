# from django.shortcuts import render
# from scrapingapp.celery import debug_task

# # Create your views here.
# def index(request):
#     debug_task.delay()
#     return render(request, 'index.html')
import os
from django.conf import settings
from django.shortcuts import render
from .task import run_scraper

SCRIPTS_FOLDER = os.path.join(settings.BASE_DIR, "scraper", "scraping_scripts")

def index(request):
    scripts = [f for f in os.listdir(SCRIPTS_FOLDER) if f.endswith(".py")]
    result = None

    if request.method == "POST":
        script_name = request.POST.get("script_name")
        task = run_scraper.delay(script_name)  # 👈 enqueue Celery task
        result = f"Task {task.id} submitted. Refresh later to see result."

    return render(request, "index.html", {"scripts": scripts, "result": result})
