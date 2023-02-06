# Bulk email-extractor-based-on-imap

email extractor based on imap bulk email extractor based on your list.txt 

A simple Python script that logs into a user's IMAP email account and removes any duplicates from the inbox. The script takes a list of email addresses and passwords and stores them in a queue. A function is then called to iterate over the queue, log into each email account, and search for duplicates. If duplicates are found, they are marked for deletion and the mailbox is expunged.

Requirements.

imaplib
email
threading
queue
time
socket
socks
re


pip install -r requirements.txt

Usage
Store the email addresses and passwords in the file list.txt, separated by a colon :.
Run the script: python email_duplicate_remover.py
The script will log into each email account, search for duplicates, and remove them.
The email addresses that have been successfully logged into and processed will be stored in the file harvest.txt.
The duplicates found in each inbox will be stored in the file duplicates.txt.
Configuration
The script includes an optional proxy configuration that can be enabled by setting use_proxy to True. The proxy type, address, and port can be specified in the proxy_type, proxy_addr, and proxy_port variables, respectively.

Note
This script is intended for educational purposes only and should not be used to access email accounts without proper authorization.
ALL TRUELY CODED BY CHATGPT FULLY CREDIT TO Yuhuang Hu (miybvladi) @miybvladi who created this amazon new era were the task is handle by our assistance 
and its very usefull for a coders, webmaster, and a content writer and many more to discover

