def Enhance(UserResponse: str): # : for the type of input

    URL = ""

    for index in UserResponse:
        if (index == '?'):
            break
        else:
            URL = URL + index 

    return URL
