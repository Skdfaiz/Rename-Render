# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26703600")

API_HASH = os.environ.get("API_HASH", "3693d895bdc8900c62464c59171419ab")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6861281486:AAFMnDwZxZXR9Xpm3_rD5Ke_5TtaZ9Cz3CI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "JadeDynastyAll") 

             # Don't Remove Credit @JadeDynastyAll
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://faizalamskd92:3PiI2oBwT6o916KS@cluster0.nfmfs2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1603868167').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
