import json

txt_file = "C:/Users/ADMIN/OneDrive/Desktop/day_15/llog.txt"      # input file
json_file = "./llog.json"    # output file

routes = []

with open(txt_file, "r") as file:
    for line in file:
        parts = line.split()
        route_dict = {}

        # First part always route/network
        route_dict["route"] = parts[0]

        i = 1
        while i < len(parts):
            token = parts[i]

            # capture valid tokens
            if token in ["via", "dev", "proto", "scope", "src", "metric"]:
                route_dict[token] = parts[i+1]
                i += 1
            elif token == "linkdown":
                route_dict["linkdown"] = True
            i += 1

        routes.append(route_dict)

# Convert to JSON and save
json_data = json.dumps(routes, indent=4)

with open(json_file, "w") as f:
    f.write(json_data)

print("llog.txt converted to llog.json successfully!")


