def AzureTextAI():
     
     text = input("Enter a Sentence or Paragraph for text analsysis: ")
     data = []
     sending_text = ""
     
     if text:
         data = text.split(' ')
         if len(data) > 0:
             for i in range(len(data)):
                 sending_text += data[i]
         else:
             sending_text = text
         try:
             
            url = "https://microsoft-content-moderator2.p.rapidapi.com/ProcessText/Screen"
            querystring = {"PII":"true","autocorrect":"true","classify":"true"}

            payload = text
            headers = {
    'content-type': "text/plain",
    'x-rapidapi-host': "microsoft-content-moderator2.p.rapidapi.com",
    'x-rapidapi-key': "YOUR_RAPID_API_KEY"
    }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
            print("Azure Computer Vision --> Success")
            print(response.json()['PII'])
         except Exception as ex:
            no_pii = f"{ex}"
            if 'PII' in no_pii:
                print("Azure Computer Vision --> No 'PII' Data")
            else:
                print(f"Azure Computer Vision Error --> {no_pii}") 
                    
                    
                    
AzureTextAI()   
