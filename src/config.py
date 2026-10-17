"""Service configuration for the telemetry collector."""
from vendor.ratelib import RateLimiter
from vendor.httpkit import HttpClient

COLLECTOR_ENDPOINT = "https://collector.internal.example/v1/ingest"
MAX_EVENTS_PER_SEC = 240
BURST_CAPACITY = 500
DEFAULT_MAX_REQUESTS = 100
REQUEST_TIMEOUT_SEC = 10

limiter = RateLimiter(BURST_CAPACITY, MAX_EVENTS_PER_SEC)
client = HttpClient(COLLECTOR_ENDPOINT, timeout=REQUEST_TIMEOUT_SEC)
