import worldcup
import math

# 30 countries with top most points
countries_list = [
    "Brazil",
    "Belgium",
    "Argentina",
    "France",
    "England",
    "Italy",
    "Spain",
    "Netherlands",
    "Portugal",
    "Denmark",
    "Germany",
    "Croatia",
    "Mexico",
    "Uruguay",
    "Switzerland",
    "United States",
    "Colombia",
    "Senegal",
    "Wales",
    "Iran",
    "Serbia",
    "Morocco",
    "Peru",
    "Japan",
    "Sweden",
    "Poland",
    "Hungary",
    "Ecuador",
    "Russia",
    "Australia"
]

# defender means position_id = 2

def all_defenders(year):
    while year <= 2014:
        countries = {}
        defenders_list = []
        history = transform_worldcup(year)
        for country_name in countries_list:
            country_wins, country_games, country_stage = count_country_properties(history, country_name)
            country_dict = {
                "Country": country_name,
                "PS": None,
                "Wins": country_wins,
                "Games": country_games,
                "Stage": country_stage
            }
            # Create a players list for this country in this year
            players_list = worldcup.squad(country_name, year)

            for player in players_list:
                defender_dict = {
                    "year": year,
                    "defender_id": None,
                    "PS": None,
                }
                defender_id = player['player_id']
                defender = worldcup.player(defender_id)[0]
                player_position = ((defender['position'])['data'])['id']
                print(player_position)

                if player_position == 2 and defender['height'] and defender['weight']:
                    height = int(defender['height'][0:3])
                    weight = int(defender['weight'][0:3])

                    # Physical Strength = PS = height * weight
                    defender_dict["defender_id"] = defender_id
                    defender_dict["PS"] = (weight ** 2) * (height ** 3) / 1000000
                    defenders_list.append(defender_dict)

            total_ps = 0
            for defs in defenders_list:
                total_ps += defs["PS"]
            country_dict["PS"] = total_ps / len(defenders_list)

            countries[country_name] = country_dict

        country_list = []

        for country in countries:
            country_list.append(countries[country])
            print(country, countries[country])
        print('\n')
        print(country_list)

        worldcup.datatocsv(country_list, 'Countries_' + str(year) + '.csv')
        year += 4


def count_country_properties(history, country_name):
    wins = 0
    games = 0
    stage = 0
    country_ID = worldcup.searchteam(country_name)
    for ID in history:
        if ID['winner_team_id'] == country_ID:
            wins += 1
        if ID['localteam_id'] == country_ID or ID['visitorteam_id'] == country_ID:
            games += 1
            stage = max(stage, ID['stage'])
    return wins, games, stage


def transform_worldcup(year):
    data = worldcup.results(year)
    for id in data:
        id['stage'] = stage_id_year(year)[id['stage_id']]
        local_score = (id['scores'])['localteam_score']
        visitor_score = (id['scores'])['visitorteam_score']
        difference = abs(local_score - visitor_score)
        if difference in [0, 1]:
            id['competitive'] = 1
        else:
            id['competitive'] = 0
    worldcup.datatocsv(data, 'Results_' + str(year) + '.csv')
    return data


def stage_id_year(year):
    stage_keys = {2018: {1733: 0, 1727: 1, 1728: 1, 1729: 1, 1730: 1, 1731: 1},
                  2014: {12917: 0, 12901: 1, 12896: 1, 12898: 1, 12899: 1, 12900: 1},
                  2010: {12894: 0, 12884: 1, 12890: 1, 12891: 1, 12893: 1, 12892: 1}}
    return stage_keys[year]


if __name__ == '__main__':
    all_defenders(2010)
