import requests
import time
import json
import sys


def getCategories(catType):
    res = requests.get("https://api.guildwars2.com/v2/" + catType)
    data = []
    print(len(res.json()))
    for nmb in res.json():
        try:
            item = requests.get("https://api.guildwars2.com/v2/" + catType + "/" + str(nmb))
            print(str(item.status_code) + "|" + str(item.json()))
            dic = {
                "name": item.json().get("name"),
                "id": item.json().get("id"),
                "chat_link": item.json().get("chat_link")
                }
            data.append(dic)
        except requests.exceptions.RequestException as e:
            print(e)
            pass
        except requests.exceptions.JSONDecodeError:
            print("Failed to resolve - DecodeErr")
            pass
        except requests.exceptions.InvalidJSONError:
            print("Failed to resolve - InvalidErr")
            pass

    with open(catType + ".json", "w") as f:
        json.dump(data, f)

    """
    with open('my.json') as json_file:
        data = json.load(json_file)
        print(data)
    """
    pass


def getPois():
    data = []
    try:
        regions = requests.get("https://api.guildwars2.com/v2/continents/1/floors/1/regions")
        print(regions.json())
        for region in regions.json():
            mapsByRegion = requests.get("https://api.guildwars2.com/v2/continents/1/floors/1/regions/" + str(region) + "/maps")
            print("Region: " + str(region))
            print(mapsByRegion.json())

            for map in mapsByRegion.json():
                currentMap = requests.get("https://api.guildwars2.com/v2/continents/1/floors/1/regions/" + str(region) + "/maps/" + str(map) + "/pois")
                pois = currentMap.json()

                for poi in pois:
                    item = requests.get("https://api.guildwars2.com/v2/continents/1/floors/1/regions/" + str(region) + "/maps/" + str(map) + "/pois/" + str(poi))
                    print(str(item.status_code) + "|" + str(item.json()))
                    dic = {
                        "name": item.json().get("name"),
                        "id": item.json().get("id"),
                        "chat_link": item.json().get("chat_link")
                    }
                    data.append(dic)

        regions = requests.get("https://api.guildwars2.com/v2/continents/2/floors/1/regions")
        print(regions.json())
        for region in regions.json():
            mapsByRegion = requests.get("https://api.guildwars2.com/v2/continents/2/floors/1/regions/" + str(region) + "/maps")
            print("Region: " + str(region))
            print(mapsByRegion.json())

            for map in mapsByRegion.json():
                currentMap = requests.get("https://api.guildwars2.com/v2/continents/2/floors/1/regions/" + str(region) + "/maps/" + str(map) + "/pois")
                pois = currentMap.json()

                for poi in pois:
                    item = requests.get("https://api.guildwars2.com/v2/continents/2/floors/1/regions/" + str(region) + "/maps/" + str(map) + "/pois/" + str(poi))
                    print(str(item.status_code) + "|" + str(item.json()))
                    dic = {
                        "name": item.json().get("name"),
                        "id": item.json().get("id"),
                        "chat_link": item.json().get("chat_link")
                    }
                    data.append(dic)

    except requests.exceptions.RequestException as e:
        print(e)
        pass
    except requests.exceptions.JSONDecodeError:
        print("Failed to resolve - DecodeErr")
        pass
    except requests.exceptions.InvalidJSONError:
        print("Failed to resolve - InvalidErr")
        pass

    with open("pois" + ".json", "w") as f:
        json.dump(data, f)

    pass



def main():
    getCategories("items")
    #getCategories("skills")
    #getCategories("skins")
    #getCategories("colors")
    #getCategories("traits")
    #getCategories("recipes")
    #getPois()

if __name__ == '__main__':
    main()