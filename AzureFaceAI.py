def AzureFaceAI():
    count=0
    total_age=0
    male_count=0
    female_count=0
    total_smile=0
    url_path = input("Enter a URL For Analysis: ")
    if url_path:
        try:
            url = "https://microsoft-face1.p.rapidapi.com/detect"

            querystring = {"returnFaceAttributes":"age, gender,headPose,smile,facialHair,glasses,emotion","detectionModel":"detection_01","returnFaceLandmarks":"true","recognitionModel":"recognition_01","returnFaceId":"true","returnRecognitionModel":"true"}
     
            payload = "{\r\"url\": \""+url_path+"\"\r}"
            headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "microsoft-face1.p.rapidapi.com",
    'x-rapidapi-key': "YOUR_RAPID_API_KEY"
    }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
            result = response.json()
            
            if len(result) >1:
                print(f"Detected People Number --> {len(result)}")
                for i in range(len(result)):
                    count=i+1
                    data = result[i]
                    face_attributes = data['faceAttributes']
                    total_age +=face_attributes['age']
                    print(f"{count}.Age-> {face_attributes['age']}")
                    if face_attributes['gender'] == "male":
                        male_count+=1
                    elif face_attributes['gender'] == "female":
                        female_count+=1
                    
                    total_smile+=face_attributes['smile']
                    
                    
                average = total_age / len(result)
                average_smile = total_smile / len(result)
                print(f"Total Age Average --> {average}")
                print(f"Total Smile Average --> 1/{average_smile}")
                print(f"Male Number --> {male_count}")
                print(f"Female Number --> {female_count}")
                
            else:
                data = result[0]
                face_attributes = data['faceAttributes']
                emotion = face_attributes['emotion']
                emotions = ['anger','contempt','disgust','fear','happiness','neutral','sadness','surprise']
                
                faceid = data['faceId']
                age = face_attributes['age']
                gender = face_attributes['gender']
                glasses = face_attributes['glasses']
                
                print(f"FACE ID --> {faceid}")
                print(f"AGE --> {age}")
                print(f"GENDER --> {gender}")
                print(f"GLASSES --> {glasses}")
                points = []
                for i in range(len(emotions)):
                    subje = emotions[i].upper()
                    result = emotion[emotions[i]]
                    points.append(result)
                    print(f"{subje} --> 1/{result}")
                points.sort()
                for i in range(len(emotions)):
                    subje = emotions[i].upper()
                    result = emotion[emotions[i]]
                    if result == points[len(points)-1]:
                        print(f"DETECTED EMOTION --> {subje} --> 1/{result}")
                    
                    
                
                
                
        except Exception as ex:
            print(f"Azure Computer Vision Error --> {ex}")
            
AzureFaceAI()
