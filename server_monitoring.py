# cpu_monitor.py
import psutil
import time

THRESHOLD = 10

def monitor_cpu(threshold=THRESHOLD, interval=1):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=interval)

            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

            # Sleep for a short time before checking again (optional, to reduce CPU load)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

monitor_cpu()