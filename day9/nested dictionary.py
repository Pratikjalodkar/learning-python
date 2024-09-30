# nested list and dictionary

dict = {
    "Country":{"India":["UP","MP","Bihar","Dehli"]},
    "MP":["Indore","Dewas"]
}


#nesting a dictionary in a list
dict2 = [
    {
        "Country":{"India":["UP","MP","Bihar","Dehli"]},
        "MP":["Indore","Dewas"]
    },
    {
        "Country":{"India":["UP","MP","Bihar","Dehli"]},
        "MP":["Indore","Dewas"]
    },
        {
        "Country":{"India":["UP","MP","Bihar","Dehli"]},
        "MP":["Indore","Dewas"]
    }
]
print(dict2)