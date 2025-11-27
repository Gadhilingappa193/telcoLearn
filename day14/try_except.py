import subprocess
import logging
logging.basicConfig(filename='log.txt', level=logging.WARNING)
logging.debug("This is debug")
logging.info("program started")
logging.warning('warning WARNING =======')
logging.error('error information')
logging.critical('critical in info')

ip_list = ["1.168.1.13","8.8.8.8","10.0.0.1","127.0.0.1","0.0.0.0"]

for i in ip_list:
    try:
        result = subprocess.run(
            ["ping", "-c", "1", i],
            stdout=subprocess.DEVNULL,
            timeout=0.01  # ⏱ timeout added
        )

        if result.returncode == 0:
            print(f"IP address {i} is reachable.")
        else:
            print(f"IP address {i} is unreachable.")

    except subprocess.TimeoutExpired:
        print(f"IP address {i} ping is slow (timeout).")

