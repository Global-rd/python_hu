import requests

class RickMortyAPI:

    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api"

    def get_data(self, endpoint, params):
        data = []
        url = f"{self.base_url}/{endpoint}"

        while url:
            print(url)
            response = requests.get(url, params=params)
            if response.status_code == 200:
                result = response.json()
                data.extend(result["results"])
                url = result["info"].get("next", None)
            else:
                print(f"Error {response.status_code}: {response.json().get("error", "Unkown error")}")
                break
        return data


    def get_characters(self, name=None, status=None, species=None, type=None, gender=None):
        params = {
            "name": name,
            "status": status,
            "species": species,
            "type": type,
            "gender": gender
        }

        return self.get_data(endpoint="character", params=params)
        
    def get_episodes(self, name=None, episode=None):
        params = {"name": name,
                  "episode": episode}
        
        return self.get_data(endpoint="episode", params=params)
    
    def get_locations(self, name=None, type=None, dimension=None):
        params = {"name": name,
                  "type": type,
                  "dimension": dimension}
        
        return self.get_data("location", params=params)
    
api = RickMortyAPI()

characters = api.get_characters()
print(len(characters))
episodes = api.get_episodes()
print(len(episodes))
locations = api.get_locations()
print(len(locations))

#https://github.com/public-apis/public-apis