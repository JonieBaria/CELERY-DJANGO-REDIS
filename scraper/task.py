import importlib
from celery import shared_task

@shared_task
def run_scraper(script_name):
    try:
        module_name = f"scraper.scraping_scripts.{script_name.replace('.py','')}"
        script = importlib.import_module(module_name)
        if hasattr(script, "main"):
            result = script.main()
            return result
        else:
            return f"{script_name} has no main() function."
    except Exception as e:
        return f"Error running {script_name}: {str(e)}"
