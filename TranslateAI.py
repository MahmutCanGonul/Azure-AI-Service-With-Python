def TranslateAI():
    languages = ["English","Spanish","Franche","German","Turkish"]
    keys = {languages[0]:"en",languages[1]:"es",languages[2]:"fr",languages[3]:"de",languages[4]:"tr"}
    target_lan = ""
    
    for i in range(len(languages)):
        print(f"'{i+1}' --> {languages[i]}")
    
    choice = input("Which language to translate? ")
    
    if choice == "1":
        target_lan=keys[languages[int(choice)-1]]
    elif choice == "2":
         target_lan=keys[languages[int(choice)-1]]
    elif choice == "3":
         target_lan=keys[languages[int(choice)-1]]
    elif choice == "4":
         target_lan=keys[languages[int(choice)-1]]
    elif choice == "5":
         target_lan=keys[languages[int(choice)-1]]
    else:
        return "Choice --> Not Correct"
    
    
    sentence = input("Enter a Sentence: ")
    if sentence:
        try:
            url = "https://microsoft-translator-text.p.rapidapi.com/translate"
            querystring = {"to":target_lan,"api-version":"3.0","profanityAction":"NoAction","textType":"plain"}
            payload = "[\r\n    {\r\n        \"Text\": \""+sentence+"\"\r\n    }\r\n]"
            headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com",
    'x-rapidapi-key': "843406cdb2msh623e555d8416d8ep1d7e8ajsnb9afd7d794c4"
    }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
            data = response.json()
            result = data[0]['translations']
            print(f"Result Sentence --> {result[0]['text']}")
        except Exception as ex:
            print(f"Error --> {ex}")
            
TranslateAI()
