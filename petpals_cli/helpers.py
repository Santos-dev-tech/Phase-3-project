from datetime import datetime
from termcolor import colored
import pyfiglet

def display_header(text):
    """Print styled application header"""
    print(colored(pyfiglet.figlet_format(text), 'blue'))
    print(colored("="*50 + f"\n{datetime.now().strftime('%Y-%m-%d %H:%M')}\n", 'yellow'))

def validate_age_input(age_str):
    """Ensure age is positive integer"""
    try:
        age = int(age_str)
        return age > 0
    except ValueError:
        return False