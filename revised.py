import json

with open('filtered_country_data.json', 'r') as file:
    data = json.load(file)

data_types = ["tfr_score", "imr", "gii", "education", "life_expectancy", "gnipc", "rni", "hdi", "pop_online", "prison_pop", "co2_pc", "literacy_rate"]

ranks = []

def rank(dic, key, reversed):
    dic = sorted(dic, key = lambda d: d[key], reverse=reversed)
    for i, entry in enumerate(dic):
        entry[key] = i

def isBetter(dic, key, index1, index2):
    if dic[index1][key] > dic[index2][key]:
        return True

def calculateWins():
    for i, entry in enumerate(ranks):
        wins = 0
        entry["wins"] = 0
        for j, _ in enumerate(ranks):
            if j != i:
                cat_wins = sum(1 for k in data_types if isBetter(ranks, k, i, j))
                if cat_wins >= 6:
                    wins += 1
        entry["wins"] = wins

for entry in data:
    tfr_score = round(-(abs(float(entry["tfr"]) - 2.1)), 2)
    ranks.append({
        "name": entry["country"],
        "tfr_score": tfr_score,
        "imr": float(entry["imr"]),
        "rni": entry["rni"],
        "gnipc": entry["gnipc"],
        "hdi": entry["hdi"],
        "life_expectancy": entry["le"],
        "education": entry["eys"],
        "gii": entry["gii"],
        "pop_online": entry["pop_online"],
        "prison_pop": entry["prison_pop"],
        "co2_pc": entry["co2_pc"],
        "literacy_rate": entry["literacy_rate"]
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
for i, entry in enumerate(ranks):
    entry["rank"] = i + 1

with open("rank.json", "w") as f:
    json.dump(ranks, f)
