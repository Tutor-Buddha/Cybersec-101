import requests


# Function to fetch the ISP assigned IP address
def get_ip() -> str:
    # Log the start of the function
    print("Starting get_ip() function")
    try:
        ip = requests.get('https://api.ipify.org').text
    except:
        # Log the exception
        print("Exception occurred in get_ip() function")
        return "No internet connection"
    else:
        # Log the end of the function
        print("Ending get_ip() function")
        return ip
    

# Test the function
print(get_ip())