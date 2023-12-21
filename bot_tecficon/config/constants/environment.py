
import os


def get_env(key: str) -> str:
    temp = os.getenv(key)
    assert temp is not None, f'Environment variable {key} is not set'
    return temp


TOK = get_env('TOK')

BASE_URL_SINAPP = 'http://10.8.0.1:8090/scriptcase/app/Hurtado_Gandini'

BASE_URL_ALLIA2 = 'https://www.allia2net.com.co/ngx-epac-professional/public/home'
USER_ALLIA2 = get_env('USER_ALLIA2')
PASS_ALLIA2 = get_env('PASS_ALLIA2')
