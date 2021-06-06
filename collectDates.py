import sourceData
import finderLogic

dataLen =len(sourceData.subscribers["subs"])
for i in range(0,dataLen):
    pincode=sourceData.subscribers["subs"][i]["pin"]
    ageLimit=sourceData.subscribers["subs"][i]["age_limit"]
    output=finderLogic.findslots(pincode=pincode, ageLimit=ageLimit)
    print(pincode, ageLimit)
    print (output)

