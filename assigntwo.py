import psutil
import time
import logging

def monitor_cpu(threshold=80, check_interval=1, alert_cooldown=5):
    """
    Monitor the CPU usage and alert if it exceeds the given threshold.

    Args:
    threshold (int): The CPU usage percentage that, if exceeded, will trigger an alert.
    check_interval (int): The interval (in seconds) between CPU usage checks.
    alert_cooldown (int): The minimum time (in seconds) between consecutive alerts.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info("Monitoring CPU usage... Press Ctrl+C to stop.")
    
    last_alert_time = 0

    try:
        while True:
            # Get the current CPU usage as a percentage over the check interval
            cpu_usage = psutil.cpu_percent(interval=check_interval)
        
            # Check if CPU usage exceeds the threshold
            if cpu_usage > threshold:
                current_time = time.time()
                if current_time - last_alert_time > alert_cooldown:
                    logging.warning(f"Alert! CPU usage exceeds threshold: {cpu_usage:.2f}%")
                    last_alert_time = current_time
            
            # Pause for the specified check_interval
            time.sleep(check_interval)
    
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Set the CPU usage threshold and monitoring parameters (can be modified as needed)
    cpu_threshold = 80
    check_interval = 1
    alert_cooldown = 5
    
    # Start monitoring CPU usage
    monitor_cpu(threshold=cpu_threshold, check_interval=check_interval, alert_cooldown=alert_cooldown)
