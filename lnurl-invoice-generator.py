import os
import requests
from lnurl import Lnurl, LnurlResponse, LnurlPayResponse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def pay_lnurl():
    # Get the lnurl link from the environment variable
    lnurl_link = os.getenv('LNURL_LINK')

    if lnurl_link is None:
        raise Exception('Please set the LNURL_LINK environment variable')

    # Probe the lnurl link to get its parameters
    lnurl = Lnurl(lnurl_link)
    r = requests.get(lnurl.url)
    
    if r.status_code != 200:
        raise Exception('Error contacting the lnurl service')
    
    res = LnurlResponse.from_dict(r.json())
    
    if not isinstance(res, LnurlPayResponse):
        raise Exception('This is not a valid lnurl-pay link')

    # Convert min and max sendable amounts to satoshis
    min_amount_sats = res.min_sendable // 1000
    max_amount_sats = res.max_sendable // 1000

    # Prompt the user to enter an amount within the min and max range
    amount = int(input(f'Please enter the amount in satoshis (between {min_amount_sats:,} and {max_amount_sats:,}): ').replace(',', '')) * 1000

    if amount < res.min_sendable or amount > res.max_sendable:
        raise Exception(f'Amount should be between {min_amount_sats} and {max_amount_sats} satoshis')

    # Create a payment request
    r = requests.get(res.callback, params={'amount': amount})

    if r.status_code != 200:
        raise Exception('Error creating payment request')

    payment_request = r.json()

    # Return the payment request to be paid by a lightning wallet
    return payment_request

payment_request = pay_lnurl()
print("Here's your invoice:\n" + payment_request['pr'])



