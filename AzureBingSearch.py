def AzureBingSearch():
    search = input("What do you want search?")
    if search:
        try:
           url = "https://bing-news-search1.p.rapidapi.com/news/search"

           querystring = {"q":search,"mkt":"en-US","freshness":"Day","textFormat":"Raw","safeSearch":"Off"}

           headers = {
    'x-bingapis-sdk': "true",
    'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
    'x-rapidapi-key': "843406cdb2msh623e555d8416d8ep1d7e8ajsnb9afd7d794c4"
    }
 
           response = requests.request("GET", url, headers=headers, params=querystring)
           json = response.json()
           values = json['value']
           counts = []
           url = []
           
           for i in range(len(values)):
               value = values[i]
               print(f"Article --> '{i+1}'")
               print(f"Subject --> {value['name']}")
               print(f"URL --> {value['url']}")
               print(f"Description --> {value['description']}")
               print(f"Publish Date --> {value['datePublished']}")
               counts.append(i+1)
               url.append(value['url'])
               print("//////////////////////")
               print()
           choice = input("Which news do you want to search?")
           if choice.isdigit():
               ch = int(choice)
               for i in range(len(counts)):
                   if counts[i] == ch:
                       webbrowser.open(url[ch-1])
                       break
                  
        except Exception as ex:
            print(f"Error --> {ex}")
            
AzureBingSearch()      
