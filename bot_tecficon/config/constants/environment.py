
import os


temp = os.getenv('TOK')

assert temp is not None, 'Environment variable TOK is not set'
TOK: str = temp
