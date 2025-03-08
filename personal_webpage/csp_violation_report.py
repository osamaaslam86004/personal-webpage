import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Set up a logger for CSP reports
logger = logging.getLogger("csp")


@csrf_exempt  # CSP reports are sent via POST, so CSRF protection should be disabled
def csp_violation_report(request):
    if request.method == "POST":
        try:
            report_data = json.loads(request.body.decode("utf-8"))
            logger.warning(f"CSP Violation Report: {json.dumps(report_data, indent=2)}")
        except json.JSONDecodeError:
            logger.error("Invalid CSP report received")
        return JsonResponse({"status": "Report received"}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)
