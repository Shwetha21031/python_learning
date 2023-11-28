# for encoding , decoding , returning , assigning the tokens
import time # to set expiration time
import jwt # encoding and decoding generated strings
from decouple import config # change params / stores (in ini or .env file) them without redeploying app 

JWT_SECRET = config("secret")
JSWT_ALGORITHM = config("algorithm")

# to return token (JWT)
def token_response(token:str):
    return{
        "access token" : token
    }

# signing the JWT string  
def signJWT(userID : str):
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 600
    }
    token = jwt.encode(payload , JWT_SECRET ,algorithm=JSWT_ALGORITHM)
    return token_response(token)

# decoding the jwt
def decodeJWT(token : str):
    try:
        decode_token = jwt.decode(token , JWT_SECRET , algorithm=JSWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time () else None
    except:
        return {}
    