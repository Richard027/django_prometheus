'''django_prometheus.django_prometheus.views
'''
__author__ = "Philip Kershaw"
__date__ = "25 Jul 2019"
__copyright__ = "(C) 2019 UKRI"
__license__ = "license"
__contact__ = "Philip.Kershaw@stfc.ac.uk"
__all__ = []
from django.http import HttpResponse
from prometheus_client import Summary, Counter, generate_latest

# Create a metric to track time spent and requests made.
INDEX_TIME = Summary('index_request_processing_seconds', 
                     'DESC: INDEX time spent processing request')

# Create a metric to count the number of runs on process_request()
c = Counter('requests_for_host', 
            'Number of runs of the process_request method', 
            ['method', 'endpoint'])


@INDEX_TIME.time()
def index(request):
    label_dict = {"method": request.method, "endpoint": request.path}
    c.labels(**label_dict).inc()
    
    return HttpResponse("Hello, world.")


def metrics(request):
    return HttpResponse(generate_latest())
