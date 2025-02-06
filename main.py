import json
from types import SimpleNamespace

with open('countrydata.json', 'r') as file:
    data = json.load(file)

ranks = []

def clamp(n, min, max): 
    if n < min: 
        return min
    elif n > max: 
        return max
    else: 
        return n 

for i in range(len(data)):
    hdi = int(data[i]["hdi_2022"])
    life_expectancy = data[i]["le_2022"] / 87
    schooling_score = data[i]["eys_2022"] / 22
    gni_score = clamp(data[i]["gnipc_2022"] / 75000, 0, 1)
    ranks.append({
        "name": data[i]["Country"],
        "total": (hdi + life_expectancy + schooling_score + gni_score) / 4
    })
    #print(str(rankings[i]["name"]) + ": " + str(rankings[i]["hdi"]) + "  " + str(rankings[i]["life_expectancy_score"]) + "  " + str(rankings[i]["schooling_score"]) + "  " + str(rankings[i]["gni_score"]))
    #print(str(ranks[i]["name"] + ": " + str(ranks[i]["total"])))

sorted_ranks = sorted(ranks, key = lambda d: d["total"])
print(sorted_ranks)

with open("rank.json", "w") as f:
    json.dump(sorted_ranks, f)




