import requests
import json
import datetime
from datetime import date
from datetime import timedelta

endpoint = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?'
ageLimit=45 #chnage it to 18
pincode='313001'
#date='03-05-2021'

# This API can't be called from the code, so we would need abreowe agent

#Request URL: https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=504&date=03-05-2021

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def pollURL(endpoint, pincode, date):
    url=endpoint+'pincode='+pincode+'&date='+date
    print(url)
    response=requests.get(url, headers=headers)
    return(response)


if __name__ == '__main__':
    slot_list =[]
    #for date1 in dates :
    if 1==1:
        date2=date.today().strftime("%d-%m-%Y")
        response = pollURL(endpoint, pincode, date2)    
        #print(response.content)
        if response.status_code == 200:
            vacdata=response.json()
            #print(vacdata)
            center_count =len(vacdata["centers"])
            for i in range(0,center_count):
                sessions = vacdata["centers"][i]["sessions"]
                location = vacdata["centers"][i]["name"]
                freepaid =vacdata["centers"][i]["fee_type"]
            
                for i in range(len(sessions)):
                    session_list=[]
                    min_age_limit =sessions[i]["min_age_limit"]
                    available=sessions[i]["available_capacity"]
                    slot= sessions[i]["slots"]
                    if available > 0 :
                    #if min_age_limit == ageLimit and available > 0 : #uncoment this and comment above if you want to fiter by age limit
                        session_list.append(sessions[i]["date"])
                        session_list.append(location)
                        session_list.append(freepaid)
                        session_list.append(min_age_limit) 
                        session_list.append(sessions[i]["vaccine"])
                        session_list.append(slot)
                        session_list.append(available)
                        slot_list.append(session_list)
            print(*slot_list, sep='\n')
        else:
            exit()


