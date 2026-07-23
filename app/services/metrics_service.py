from prometheus_client import Counter, Histogram

# Counts every HTTP request
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of HTTP requests received"
)

# Measures request duration
REQUEST_DURATION = Histogram(
    "app_request_duration_seconds",
    "Time spent processing HTTP requests"
)