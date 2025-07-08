import requests

def get_exchange_rates(base_currency):
    """Fetches exchange rates from the API for a given base currency."""
    api_url = f"https://open.er-api.com/v6/latest/{base_currency}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        print(data)
        if data.get('result') == 'success':
            print(data['rates'])
            return data['rates']
        else:
            print("API did not return a successful result.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def convert_currency(amount, from_currency, to_currency, rates):
    """Converts an amount from one currency to another using the provided rates."""
    if not rates or to_currency not in rates:
        print(f"Conversion rate for {to_currency} not found.")
        return None
   
    rate = rates[to_currency]
    converted_amount = amount * rate
    return converted_amount

# --- Main script ---
bases =input("Enter the base currency : ")
base=bases.upper()
targets = input("Enter the target currency : ")
target=targets.upper()
amount_to_convert = 1

print(f"Fetching latest rates with base currency {base}...")
exchange_rates = get_exchange_rates(base)

if exchange_rates:
    converted_value = convert_currency(amount_to_convert, base, target, exchange_rates)
    if converted_value is not None:
        print(f"{amount_to_convert} {base} is equal to {converted_value:.2f} {target}")
