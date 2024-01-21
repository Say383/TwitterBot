import psutil
import time
from cachetools import cached, TTLCache

class PerformanceMonitor:
    def __init__(self):
        self.process = psutil.Process()

    def log_resource_usage(self):
        cpu_usage = self.process.cpu_percent(interval=1)
        memory_usage = self.process.memory_info().rss
        print(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage} bytes")

    @cached(cache=TTLCache(maxsize=100, ttl=300))
    def get_cached_response(self, data):
        # Process and return response for the given data
        time.sleep(2)  # Simulate processing time
        return f"Processed data: {data}"

# Example usage
performance_monitor = PerformanceMonitor()
performance_monitor.log_resource_usage()
cached_response = performance_monitor.get_cached_response("sample data")
