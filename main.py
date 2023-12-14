import requests

with open("uni.txt", "r") as f:
    data = f.readlines()

sorted_data = sorted(data)

for line in sorted_data:
    print(line)
