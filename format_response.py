
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_output = f"City: {name}\nCondition: {desc}\nTemperature (oF): {temp}"
    except:
        final_output = "There was a problem get the information"
    return final_output