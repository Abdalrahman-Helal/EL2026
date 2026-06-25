"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""

    import requests

    ip_response = requests.get("https://api.ipify.org?format=json")
    ip_data = ip_response.json()
    print("Your public IP address is:", ip_data["ip"])

    location_response = requests.get(f'https://ipinfo.io/{ip_data["ip"]}/geo')
    location_data = location_response.json()

    print("Your location details are:")
    for key, value in location_data.items():
        print(f"{key}: {value}")
    return location_data


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
