def AzureOCR():
    path = input("Enter a URL For Analysis: ")
    try: 
        url = "https://microsoft-computer-vision3.p.rapidapi.com/detect"

        payload = "{\r\n    \"url\": \""+path+"\"\r\n}"
        headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "microsoft-computer-vision3.p.rapidapi.com",
    'x-rapidapi-key': "YOUR_RAPID_API_KEY"
    }

        response = requests.request("POST", url, data=payload, headers=headers)
        print("Azure Computer Vision --> Success")
        print(response.json())
    except Exception as ex:
        print(f"Azure Computer Vision Error --> {ex}")    

        
AzureOCR()
