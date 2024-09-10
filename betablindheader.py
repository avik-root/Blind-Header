import requests  # type: ignore
import pyfiglet  # type: ignore
from termcolor import colored  # type: ignore
import socket  # type: ignore
import random

banner1 = pyfiglet.figlet_format("BlindHeader", font="small")
banner2 = pyfiglet.figlet_format("by avik-root", font="digital")
banner3 = pyfiglet.figlet_format("Version 1.5", font="digital")
banner4 = pyfiglet.figlet_format("BETA", font="digital")

def random_color():
    return f"\033[38;2;{random.randint(0, 255)};{random.randint(0, 255)};{random.randint(0, 255)}m"

def get_ip_address(url):
    try:
        domain = url.replace("http://", "").replace("https://", "").split('/')[0]
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        print(f"Error retrieving website IP address: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error as e:
        print(f"Error retrieving local IP address: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        return public_ip
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving public IP address: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def check_headers(url):
    headers_to_check = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy"
    ]
    try:
        local_ip = get_local_ip()
        public_ip = get_public_ip()
        if local_ip and public_ip:
            print(f"Local Machine IP address: {colored(local_ip, 'yellow')}")
            print(f"Your Public IP address: {colored(public_ip, 'blue')}")
        ip_address = get_ip_address(url)
        if ip_address:
            print(f"Website IP address: {colored(ip_address, 'cyan')}")
        response = requests.get(url)
        enabled_count = 0
        result = f"Checking security headers for {url}:\n"
        for header in headers_to_check:
            if header in response.headers:
                enabled_count += 1
                result += f"{header}: {colored('Enabled', 'green')}\n"
            else:
                result += f"{header}: {colored('Disabled', 'red')}\n"
        if enabled_count == 5:
            grade = colored("A+", 'green')
        elif enabled_count == 4:
            grade = colored("A", 'light_green')
        elif enabled_count == 3:
            grade = colored("B", 'yellow')
        elif enabled_count == 2:
            grade = colored("C", 'orange')
        else:
            grade = colored("F", 'red') 
        result += f"Overall Grade: {grade}\n"
        print(result)
        with open("history.txt", "a") as file:
            file.write(result + "\n")
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not connect to {url}")
        return ""

def main():
    print(random_color() + banner1 + "\033[0m")
    print(random_color() + banner2 + "\033[0m")
    print(f"{random_color()}{banner3}\033[0m" + f"\033[91m{banner4}\033[0m")
    print("\033[91mGithub: https://github.com/avik-root\033[0m\n\n")
    while True:
        url = input("Enter the website URL (with http/https): ").strip()
        check_headers(url)
        continue_choice = input("Do you want to check another website? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Exiting the program, waka waka ee ee.")
            break

if __name__ == "__main__":
    main()