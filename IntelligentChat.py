from wxpy import *

bot = Bot(cache_path=True)

my_friend = ensure_one(bot.search('人生如梦'))

turing = Tuling(api_key='7e239ea4ae684326a95e9cce4f99bd56')


@bot.register(my_friend)
def reply_my_friend(msg):
    resp = turing.do_reply(msg)
    print(msg, ' ', resp)


embed()
