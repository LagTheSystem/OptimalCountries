import json

with open('countrydata.json', 'r') as file:
    data = json.load(file)

with open('othercountrydata.json', 'r') as file:
    otherdata = json.load(file)

ranks = []

for i in range(len(otherdata)):
    tfr_score = round(-(abs(float(otherdata[i]["tfr"]) - 2.1)), 2)
    ranks.append({
        "name": otherdata[i]["country"],
        "tfr_score": tfr_score,
        "imr": float(otherdata[i]["imr"]),
        "rni": float(otherdata[i]["rni"]),
    })

for i in range(len(data)):
    ranks[i]["gnipc"] = float(data[i]["gnipc_2022"]),
    ranks[i]["hdi"] = float(data[i]["hdi_2022"]),
    ranks[i]["life_expectancy"] = float(data[i]["le_2022"]),
    ranks[i]["education"] = float(data[i]["eys_2022"]),
    ranks[i]["gii"] = float(data[i]["gii_2022"]),
    print(float(data[i]["gii_2022"]))

ranks = sorted(ranks, key = lambda d: d["tfr_score"])
for i in range(len(ranks)):
    ranks[i]["tfr_score"] = i

# Stats that are better closer to zero must be reversed
ranks = sorted(ranks, key = lambda d: d["imr"], reverse=True)
for i in range(len(ranks)):
    ranks[i]["imr"] = i

#ranks = sorted(ranks, key = lambda d: d["gii"], reverse=True)
#for i in range(len(ranks)):
    #ranks[i]["gii"] = i

#print(ranks)