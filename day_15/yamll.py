import yaml

with open('nrf.yaml') as f:
    data = yaml.safe_load(f)
    
# service=data["services"]["oai-amf"]
# list1=service.get("environment",[])
# dict1={}
# for i in list1:
#     if "=" in i:
#         key,value=i.split("=",1)
#         dict1[key]=value
        
    
# print("MCC =", dict1.get("MCC"))


# services = data.get("services",{})

# for service_name, service_data in services.items():
#     depends = service_data.get("depends_on")
#     dep_list = []
#     if not depends:
#         print(f"{service_name}: None")
#     else:
#         if isinstance(depends, list):
#             dep_list = depends
#         else:
#             dep_list= ["NA"]
        
#     depends_str = ", ".join(dep_list)
#     # print(f"{service_name}:{depends_str}")
    
#     ipv4 = "None"
#     networks = service_data.get("networks")
    
#     if networks:
#         for net_name, net_data in networks.items():
#             ipv4 = net_data.get("ipv4_address","None")
#             break
        
#     print(f"{service_name} --> depends on: {depends_str} -->| IP Address: {ipv4}")
    
services = data.get("services", {})

for service_name, service_data in services.items():
    depends = service_data.get("depends_on")
    dep_list = []

    if depends:
        if isinstance(depends, list):
            dep_list = depends
        else:
            dep_list = ["NA"]
    else:
        dep_list = ["None"]

    depends_str = ", ".join(dep_list)

    ipv4 = "None"
    networks = service_data.get("networks")

    if networks:
        for net_name, net_data in networks.items():
            ipv4 = net_data.get("ipv4_address", "None")
            break

    print(f"{service_name} --> depends on: {depends_str} -->| IP Address: {ipv4}")
