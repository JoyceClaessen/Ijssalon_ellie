def presenteer(mijn_dict,totaal):
    '''
    mijn_dict={
        ":":10,
        "vlees:":25,
        "overig:":15
        }
    totaal = 50
    '''
    for k,v in mijn_dict.items():
        print(k,v)
    print("=====================")
    return(totaal)