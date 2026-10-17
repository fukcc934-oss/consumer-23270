"""Service configuration for the telemetry collector."""
from vendor.ratelib import RateLimiter

COLLECTOR_ENDPOINT = "https://collector.internal.example/v1/ingest"
MAX_EVENTS_PER_SEC = 240
BURST_CAPACITY = 500

limiter = RateLimiter(BURST_CAPACITY, MAX_EVENTS_PER_SEC)
