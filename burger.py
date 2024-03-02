import requests

def scan_roblox_users(keyword, limit):
    api_url = f"https://users.roblox.com/v1/users/search?keyword={keyword}&limit={limit}"
    
    try:
        response = requests.get(api_url)
        data = response.json()

        if 'data' in data and data['data']:
            users = data['data']
            for user in users:
                print(f"Username: {user['name']}, UserID: {user['id']}")
        else:
            print("No users found with the specified keyword.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage
scan_roblox_users("terrorism", 1000)
