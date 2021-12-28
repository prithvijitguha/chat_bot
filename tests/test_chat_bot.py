from chat_bot.src.chat_bot import ChatBot

def test_keep_short():
    chat_bot_object = ChatBot()
    assert chat_bot_object.keep_short_conversation == 0

