
import os

from dotenv import load_dotenv


load_dotenv()

def get_env(key: str) -> str:
    temp = os.getenv(key)
    assert temp is not None, f'Environment variable {key} is not set'
    return temp


TOK = get_env('TOK')

BASE_URL_SINAPP = 'https://sinapp.hgdsas.com/'

BASE_URL_ALLIANZ = 'https://www.allia2net.com.co/ngx-epac-professional/public/home'
USER_ALLIANZ = get_env('USER_ALLIANZ')
PASS_ALLIANZ = get_env('PASS_ALLIANZ')

BASE_URL_FOLLOW_UP = 'https://sec-co.controlexpert.com/platform/'
USER_FOLLOW_UP = get_env('USER_FOLLOW_UP')
PASS_FOLLOW_UP = get_env('PASS_FOLLOW_UP')
