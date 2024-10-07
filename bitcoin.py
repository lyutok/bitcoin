import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        number = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rate = float(response.json()["bpi"]["USD"]["rate"].replace(",", ""))
    except ValueError:
        sys.exit("Command-line argument is not a number")

    except requests.RequestException:
        print("Invalid request answer")
    else:
        print(f"${rate * number:,.4f}")


main()
