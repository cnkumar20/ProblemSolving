def fiddle(dict0):
    print(dict0["lname"])
    print(dict0.pop("address"))
    print([x for x in dict0.keys()])
    print(len(dict0))


if __name__=="__main__":
    dict0 = dict()
    dict0["name"]="Nandiesh"
    dict0["lname"]="Chandregowda"
    dict0["address"]="Chicago"
    fiddle(dict0)

    
