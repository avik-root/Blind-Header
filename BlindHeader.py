import requests # type: ignore
import pyfiglet # type: ignore
from termcolor import colored # type: ignore
def create_error_banner():
    banner = pyfiglet.figlet_format("BlindHeader", font="small")
    print(banner)
    banner = pyfiglet.figlet_format("by avik-root  Version 1.2", font="digital")
    print(banner)
    banner = pyfiglet.figlet_format("STABLE", font="digital")
    print(banner)
    print("Github: https://github.com/avik-root")
if __name__ == "__main__":create_error_banner()

def check_headers(url):
    headers_to_check = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy"
    ]
    try:
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
    while True:
        url = input("Enter the website URL (with http/https): ").strip()
        check_headers(url)
        continue_choice = input("Do you want to check another website? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Exiting the program. waka waka ee ee ")
            break
if __name__ == "__main__":
    main()
