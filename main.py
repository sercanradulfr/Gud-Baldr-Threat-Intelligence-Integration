import requests
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Gud Baldr")
print(ascii_banner)


API_BASE_URL = "https://api.threatintelligenceplatform.com/v1/infrastructureAnalysis"

def fetch_threat_intelligence(domain_name, api_key):
    url = f"{API_BASE_URL}?domainName={domain_name}&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any unsuccessful status codes
        
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return None

def print_threat_intelligence(data):
    if isinstance(data, list):
        for item in data:
            print_threat_intelligence(item)
            print("\n")
    elif isinstance(data, dict):
        print("Threat Intelligence Data:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(data)

def main():
    api_key = input("Enter your API key: ")
    domain_name = input("Enter a domain name: ")
    
    threat_intel = fetch_threat_intelligence(domain_name, api_key)
    
    if threat_intel:
        print_threat_intelligence(threat_intel)
    else:
        print("No threat intelligence data found for the given domain name.")

if __name__ == "__main__":
    main()
