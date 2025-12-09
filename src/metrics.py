from prometheus_client import Gauge

cpu_usage_gauge = Gauge(
    "infra_cpu_usage_percent",
    "Mock CPU usage percentage"
)

memory_usage_gauge = Gauge(
    "infra_memory_usage_percent",
    "Mock memory usage percentage"
)

def update_mock_metrics():
    # deterministic mock values for MVP
    cpu_usage_gauge.set(65)
    memory_usage_gauge.set(70)