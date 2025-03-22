import os

class Config(object):
    BOT_TOKEN = os.environ.get("")
    API_ID = int(os.environ.get("23680771"))
    API_HASH = os.environ.get("0c58f3e3fecefc4a9d8e5bcf6968a106")
    AUTH_USER = os.environ.get('7796913460', '7109179238').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝗥𝗼𝘆 𝗝𝗮𝗮𝘁™"#Here You Can Change with Your Name  or any custom name or title you prefer
