import os

api_id = 24192661
api_hash = "810a6dc0b2c2bf4db55db3a9ad999b56"
bot_token = "7074408721:AAEtp4ZeiFq-n8UjWTjrNsrMmRfZ_RX2Tko"
# Split the AUTH_USERS string and convert each part to an integer
#auth_users_str = os.environ.get("AUTH_USERS")
#auth_users_list = auth_users_str.split(', ')
auth_users = 5427627648

sudo_user = 5427627648
log_channel = -1002079009211

# Now you can use the 'auth_users' list as needed
print(f"API ID: {api_id}")
print(f"API Hash: {api_hash}")
print(f"Bot Token: {bot_token}")
print(f"Authorized Users: {auth_users}")
print(f"Sudo User: {sudo_user}")
print(f"Log Channel: {log_channel}")
