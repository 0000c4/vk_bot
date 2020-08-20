import vk_api
import time
import settings
import getText
vk_session = vk_api.VkApi(settings.login,settings.password)
vk_session.auth()
vk = vk_session.get_api()
session_api = vk_session.get_api()
vk = vk_session.get_api()
while True:
    vk.wall.post(owner_id = settings.id,message = getText.get_text())
    time.sleep(settings.interval)
