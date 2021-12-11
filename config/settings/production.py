from .base import *  # noqa F403
from .base import env

# 지정된 호스트만 접속 가능 ( 반드시 명시해줘야함 )
ALLOWED_HOSTS = env.get("ALLOWED_HOSTS", default="example.com").split(",")

print(ALLOWED_HOSTS)
