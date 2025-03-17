import json

with open('filtered_country_data.json', 'r') as file:
    data = json.load(file)

data_types = ["tfr_score", "imr", "gii", "education", "life_expectancy", "gnipc", "rni", "hdi", "pop_online", "prison_pop", "co2_pc", "literacy_rate"]

ranks = []

def rank(dict, key, reversed):
    dict = sorted(dict, key = lambda d: d[key], reverse=reversed)
    for i in range(len(ranks)):
        dict[i][key] = i

def isBetter(dict, key, index1, index2):
    if (dict[index1][key] > dict[index2][key]):
        return True

def calculateWins():
    for i in range(len(ranks)):
        wins = 0
        ranks[i]["wins"] = 0
        for j in range(len(ranks)):
            cat_wins = 0
            if (j != i):
                for k in range(len(data_types)):
                    if (isBetter(ranks, data_types[k], i, j)):
                        cat_wins += 1
            if (cat_wins >= 6):
                wins += 1
        ranks[i]["wins"] = wins


for i in range(len(data)):
    tfr_score = round(-(abs(float(data[i]["tfr"]) - 2.1)), 2)
    ranks.append({
        "name": data[i]["country"],
        "tfr_score": tfr_score,
        "imr": float(data[i]["imr"]),
        "rni": data[i]["rni"],
        "gnipc": data[i]["gnipc"],
        "hdi": data[i]["hdi"],
        "life_expectancy": data[i]["le"],
        "education": data[i]["eys"],
        "gii": data[i]["gii"],
        "pop_online": data[i]["pop_online"],
        "prison_pop": data[i]["prison_pop"],
        "co2_pc": data[i]["co2_pc"],
        "literacy_rate": data[i]["literacy_rate"]
    })

# Stats that are better closer to zero must be reversed
rank(ranks, "tfr_score", False)
rank(ranks, "imr", True)
rank(ranks, "gii", True)
rank(ranks, "education", False)
rank(ranks, "life_expectancy", False)
rank(ranks, "gnipc", False)
rank(ranks, "rni", True)
rank(ranks, "hdi", False)
rank(ranks, "pop_online", False)
rank(ranks, "prison_pop", True)
rank(ranks, "co2_pc", True)
rank(ranks, "literacy_rate", False)

calculateWins()

ranks = sorted(ranks, key = lambda d: d["wins"], reverse=True)
for i in range(len(ranks)):
        ranks[i]["rank"] = i + 1

with open("rank.json", "w") as f:
    json.dump(ranks, f)