import os

def ip_reachability_tester():
    ip = input("Enter an IP address to ping: ")
    
    print(f"Pinging {ip} ...")
    
    # -n is for Windows, -c is for Linux/Mac
    command = f"ping -n 1 {ip}" if os.name == "nt" else f"ping -c 1 {ip}"
    
    response = os.system(command)
    
    if response == 0:
        print(f"{ip} is reachable ✔")
    else:
        print(f"{ip} is NOT reachable ✖")


# ---- Task 2 Functions ----
def calculate_average(data):
    return sum(data) / len(data)

def get_summary(data):
    return {
        "Min": min(data),
        "Max": max(data),
        "Average": calculate_average(data)
        
    }


# ---- Task 3: Menu-Driven CLI Tool ----
while True:
    print("\n===== MENU =====")
    print("1. IP Reachability Tester")
    print("2. Latency Summary Calculator")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        ip_reachability_tester()

    elif choice == "2":
        user_input = input("Enter comma-separated latency values: ")
        try:
            latency_list = list(map(float, user_input.split(",")))
            summary = get_summary(latency_list)
            print("Latency Summary:", summary)
        except ValueError:
            print("Invalid input! Please enter numbers separated by commas.")

    elif choice == "3":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
