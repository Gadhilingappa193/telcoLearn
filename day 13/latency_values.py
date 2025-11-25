latency_values = [20,30,35,67,89,34,67,88]

def calc_avg(data):
    return sum(data) / len(data)

def get_summary(data):
    minimum = min(data)
    maximum = max(data)
    average = calc_avg(data)
    
    return minimum, maximum, average
result = get_summary(latency_values)
print("Latency summary", result)
    