
import time

requests_log = {}

def rate_limit(user_ip):
    current_time = time.time()

    if user_ip not in requests_log:
        requests_log[user_ip] = []

    # keep last 60 sec
    requests_log[user_ip] = [
        t for t in requests_log[user_ip] if current_time - t < 60
    ]

    if len(requests_log[user_ip]) >= 5:
        raise Exception("Rate limit exceeded")

    requests_log[user_ip].append(current_time)
