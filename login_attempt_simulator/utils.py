"""Utility functions for the login attempt simulator."""

import itertools
import json
import random
import string

def make_userbase(out_file):
    """Generate a userbase and save it to a file."""
    with open(out_file, 'w') as user_base:
        for first, last in itertools.product(
            string.ascii_lowercase, ['smith', 'jones', 'kim', 'lopez', 'brown']
        ):
            user_base.write(first + last + '\n')
        for account in ['admin', 'master', 'dba']:
            user_base.write(account + '\n')

def get_valid_users(user_base_file):
    """Read in users from the userbase file."""
    with open(user_base_file, 'r') as file:
        return [user.strip() for user in file.readlines()]

def random_ip_generator():
    """Randomly generate a fake IP address. Not all these will be valid."""
    return '%d.%d.%d.%d' % tuple(
        random.randint(0, 255) for i in range(4)
    )

def assign_ip_addresses(user_list):
    """Assign users 1-3 IP fake addresses, returning a dictionary."""
    return {
        user : [
            random_ip_generator() for i in range(random.randint(1, 3))
        ] for user in user_list
    }

def save_user_ips(user_ip_dict, file):
    """Save the mapping of users and their IPs to JSON file."""
    with open(file, 'w') as file:
        json.dump(user_ip_dict, file)

def read_user_ips(file):
    """Read in the JSON file of the user-IP mapping."""
    with open(file, 'r') as file:
        return json.loads(file.read())