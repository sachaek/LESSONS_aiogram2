from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("IP")  # Тоже str, но для айпи адреса хоста
QIWI_TOKEN = env.str("QIWI_TOKEN")
WALLET_QIWI = env.str("WALLET_QIWI")
QIWI_PUBKEY = env.str("QIWI_PUBKEY")

banner_users = [1241241, 214124]