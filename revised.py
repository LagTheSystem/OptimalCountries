import json

with open('filtered_country_data.json', 'r') as file:
    data = json.load(file)

data_types = [
    ("tfr_score", False),
    ("imr", True),
    ("gii", True),
    ("education", False),
    ("life_expectancy", False),
    ("gnipc", False),
    ("rni", True),
    ("hdi", False),
    ("pop_online", False),
    ("prison_pop", True),
    ("co2_pc", True),
    ("literacy_rate", False),
]

ranks = []

def rank(dic, key, isReversed):
    dic = sorted(dic, key = lambda d: d[key], reverse=isReversed)
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
                cat_wins = sum(1 for k, _ in data_types if isBetter(ranks, k, i, j))
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

for type, isReversed in data_types:
    rank(ranks, type, isReversed)

calculateWins()

ranks = sorted(ranks, key = lambda d: d["wins"], reverse=True)
for i, entry in enumerate(ranks):
    entry["rank"] = i + 1

with open("rank.json", "w") as f:
    json.dump(ranks, f)
