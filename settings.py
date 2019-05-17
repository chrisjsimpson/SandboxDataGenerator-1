OAUTH_CONSUMER_KEY = '52twqicuegicqljbpsb5macoj4on22ss05vm0yms'
OAUTH_CONSUMER_SECRET = 'alshky0ujfeuattvqkqzi12wfofcmbges5wuescu'

API_HOST = 'https://openlab.openbankproject.com'

API_VERSION = '3.1.0'

REDIRECT_URL = 'http://127.0.0.1:9090'

OAUTH_TOKEN_PATH = '/oauth/initiate'
OAUTH_AUTHORIZATION_PATH = '/oauth/authorize'
OAUTH_ACCESS_TOKEN_PATH = '/oauth/token'

DIRECTLOGIN_PATH = '/my/logins/direct'

ADMIN_USERNAME = "pflee"
ADMIN_PASSWORD = "Pflee@0218"

FILE_ROOT = "./output_path/"

VERIFY = True if API_HOST.startswith("https") else False

OUTPUT_PATH = "./output_path/"

INPUT_PATH = "./input_file/"
DATASET_PATH = "{}dataset.xlsx".format(INPUT_PATH)
OPTIONS_PATH = "{}options.xlsx".format(INPUT_PATH)
USER_NUM = 2
BANK_NUMBER=3
BRANCH_NUMBER=4
ATM_NUMBER=6
PRODUCT_NUMBER=10
COUNTRY='MXN'
OUTPUT_DIR='./output_path'