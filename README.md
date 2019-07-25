# django_prometheus
Demo project to show integration of Python prometheus client with a Django app

## Testing
Run Django app:
```bash
python manage.py runserver
```

Try querying instrumented endpoint:
```bash
while [ 1 ]; do sleep 2; curl http://localhost:8000; done
```

Then check metrics endpoint:
```bash
curl http://localhost:8000/metrics
```

