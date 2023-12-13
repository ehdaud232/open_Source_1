import requests

api_key = 'RGAPI-4ccb12a4-bbf2-4107-aa40-e05ccca889b5'
summoner_name = '빠빠짜따까바짜까'

url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'
response = requests.get(url)

if response.status_code == 200:
    summoner_data = response.json()
    account_id = summoner_data['accountId']
    summoner_id = summoner_data['id']

    rank_url = f'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}'
    rank_response = requests.get(rank_url)

    if rank_response.status_code == 200:
        rank_data = rank_response.json()
        if rank_data:
            print(f"Summoner Name: {summoner_name}")
            for entry in rank_data:
                if entry['queueType'] == 'RANKED_SOLO_5x5':
                    
                    tier = entry['tier']
                    rank = entry['rank']
                    lp = entry['leaguePoints']
                    wins = entry['wins']
                    losses = entry['losses']
                    win_rate = f"{(wins / (wins + losses)) * 100:.2f}%"
                    print(f"Rank: {tier} {rank} {lp} LP")
                    print(f"Wins: {wins}, Losses: {losses}, Win Rate: {win_rate}")

        else:
            print(f"{summoner_name} is not ranked in any queue.")
    else:
        print("Failed to fetch ranked data.")
else:
    print("Failed to fetch summoner data.")

