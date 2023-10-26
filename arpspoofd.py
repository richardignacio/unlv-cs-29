import os
from pprint import pprint
from datetime import datetime

LOG_FILE = "duplicates.log"


def extract_arp_table():
    """ Project Task 1: ARP Table Extraction
        1. Execute the "arp -a" command
        2. Capture the output and store variable
        3. Parse the output in the variable
            a. Is it a multi-line string?  How do you break that up?
            b. How can you process multiple lines to find ones you are interested in?
            c. Find the lines you are interested in ("dynamic")
        4. Store the IP address to MAC mapping into a dictionary

        Hints
            # Execute a system command and store the output
            cmd_out = os.popen("dir").read()

            # Split a multi-line string, into separate lines
            lines = sample.splitlines()

            # From the arp table, you are interested in the
            # dynamic entries:
            # 192.168.7.231         c4-91-0c-ab-88-09     dynamic

            if "mysmallstring" in my_large_string:
                do_something
    """
    # Execute a system command to display the arp table and store the results
    cmd_out = os.popen("arp -a").read()

    # Break up the multiline string into separate lines
    lines_out = cmd_out.splitlines()

    ip_mac_map = {}
    for line in lines_out:
        if "dynamic" in line:
            fields = line.split()
            ip_mac_map[fields[0]] = fields[1]

    return ip_mac_map


def identify_duplicate_mac(arp_table):
    """ Project Task 2: Identifying MAC Address Duplication
        1. Get the arp table dictionary from the extract_arp_table function
        2. Create a variable to store MAC address that have been "seen"
        3. Iterate over the MAC addresses
            a. Compare them to MAC addresses that have already been seen
            b. Print a message if a duplicate is found
            c. Otherwise store the current MAC address in the variable of "seen" MACs
    """
    macs_seen = []
    for ip in arp_table:
        mac = arp_table[ip]
        if mac in macs_seen:
            print(f"Found duplicate MAC address: {mac}")
            log_duplicate(mac)
        else:
            macs_seen.append(mac)


def log_duplicate(mac):
    """ Project Task 3: Logging Events
    1. Get the duplicate MAC address
    2. Get the current date and time and store it in a variable
    3. Build a string to append to a log file
    4. Append that string to a log file

    Hint to get the current date/time:
        from datetime import datetime
        datetime.now()
    """
    timestamp = datetime.now()
    entry = f'{timestamp} arpspoof "Duplicate MAC address found: {mac}"\n'
    with open(LOG_FILE, "a") as log_file:
        log_file.write(entry)


def main():
    """
    The main program that calls the other functions
    """
    arp_table = extract_arp_table()

    # For testing only:
    # Add a duplicate MAC from your arp table (use a fake IP for the key)
    # arp_table["1.1.1.1"] = "38-f9-d3-2b-63-57"
    identify_duplicate_mac(arp_table)


if __name__ == '__main__':
    main()
