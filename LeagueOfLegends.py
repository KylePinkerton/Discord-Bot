from riotwatcher import RiotWatcher
import asyncio
import discord
from discord.ext import commands
import requests
import random


def __init__(self, bot):
        self.bot = bot


API_KEY = '___' #api key not inserted
watcher = RiotWatcher(API_KEY) #RiotWatcher is a constructor in the library
my_region = 'na1'

class LeagueOfLegends:
    """Class LeagueOfLegends
    Cog for bot.py which contains
    relevant functions for the
    game League Of Legends
    """
    def __init__(self, bot):
        self.bot = bot
        self.summoner = 'imaqtpie' #default summoner is the legend himself imaqtpie
        
    #https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/RiotSchmick?api_key=RGAPI-48bd0527-0594-414e-80de-d7601c7bfc40
    #{"id":19887289,"accountId":32639237,"name":"Imaqtpie","profileIconId":556,"revisionDate":1527354931000,"summonerLevel":153}

    #https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/19887289?api_key=RGAPI-48bd0527-0594-414e-80de-d7601c7bfc40
    #{"status":{"message":"Data not found","status_code":404}}
    #{"gameId":2791458407,"mapId":11,"gameMode":"CLASSIC","gameType":"MATCHED_GAME","gameQueueConfigId":420,"participants":[{"teamId":100,"spell1Id":4,"spell2Id":11,"championId":9,"profileIconId":504,"summonerName":"Nikkone","bot":false,"summonerId":20220845,"gameCustomizationObjects":[],"perks":{"perkIds":[8112,8126,8138,8105,8234,8237],"perkStyle":8100,"perkSubStyle":8200}},{"teamId":100,"spell1Id":4,"spell2Id":21,"championId":161,"profileIconId":3221,"summonerName":"fwii","bot":false,"summonerId":19296564,"gameCustomizationObjects":[],"perks":{"perkIds":[8229,8226,8234,8237,8473,8472],"perkStyle":8200,"perkSubStyle":8400}},{"teamId":100,"spell1Id":4,"spell2Id":7,"championId":145,"profileIconId":556,"summonerName":"Imaqtpie","bot":false,"summonerId":19887289,"gameCustomizationObjects":[],"perks":{"perkIds":[8021,9111,9104,8014,8234,8236],"perkStyle":8000,"perkSubStyle":8200}},{"teamId":100,"spell1Id":14,"spell2Id":4,"championId":201,"profileIconId":522,"summonerName":"twtv vincentslol","bot":false,"summonerId":20759358,"gameCustomizationObjects":[],"perks":{"perkIds":[8465,8473,8429,8242,8313,8316],"perkStyle":8400,"perkSubStyle":8300}},{"teamId":100,"spell1Id":4,"spell2Id":12,"championId":164,"profileIconId":907,"summonerName":"MistyStumpey","bot":false,"summonerId":41233933,"gameCustomizationObjects":[],"perks":{"perkIds":[8005,9111,9104,8014,8473,8472],"perkStyle":8000,"perkSubStyle":8400}},{"teamId":200,"spell1Id":11,"spell2Id":4,"championId":107,"profileIconId":7,"summonerName":"Inorï","bot":false,"summonerId":20389591,"gameCustomizationObjects":[],"perks":{"perkIds":[8112,8143,8138,8105,9111,8014],"perkStyle":8100,"perkSubStyle":8000}},{"teamId":200,"spell1Id":4,"spell2Id":7,"championId":498,"profileIconId":3440,"summonerName":"Spawwwwn","bot":false,"summonerId":32299406,"gameCustomizationObjects":[],"perks":{"perkIds":[8021,9101,9103,8014,8234,8236],"perkStyle":8000,"perkSubStyle":8200}},{"teamId":200,"spell1Id":4,"spell2Id":14,"championId":497,"profileIconId":3236,"summonerName":"lron Pyrite","bot":false,"summonerId":21014987,"gameCustomizationObjects":[],"perks":{"perkIds":[8465,8473,8429,8453,8243,8234],"perkStyle":8400,"perkSubStyle":8200}},{"teamId":200,"spell1Id":4,"spell2Id":7,"championId":112,"profileIconId":18,"summonerName":"Rapidx","bot":false,"summonerId":26306103,"gameCustomizationObjects":[],"perks":{"perkIds":[8214,8226,8210,8237,8139,8135],"perkStyle":8200,"perkSubStyle":8100}},{"teamId":200,"spell1Id":4,"spell2Id":6,"championId":122,"profileIconId":934,"summonerName":"Tony Top 2","bot":false,"summonerId":52559520,"gameCustomizationObjects":[],"perks":{"perkIds":[8010,9111,9104,8299,8473,8472],"perkStyle":8000,"perkSubStyle":8400}}],"observers":{"encryptionKey":"S43+NYQ8+IEPdGDekl7wTU9KY3Qy9KI0"},"platformId":"NA1","bannedChampions":[{"championId":121,"teamId":100,"pickTurn":1},{"championId":-1,"teamId":100,"pickTurn":2},{"championId":24,"teamId":100,"pickTurn":3},{"championId":4,"teamId":100,"pickTurn":4},{"championId":104,"teamId":100,"pickTurn":5},{"championId":104,"teamId":200,"pickTurn":6},{"championId":28,"teamId":200,"pickTurn":7},{"championId":39,"teamId":200,"pickTurn":8},{"championId":142,"teamId":200,"pickTurn":9},{"championId":91,"teamId":200,"pickTurn":10}],"gameStartTime":0,"gameLength":0}
    def set_default_summoner(self, summoner):
        self.summoner = summoner
        
    def get_league_stats(self, summoner):
        """ str -> lst of str
        get_leage_stats('imaqtpie') ->
        ['Imaqtpie', '19887289', '32639237', '154', 'CHALLENGER', 'I', '483', '690', '658']
        [summoner_name, summoner_id, summoner_accountid, summoner_level, rank_tier, rank_rank, rank_lp, rank_wins, rank_losses]
        """
        summoner_info = watcher.summoner.by_name(my_region, summoner) #calls a function on the watcher object
        summoner_name = str(summoner_info['name'])
        summoner_level = str(summoner_info["summonerLevel"])
        #print(summoner_info)
        summoner_id = str(summoner_info['id'])
        summoner_accountid = str(summoner_info['accountId'])
        my_ranked_stats = watcher.league.positions_by_summoner(my_region, summoner_id) #a function of the library
        #print(my_ranked_stats)

        my_ranked_stats_length = len(my_ranked_stats)
        #print(my_ranked_stats_length)
        #IF THEY HAVE NO RANK AT ALL 
        if len(my_ranked_stats) == 0:
            lst = [summoner_name, summoner_id, summoner_accountid, summoner_level, "N/A", "N/A", "N/A", "N/A", "N/A"]
            return lst

        else: 
            for i in range(my_ranked_stats_length):
                league_mode_info = my_ranked_stats[i]
                if my_ranked_stats[i]["queueType"] == 'RANKED_SOLO_5x5':
                    ranked_solo_info = my_ranked_stats[i]
                    trigger = True
                                
            #IF THEY HAVE RANKED SOLO
            if trigger: 
                        
            #print(ranked_solo_info)
                rank_tier = str(ranked_solo_info["tier"])
                rank_rank = str(ranked_solo_info["rank"])
                rank_lp = str(ranked_solo_info["leaguePoints"])
                rank_wins = str(ranked_solo_info["wins"])
                rank_losses = str(ranked_solo_info["losses"])

                #print("Summoner: " + summoner_name + " Level " + summoner_level)
                #print("Rank: " + rank_tier + " " + rank_rank + " " + rank_lp + " LP")
                #print("Win/loss: " + rank_wins + "—" + rank_losses)

                lst = [summoner_name, summoner_id, summoner_accountid, summoner_level, rank_tier, rank_rank, rank_lp, rank_wins, rank_losses]
                #print(lst)

                return lst

                #they have some other rank, CAN IMRPOVE THIS TO DEFAULT TO 5X5, 3X3
            elif trigger==False:
                lst = [summoner_name, summoner_id, summoner_accountid, summoner_level, "N/A", "N/A", "N/A", "N/A", "N/A"]
                return lst
                                
                                

    def print_individual_ranked_stats(self, leaguestats):
        """leaguestats (from get_league_stats) -> None
        prints leaguestats nicely
        """
        print(leaguestats[0] + " Rank: " + leaguestats[4] + " " + leaguestats[5] + " " + leaguestats[6] + " LP" + " Win/loss: " + leaguestats[7] + "-" + leaguestats[8] + " Level " + leaguestats[3]) 
        #print("Rank: " + leaguestats[4] + " " + leaguestats[5] + " " + leaguestats[6] + " LP")
        #print("Win/loss: " + leaguestats[7] + "—" + leaguestats[8])


    def return_individual_ranked_stats(self, leaguestats):
        """leaguestats (from get_league_stats) -> String
        returns leaguestats in string form
        """

        return leaguestats[0] + " Rank: " + leaguestats[4] + " " + leaguestats[5] + " " + leaguestats[6] + " LP" + " Win/loss: " + leaguestats[7] + "-" + leaguestats[8] + " Level " + leaguestats[3]

    def is_in_game(self, leaguestats):
        """leaguestats (from get_league_stats) -> bool
        """
        search_string = "https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + leaguestats[1] + "?api_key=" + API_KEY
        response = requests.get(search_string)
        if str(response) == "<Response [200]>":
            return True
        else:
            return False
        #file = response.json()
        #print(response)
        #print(file)
                
                
    def current_game(self, leaguestats):
        """ leaguestats (from get_league_stats) -> json
                    

        """
        search_string = "https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + leaguestats[1] + "?api_key=" + API_KEY
        response = requests.get(search_string)

        file = response.json()
        #if we want match id/more match info, we can use file without parsing to participants
        participants_info = file['participants']
        #print(response) #<Response [200]> #if in game
        #print(file) #{'gameId': 2792424858, 'mapId': 11, 'gameMode': 'CLASSIC', 'gameType': 'MATCHED_GAME', 'gameQueueConfigId': 420, 'participants': [{'teamId': 100, 'spell1Id': 4, 'spell2Id': 12, 'championId': 81, 'profileIconId': 3264, 'summonerName': 'Apollo Price', 'bot': False, 'summonerId': 7250, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8359, 8304, 8316, 8347, 8226, 8236], 'perkStyle': 8300, 'perkSubStyle': 8200}}, {'teamId': 100, 'spell1Id': 14, 'spell2Id': 4, 'championId': 55, 'profileIconId': 3440, 'summonerName': 'Evølve', 'bot': False, 'summonerId': 91615420, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8143, 8138, 8134, 9111, 8014], 'perkStyle': 8100, 'perkSubStyle': 8000}}, {'teamId': 100, 'spell1Id': 4, 'spell2Id': 12, 'championId': 39, 'profileIconId': 11, 'summonerName': '3in1warrïor', 'bot': False, 'summonerId': 21830641, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8010, 9111, 9104, 8014, 8473, 8472], 'perkStyle': 8000, 'perkSubStyle': 8400}}, {'teamId': 100, 'spell1Id': 4, 'spell2Id': 14, 'championId': 12, 'profileIconId': 3159, 'summonerName': 'Hopefulqt', 'bot': False, 'summonerId': 51075422, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8439, 8473, 8444, 8242, 8316, 8347], 'perkStyle': 8400, 'perkSubStyle': 8300}}, {'teamId': 100, 'spell1Id': 4, 'spell2Id': 11, 'championId': 121, 'profileIconId': 1123, 'summonerName': 'lc0nic', 'bot': False, 'summonerId': 45186258, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8143, 8138, 8105, 8234, 8232], 'perkStyle': 8100, 'perkSubStyle': 8200}}, {'teamId': 200, 'spell1Id': 4, 'spell2Id': 7, 'championId': 145, 'profileIconId': 556, 'summonerName': 'Imaqtpie', 'bot': False, 'summonerId': 19887289, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8021, 9111, 9104, 8014, 8234, 8236], 'perkStyle': 8000, 'perkSubStyle': 8200}}, {'teamId': 200, 'spell1Id': 14, 'spell2Id': 4, 'championId': 142, 'profileIconId': 23, 'summonerName': 'Shiphtur', 'bot': False, 'summonerId': 19967304, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8143, 8138, 8135, 8306, 8316], 'perkStyle': 8100, 'perkSubStyle': 8300}}, {'teamId': 200, 'spell1Id': 4, 'spell2Id': 14, 'championId': 497, 'profileIconId': 1301, 'summonerName': 'Tony Top', 'bot': False, 'summonerId': 19587365, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8214, 8243, 8234, 8237, 8473, 8472], 'perkStyle': 8200, 'perkSubStyle': 8400}}, {'teamId': 200, 'spell1Id': 4, 'spell2Id': 12, 'championId': 114, 'profileIconId': 1665, 'summonerName': 'Azures', 'bot': False, 'summonerId': 68469257, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8437, 8473, 8472, 8453, 8234, 8236], 'perkStyle': 8400, 'perkSubStyle': 8200}}, {'teamId': 200, 'spell1Id': 11, 'spell2Id': 4, 'championId': 64, 'profileIconId': 3440, 'summonerName': 'Sophist Ságe', 'bot': False, 'summonerId': 88490180, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8143, 8138, 8105, 8234, 8236], 'perkStyle': 8100, 'perkSubStyle': 8200}}], 'observers': {'encryptionKey': 'id+Oba82OD+wMURqa6Q2+WfsfEIOe4t0'}, 'platformId': 'NA1', 'bannedChampions': [{'championId': 104, 'teamId': 100, 'pickTurn': 1}, {'championId': 136, 'teamId': 100, 'pickTurn': 2}, {'championId': 157, 'teamId': 100, 'pickTurn': 3}, {'championId': 91, 'teamId': 100, 'pickTurn': 4}, {'championId': 24, 'teamId': 100, 'pickTurn': 5}, {'championId': 85, 'teamId': 200, 'pickTurn': 6}, {'championId': 91, 'teamId': 200, 'pickTurn': 7}, {'championId': 164, 'teamId': 200, 'pickTurn': 8}, {'championId': 104, 'teamId': 200, 'pickTurn': 9}, {'championId': 5, 'teamId': 200, 'pickTurn': 10}], 'gameStartTime': 1527447649282, 'gameLength': 392}
        #print(participants_info) #[{'teamId': 100, 'spell1Id': 4, 'spell2Id': 12, 'championId': 81, 'profileIconId': 3264, 'summonerName': 'Apollo Price', 'bot': False, 'summonerId': 7250, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8359, 8304, 8316, 8347, 8226, 8236], 'perkStyle': 8300, 'perkSubStyle': 8200}}, {'teamId': 100, 'spell1Id': 14, 'spell2Id': 4, 'championId': 55, 'profileIconId': 3440, 'summonerName': 'Evølve', 'bot': False, 'summonerId': 91615420, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8143, 8138, 8134, 9111, 8014], 'perkStyle': 8100, 'perkSubStyle': 8000}}, {'teamId': 100, 'spell1Id': 4, 'spell2Id': 12, 'championId': 39, 'profileIconId': 11, 'summonerName': '3in1warrïor', 'bot': False, 'summonerId': 21830641, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8010, 9111, 9104, 8014, 8473, 8472], 'perkStyle': 8000, 'perkSubStyle': 8400}}, {'teamId': 100, 'spell1Id': 4, 'spell2Id': 14, 'championId': 12, 'profileIconId': 3159, 'summonerName': 'Hopefulqt', 'bot': False, 'summonerId': 51075422, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8439, 8473, 8444, 8242, 8316, 8347], 'perkStyle': 8400, 'perkSubStyle': 8300}}, {'teamId': 100, 'spell1Id': 4, 'spell2Id': 11, 'championId': 121, 'profileIconId': 1123, 'summonerName': 'lc0nic', 'bot': False, 'summonerId': 45186258, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8143, 8138, 8105, 8234, 8232], 'perkStyle': 8100, 'perkSubStyle': 8200}}, {'teamId': 200, 'spell1Id': 4, 'spell2Id': 7, 'championId': 145, 'profileIconId': 556, 'summonerName': 'Imaqtpie', 'bot': False, 'summonerId': 19887289, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8021, 9111, 9104, 8014, 8234, 8236], 'perkStyle': 8000, 'perkSubStyle': 8200}}, {'teamId': 200, 'spell1Id': 14, 'spell2Id': 4, 'championId': 142, 'profileIconId': 23, 'summonerName': 'Shiphtur', 'bot': False, 'summonerId': 19967304, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8143, 8138, 8135, 8306, 8316], 'perkStyle': 8100, 'perkSubStyle': 8300}}, {'teamId': 200, 'spell1Id': 4, 'spell2Id': 14, 'championId': 497, 'profileIconId': 1301, 'summonerName': 'Tony Top', 'bot': False, 'summonerId': 19587365, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8214, 8243, 8234, 8237, 8473, 8472], 'perkStyle': 8200, 'perkSubStyle': 8400}}, {'teamId': 200, 'spell1Id': 4, 'spell2Id': 12, 'championId': 114, 'profileIconId': 1665, 'summonerName': 'Azures', 'bot': False, 'summonerId': 68469257, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8437, 8473, 8472, 8453, 8234, 8236], 'perkStyle': 8400, 'perkSubStyle': 8200}}, {'teamId': 200, 'spell1Id': 11, 'spell2Id': 4, 'championId': 64, 'profileIconId': 3440, 'summonerName': 'Sophist Ságe', 'bot': False, 'summonerId': 88490180, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8143, 8138, 8105, 8234, 8236], 'perkStyle': 8100, 'perkSubStyle': 8200}}]
        #print(len(participants_info)) #10
        #print(participants_info[0]) #{'teamId': 100, 'spell1Id': 4, 'spell2Id': 12, 'championId': 81, 'profileIconId': 3264, 'summonerName': 'Apollo Price', 'bot': False, 'summonerId': 7250, 'gameCustomizationObjects': [], 'perks': {'perkIds': [8359, 8304, 8316, 8347, 8226, 8236], 'perkStyle': 8300, 'perkSubStyle': 8200}}
        #print(participants_info[0]['teamId']) #100
        #print(participants_info[0]['summonerName']) #3in1warrior
        #print(participants_info[0]['summonerId']) #47943093
        #print(participants_info[0]['championId']) #12
        return participants_info

    def get_team_info(self, currentgame):
        """currentgame (from current_game) -> tuple of length 2
        index 1 of tuple = 2d list of players on team 1, inner list has individal player info
        index 2 of tuple = 2d list of players on team 2, inner list has individal player info
        """
        team1 = []
        team2 = []
        #info for each player contained in currentgame[i]
        #if we want rune info, we can use this
        for i in range(len(currentgame)):
            if currentgame[i]['teamId'] == 100:
                summoner_name = currentgame[i]['summonerName']
                summoner_id = currentgame[i]['summonerId']
                champion_id = currentgame[i]['championId']
                templst = [summoner_name, summoner_id, champion_id]
                team1 += [templst]
            elif currentgame[i]['teamId'] == 200:
                summoner_name = currentgame[i]['summonerName']
                summoner_id = currentgame[i]['summonerId']
                champion_id = currentgame[i]['championId']
                templst = [summoner_name, summoner_id, champion_id]
                team2 += [templst]
                                
                             
        #print(team1) #[['Sexy Yaoi Prince', 24412033, 121], ['LoopGoop', 21998704, 25], ['Imaqtpie', 19887289, 15], ['Shiphtur', 19967304, 142], ['Azures', 68469257, 92]]
        #print(team2) #[['EricZYang', 23476283, 41], ['Inorï', 20389591, 107], ['Shimatora', 30372420, 4], ['typty', 22638316, 110], ['MELODRAMA LORDE', 34403083, 267]]
        #print((team1, team2)) #([['Sexy Yaoi Prince', 24412033, 121], ['LoopGoop', 21998704, 25], ['Imaqtpie', 19887289, 15], ['Shiphtur', 19967304, 142], ['Azures', 68469257, 92]], [['EricZYang', 23476283, 41], ['Inorï', 20389591, 107], ['Shimatora', 30372420, 4], ['typty', 22638316, 110], ['MELODRAMA LORDE', 34403083, 267]])
        return (team1, team2)
                                

    def print_team_info(self, teaminfo):
        """ teaminfo (from get_team_info) -> string
        prints teaminfo nicely
        """

        print("######### TEAM 1 #########")
        red_side_info = teaminfo[0]
        red_side_info_length = len(teaminfo[0])
        for i in range(red_side_info_length):
            print(str(i+1) + ". " + return_individual_ranked_stats(get_league_stats(teaminfo[0][i][0])))

        print("######### TEAM 2 #########")
        blue_side_info = teaminfo[1]
        blue_side_info_length = len(teaminfo[1])
        for i in range(blue_side_info_length):
            print(str(i+1) + ". " + return_individual_ranked_stats(get_league_stats(teaminfo[1][i][0])))

                

                
    def get_champion(self, champion_id):
        """ champion_id (int) -> champion name (string)
        gets a champion name from a champion id
        """

        champion_id = str(champion_id)
        search_string = "https://na1.api.riotgames.com/lol/static-data/v3/champions/" + champion_id + "?api_key=" + API_KEY
        response = requests.get(search_string)

                       
        if str(response) == "<Response [200]>": 
            pass
        else:
            return "Champion Doesn't Exist"
        file = response.json()
        #print(response) #<Response [200]>
        #print(file) #{'name': 'Corki', 'id': 42, 'title': 'the Daring Bombardier', 'key': 'Corki'}
        #print(file['name']) #Corki

        return file['name']

    #WORK IN PROGRESS
    def return_main_champion(self, leaguestats):
        """leaguestats (from get_league_stats) -> main champion and frequency (string)
        Using the summoners past 20 games, determine their main
        champion (list frequency).
        """
        summoner_champion_info = watcher.match.matchlist_by_account_recent(my_region, leaguestats[1])
        print(summoner_champion_info)

    #command version
    def get_main_champion(self, summoner):
        """leaguestats (from get_league_stats) -> main champion and frequency (string)
        Using the summoners past 20 games, determine their main
        champion (list frequency).
        """
        leaguestats = get_league_stats(summoner)
        summoner_champion_info = watcher.match.matchlist_by_account_recent(my_region, leaguestats[1])
        print(summoner_champion_info)



         


        #{'id': 39058054, 'accountId': 202029983, 'name': 'ToxX', 'profileIconId': 1152, 'revisionDate': 1527326583000, 'summonerLevel': 61}
        #[{'leagueId': '20e7b370-0d5f-11e8-b4cc-c81f66cf2333', 'leagueName': "Malphite's Runemasters", 'tier': 'GOLD', 'queueType': 'RANKED_SOLO_5x5', 'rank': 'V', 'playerOrTeamId': '39058054', 'playerOrTeamName': 'ToxX', 'leaguePoints': 52, 'wins': 9, 'losses': 6, 'veteran': False, 'inactive': False, 'freshBlood': False, 'hotStreak': False}, {'leagueId': 'ab159500-0ee8-11e8-a367-c81f66dbb56c', 'leagueName': "Kha'Zix's Tricksters", 'tier': 'SILVER', 'queueType': 'RANKED_FLEX_SR', 'rank': 'II', 'playerOrTeamId': '39058054', 'playerOrTeamName': 'ToxX', 'leaguePoints': 58, 'wins': 17, 'losses': 13, 'veteran': False, 'inactive': False, 'freshBlood': False, 'hotStreak': False}]

         

 #               s = get_league_stats('shiphtur')
  #              print("Printing indivudal stats: ")
 #               print_individual_ranked_stats(s)
 #               l = return_individual_ranked_stats(s)
 #               print("Printing returned individual rankrd stats: ")
 #               print(l)
 #               p = is_in_game(s)
 #               print("Printing is_in_game: ")
 #               print(p)
 #               s1 = current_game(s)
 #               team_info = get_team_info(s1)
 #               print("Printing team stats: ")
 #               print_team_info(team_info) """

############################   BOT COMMANDS   ########################################################################
 
    @commands.command(name="summoner", description="Sets a given summoner as the default summoner (imaqtpie by default). Commands that require a summoner name will use this summoner by default. Spaces in names must be replaced by \"-\"." , brief="Set a default summoner.", pass_context=True, aliases=("default", "default_summoner"))
    async def default_summoner(self, ctx, summoner):
        summoner = summoner.replace("-", " ")#handles spaces in summoner's name
        self.set_default_summoner(summoner)

    @commands.command(name="leaguestats", description="Gets an individual summoners league of legends stats. Spaces in names must be replaced by \"-\"." , brief="Get a summoners league of legends stats.", pass_context=True, aliases=("stats", "league_stats", "lolstats"))
    async def league_stats_summoner(self, ctx, summoner=''):
        if summoner.strip()== '': #if no argument is given, we want the default summoner
            summoner = self.summoner
            
        summoner = summoner.replace("-", " ")#handles spaces in summoner's name
        leaguestats = self.get_league_stats(summoner)
        print(leaguestats)
        string = self.return_individual_ranked_stats(leaguestats)
        await self.bot.say("%s" %string)

    @commands.command(name="gameinfo", description="Gets info about an ongoing summoner's game (if no summoner is provided, use the default summoner). Spaces in names must be replaced by \"-\"." , brief="Post info about an ongoing summoner's game.", pass_context=True, aliases=("ranks", "players"))
    async def ongoing_game(self, ctx, summoner=''):
        if summoner.strip()== '': #if no argument is given, we want the default summoner
            summoner = self.summoner
            
        summoner = summoner.replace("-", " ") #handles spaces in summoner's name
        leaguestats = self.get_league_stats(summoner)
        game_status = self.is_in_game(leaguestats)
        #print(game_status)

        if game_status:
            current_game = self.current_game(leaguestats)
            team_info = self.get_team_info(current_game)
            await self.bot.say("################## TEAM 1 ##################")
            red_side_info = team_info[0]
            red_side_info_length = len(team_info[0])
            #print(team_info[0])
            for i in range(red_side_info_length):
                p = i+1
                number = str(p)
                #print(number)
                summoner = team_info[0][i][0]
                #print(summoner)
                leaguestats = self.get_league_stats(summoner)
                #print(leaguestats)
                string = self.return_individual_ranked_stats(leaguestats)
                #print(string)
                string_print = number + ". " + string
                #print(string_print)
                await self.bot.say("%s" %string_print)

            await self.bot.say("################## TEAM 2 ##################")
            blue_side_info = team_info[1]
            blue_side_info_length = len(team_info[1])
            #print(team_info[1])
            for i in range(blue_side_info_length):
                p = i+1
                number = str(p)
                #print(number)
                summoner = team_info[1][i][0]
                #print(summoner)
                leaguestats = self.get_league_stats(summoner)
                #print(leaguestats)
                string = self.return_individual_ranked_stats(leaguestats)
                #print(string)
                string_print = number + ". " + string
                #print(string_print)
                await self.bot.say("%s" %string_print)
                


        else:
            await self.bot.say("%s is currently not in a game" %summoner)
            



def setup(bot):
    bot.add_cog(LeagueOfLegends(bot))
    print('LeagueOfLegends is loaded')
