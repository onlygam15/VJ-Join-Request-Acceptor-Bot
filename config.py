from os import environ

API_ID = int(environ.get("API_ID", "29527236
"))
API_HASH = environ.get("API_HASH", "528c2db679cf9f523ff64952fcdeffd4")
BOT_TOKEN = environ.get("BOT_TOKEN", "7969060800:AAFY3vawWS-M0nwxr1Am0Pc29kruqpdWvuo")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", "Imtudu_accept2bot"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://onlygam15:qzSZ2sfllQyZCUp5@cluster0.jku0t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "onlygam15")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
