travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above
# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests


def add_new_country(co, vi, ci):
    travel_log.append({"country": co,
                       "visits": vi,
                       "cities": ci})


# 🚨 Do NOT change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
