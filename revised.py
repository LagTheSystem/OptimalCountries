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

for country in data:
    tfr_score = round(-(abs(float(country["tfr"]) - 2.1)), 2)
    ranks.append({
        "name": country["country"],
        "tfr_score": tfr_score,
        "imr": float(country["imr"]),
        "rni": country["rni"],
        "gnipc": country["gnipc"],
        "hdi": country["hdi"],
        "life_expectancy": country["le"],
        "education": country["eys"],
        "gii": country["gii"],
        "pop_online": country["pop_online"],
        "prison_pop": country["prison_pop"],
        "co2_pc": country["co2_pc"],
        "literacy_rate": country["literacy_rate"]
    })

for indicator, isReversed in data_types:
    rank(ranks, indicator, isReversed)

calculateWins()

ranks = sorted(ranks, key = lambda d: d["wins"], reverse=True)
for i, entry in enumerate(ranks):
    entry["rank"] = i + 1

with open("rank.json", "w") as f:
    json.dump(ranks, f)
