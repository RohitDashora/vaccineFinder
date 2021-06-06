#this file holds the jason that will eventually delivered from the source data
import json
subdata = """
{
"subs" : [
    {
        "pin":"313001",
        "age_limit":"45",
        "email":["rohitdasora@gmail.com","rohitdashora@yahoo.co.in","rohitdashora@outlook.com"]

    },
    {
        "pin":"313001",
        "age_limit":"18",
        "email":["rohitdasora@gmail.com","rohitdashora@yahoo.co.in","rohitdashora@outlook.com"]

    },
    {
        "pin":"313002",
        "age_limit":"45",
        "email":["rohitdasora@gmail.com","rohitdashora@yahoo.co.in","rohitdashora@outlook.com"]
    },
    {
        "pin":"313003",
        "age_limit":"45",
        "email":["rohitdasora@gmail.com","rohitdashora@yahoo.co.in","rohitdashora@outlook.com"]
    }
]
}
"""
subscribers=json.loads(subdata)
#print (subscribers)
