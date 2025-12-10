import time
import random

log = []

def fake_api_call():
    # 30% failure chance
    if random.random() < 0.3:
        return {"success": False, "error": "Temporary failure"}
    return {"success": True, "data": random.randint(100, 999)}

def poll_with_retry(max_retries=3):
    attempt = 0
    while attempt < max_retries:
        result = fake_api_call()
        log.append({"attempt": attempt + 1, "result": result})

        if result["success"]:
            return result

        attempt += 1
        time.sleep(attempt)  # backoff 1 → 2 → 3 sec

    return {"success": False, "error": "All retries failed"}

print(poll_with_retry())
print("Log:", log)
