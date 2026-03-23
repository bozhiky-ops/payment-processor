# utils.py

import os
from datetime import datetime
from typing import Dict, List

def generate_invoice_number(prefix: str, invoice_date: datetime, customer_id: int) -> str:
    """Generate a unique invoice number based on the prefix, invoice date, and customer ID."""
    return f"{prefix}-{invoice_date.strftime('%Y%m%d')}-{customer_id:03d}"

def load_config() -> Dict:
    """Load the application configuration from a JSON file."""
    config_file = os.path.join(os.path.dirname(__file__), 'config.json')
    import json
    with open(config_file, 'r') as f:
        return json.load(f)

def validate_card_number(card_number: str) -> bool:
    """Validate a credit card number using the Luhn algorithm."""
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    
    checksum = 0
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    
    for d in odd_digits:
        checksum += d
    
    return checksum % 10 == 0