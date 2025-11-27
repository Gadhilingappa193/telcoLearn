import yaml

# Load YAML
with open("nrf.yaml") as f:
    data = yaml.safe_load(f)

services = data.get("services", {})

print("===== LIST OF NF PORTS PER SERVICE =====")
for service_name, service_data in services.items():
    env_list = service_data.get("environment", [])
    ports = []

    for item in env_list:
        # Environment entries like: "NRF_PORT=80"
        if "=" in item:
            key, value = item.split("=", 1)

            # Filter keys containing PORT or ending with _PORT
            if "PORT" in key:
                ports.append(f"{key}={value}")

    if ports:
        print(f"{service_name}: {', '.join(ports)}")
    else:
        print(f"{service_name}: No NF_PORT variables found")

    ip_address = "None"
    networks = service_data.get("networks")
    if networks:
        for net_name, net_data in networks.items():
            ip_address = net_data.get("ipv4_address", "None")
            break

    # ------- Print Result -------
    ports_str = ", ".join(ports) if ports else "No PORT Variables"
    print(f"{service_name}:  IP={ip_address}  -->  PORTS= {ports_str}")