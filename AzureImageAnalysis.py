def AzureImageAnalysis():
    path = input("Enter a URL For Analysis: ")
    try: 
       url = "https://microsoft-computer-vision3.p.rapidapi.com/analyze"
       querystring = {"language":"en","descriptionExclude":"Celebrities","visualFeatures":"ImageType","details":"Celebrities"}
       payload = "{\r\"url\": \""+path+"\"\r}"
       headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "microsoft-computer-vision3.p.rapidapi.com",
    'x-rapidapi-key': "YOUR_RAPID_API_KEY"
    }
       response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
       print("Azure Computer Vision --> Success")
       print(response.json())
    except Exception as ex:
        print(f"Azure Computer Vision Error --> {ex}")

def AzureDescribeAnalysis():
     path = input("Enter a URL For Analysis: ")
     try:
         url = "https://microsoft-computer-vision3.p.rapidapi.com/describe"

         querystring = {"language":"en","maxCandidates":"1","descriptionExclude":"Celebrities"}

         payload = "{\r\n    \"url\": \""+path+"\"\r\n}"
         headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "microsoft-computer-vision3.p.rapidapi.com",
    'x-rapidapi-key': "843406cdb2msh623e555d8416d8ep1d7e8ajsnb9afd7d794c4"
    }

         response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
         print("Azure Computer Vision --> Success")
         print(response.json())
    
     except Exception as ex:
        print(f"Azure Computer Vision Error --> {ex}")  
        
        
AzureImageAnalysis()
