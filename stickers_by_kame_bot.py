import telebot
bot = telebot.TeleBot('_')

from telebot import types

from random import choice

#Кнопки
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    cats_button = types.KeyboardButton('Котики!🐱')
    evangelion_button = types.KeyboardButton('Ева🍉')
    meme_genshin_button = types.KeyboardButton('Геншин мемы🎮')
    ayka_genshin_button = types.KeyboardButton('Аяка❄')
    honkai_sr_button = types.KeyboardButton('Хср⭐')
    haikyuu_button = types.KeyboardButton('Волейбол🏐')
    tokyorevengers_button = types.KeyboardButton('Tokyo Revengers 🥋')
    yellowboy_button = types.KeyboardButton('Yellow Boy 😁')
    markup.add( cats_button, evangelion_button, meme_genshin_button, ayka_genshin_button, honkai_sr_button, haikyuu_button, tokyorevengers_button, yellowboy_button)

    bot.send_message(message.chat.id, text, reply_markup=markup)

# Условия кнопок
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Котики!🐱':
        bot.send_sticker(message.chat.id, choice(cats))
    elif message.text == 'Ева🍉':
        bot.send_sticker(message.chat.id, choice(evangelion))
    elif message.text == 'Геншин мемы🎮':
        bot.send_sticker(message.chat.id, choice(meme_genshin))
    elif message.text == 'Аяка❄':
        bot.send_sticker(message.chat.id, choice(ayka_genshin))
    elif message.text == 'Хср⭐':
        bot.send_sticker(message.chat.id, choice(honkai_sr))
    elif message.text == 'Волейбол🏐':
        bot.send_sticker(message.chat.id, choice(haikyuu))
    elif message.text == 'Tokyo Revengers 🥋':
        bot.send_sticker(message.chat.id, choice(tokyorevengers))
    elif message.text == 'Yellow Boy 😁':
        bot.send_sticker(message.chat.id, choice(yellowboy))

text = 'Привет! Это стикер-бот с разными категориями.\nЧтобы получить рандомный стикер из категории, нажмити на кнопку с данной категорией.' \
       '\nСписок категорий: ' + '\nКотики!🐱 - стикеры с котиками!' + '\nЕва🍉 - стикеры по аниме "Евангелион"' \
       '\nГеншин мемы🎮 - мемные стикеры по игре "Genshin Impact"' + '\nАяка❄ - стикеры с Камисато Аякой из игры "Genshin Impact"' \
       '\nХср⭐ - стикеры по игре "Honkai: Star Rail"' + '\nВолейбол🏐 - стикеры по аниме и манге "Haikyuu"' \
       '\nTokyo Revengers 🥋 - стикеры по аниме и манге "Токийские мстители"' +  '\nYellow Boy 😁 - стикер покажет какой ты сегодня Yellow Boy'

# Списки стикеров
cats = ['CAACAgIAAxkBAAEIKNBkExp2i7unEV_ETQNotMmunTGBbwACbRQAAl6xeUp5Q2lrrAQM1i8E',
        'CAACAgIAAxkBAAEIKNJkExqC3tvcMc4Pa2D0toanGAHSggACLw4AAlMVgUqQfyP64FsyyS8E',
        'CAACAgIAAxkBAAEIKNhkEyD5fg1nVijkrnHXZbZ06MhBbgACZxEAAitIgUofPpstnaB3Oy8E',
        'CAACAgIAAxkBAAEIKNpkEyD9DenKpvS0s0KyAry_rovwFwACKhIAAm-M0UqNNzGekOJWLS8E',
        'CAACAgIAAxkBAAEIKNxkEyEEv2ErJhNPEPHBJkD4KS9l_wACGRAAAg_dAUv-T2_DH4Cepy8E',
        'CAACAgIAAxkBAAEIKN5kEyEbQ-BlW6Od9Ljq6QxY0m0EVAACuBQAAgtRqUmQVgFjZEaejS8E',
        'CAACAgIAAxkBAAEIKOJkEyE_3Lb5D1TABSqhpeXsGqdVzQACdAoAArG7YUvJ7VhImW0fjy8E',
        'CAACAgIAAxkBAAEIKORkEyFE5gm8gbmObyhuYP5LEmTJigACkgoAAjVaYEuVpIvhVcnrYy8E',
        'CAACAgIAAxkBAAEIellkLqjL8zC6srmIdb7NWYgxqcjCHAACEw8AAprVyEp86gUhdfPIZy8E',
        'CAACAgIAAxkBAAEIel1kLqkN8e5m1QFfg99IjVZojHbDsQACiREAAsinEEu30fzOY_nZZC8E',
        'CAACAgIAAxkBAAEIemFkLqkvwO9kBetlfTLxQrgAAZjDxiwAAv0SAAIqncBIp3nCNHmeuF4vBA',
        'CAACAgIAAxkBAAEIemNkLqlyUQUEjlCDWbrmIUyaAlqZCAACuhYAAo3h2UrUz88XlgEDFy8E',
        'CAACAgIAAxkBAAEIem1kLqozRqdFn20VatzD5dC7CynESgACrBUAAl9M0UobCDPwT3UoJy8E',
        'CAACAgIAAxkBAAEIem9kLqp2u35JEKNzP7l4-ZojlzrJvAACHwsAAtpnYEtBfYlplY8Qyi8E',
        'CAACAgIAAxkBAAEIenFkLqqLeAyaUoJ34DUQEoP5Red0JQACcSoAApHGaUj4_IgF-d-MLy8E',
        'CAACAgIAAxkBAAEIv9JkSna1cU2w0JkVfptTpH-YVK3nsAAC0Q8AAqeAyEtx1lPcgJ-pWS8E',
        'CAACAgIAAxkBAAEIv9RkSnbAXnh4tXplVTWbec-Ou1f1AgACkBUAArTlyUvP28AHDr-D6S8E',
        'CAACAgIAAxkBAAEIv9ZkSnbMO6O3e1odKARZ-WUDWEntaQACxhQAAnJF0EtrnGFaWCKN9y8E',
        'CAACAgIAAxkBAAEIv9hkSnbkA_pFma0d9sdoHzL-2ZF43wAC-xQAAoQ-yUtydkanKpGfri8E',
        'CAACAgIAAxkBAAEIv9pkSnbz5bsdE8OFTbu7k2U1xFaW1QAC1RUAAse30EtuFXv6xli5QS8E',
        'CAACAgIAAxkBAAEIv9xkSnb7ykdGfPlYAXa64d3Sss9SwQACehMAAq1U2EursWkfUowXbC8E',
        'CAACAgIAAxkBAAEIv95kSncORt2IMEHJPeoyUug5qcDwIAACcx0AAvGXaErzilkpAabKKi8E',
        'CAACAgIAAxkBAAEIv-BkSncffv1_yaAHVe_j2F8xgHeJbQAClyAAAt88OUtsjjyKWQ5bXi8E',
        'CAACAgIAAxkBAAEIv-JkSnclIklgu4mxqa07U03A9hDntgACaR4AAh3tYUkpdZKPeRAC_i8E',
        'CAACAgIAAxkBAAEIv-RkSncxlmDKXnpLPNGmsybP4kp_2gACTCQAAt21aUvCnrO-C8Dk9y8E']
# 25 стикеров

evangelion = ['CAACAgIAAxkBAAEIelBkLqgjKfAJwkLoYj_veLWEY-7fIQACHA8AAquCwUlpn5l-z05hfi8E',
              'CAACAgIAAxkBAAEIemVkLqmdxHDiTE0XI7v3wUJ7SCtplQACkQoAAh0QwUmJ36bcjBS7Hy8E',
              'CAACAgIAAxkBAAEIemdkLqmwL0JwQdahLSXDdc9JaiE5cAACZQoAAjGpyEkO4giduKwAAUgvBA',
              'CAACAgIAAxkBAAEIemlkLqm-DSe0nuhWTuVVsVML-EEHCgACgAsAAmY0wEnS59p1Rg4tOS8E',
              'CAACAgIAAxkBAAEIemtkLqnAtjeBWYeh4DRlPGvN_dpWYgACHQ0AAmHDwEkNCTx_LKbElC8E',
              'CAACAgIAAxkBAAEIv5JkSmz-H6f_ZMmPnLioq_wrMRLVogAC2AsAAmzHwEnVhqup0eb15y8E',
              'CAACAgIAAxkBAAEIv5ZkSm0W4VvrjZ3XsTEI-GP-waAZqQACXA0AAtU_wEmQf7nHDPWr2i8E',
              'CAACAgIAAxkBAAEIv5xkSm5BvdIxEGp-UyAOguV0cqKaCgAC9g4AAihHaEo7YMnotZZI_S8E',
              'CAACAgIAAxkBAAEIv55kSm94LpPoxUbnTj33Wb0Vgoz_3wACYgADfpo8IH9edQItVaBxLwQ',
              'CAACAgIAAxkBAAEIv6BkSm-ghmIDNqxTqkzWbufpYd_KLAACeQADfpo8IILmpW4C_C5nLwQ',
              'CAACAgIAAxkBAAEIv6JkSm-t3VuSmK5VzOUNiSL6iamv4AACUg4AArGFkEkpBAhBGp_5ZC8E',
              'CAACAgIAAxkBAAEIv6RkSm_cBC-OgNNd_e-9-vLfyq9fvwACyw0AAugG6EnC34J8iDXjcy8E',
              'CAACAgIAAxkBAAEIv6ZkSm_25mkk-zBhG6PmXhClwW9FcwACgwADfpo8IMsdQMTQcNshLwQ',
              'CAACAgIAAxkBAAEIv6hkSnAR5j3hWmBZh7UD0dcvg8GW-QACUQwAAvyLoEoQagIAAcWcvS4vBA',
              'CAACAgEAAxkBAAEIv69kSnGwNj_uW2tZQcnOa83pdbQhtAACtQADEstAR9qzdnvZiRN8LwQ',
              'CAACAgEAAxkBAAEIv7FkSnG7Zq4kEV--t4t4Y47_PfKhVgACHgEAAs6HYEdWcfRi1JrlPy8E',
              'CAACAgEAAxkBAAEIv7NkSnHHZLJhDdgwsue5LDk7er4gQwAC6AAD3zKARwnFoJVb935cLwQ',
              'CAACAgIAAxkBAAEIv7VkSnHNW6R9j5b9k6HXv521ltLYTwACSRcAArIdIUnKmtUFK4KACy8E',
              'CAACAgIAAxkBAAEIv7dkSnHrOfCeUhvmQbLMnP0Kwq9i6wACnhMAAqA9KUnBy5YAART_VDovBA',
              'CAACAgIAAxkBAAEIv7lkSnIO_BBlUPRYGChWcThtu3QxxAACAhcAAmJzIEnNWsEuixP0Ai8E',
              'CAACAgIAAxkBAAEIv7tkSnIRSaK3mInFUnA1hFtWCaJ3vgACXhkAAq0OKEnuHwoZsER81C8E']
# 21 стикеров

meme_genshin = ['CAACAgQAAxkBAAEIenNkLqtUWdhadhN988x5JpPPfiwg0AACgAoAAl9pwFHs_MNRzFqssS8E',
                'CAACAgQAAxkBAAEIenVkLqtk8vdu4Ber4miTzzvoqs0U-QACuAwAAndOwFGF-PTmp4n4RS8E',
                'CAACAgQAAxkBAAEIendkLqtqr-nHj0SlvCtig8T6mEeEZQACzQkAAoReuFHXOBPPM6sC3C8E',
                'CAACAgIAAxkBAAEItypkRxcTRYjv5mHk00tfaPblp2LOfwACyxIAAq2x-EoWoFVlqeuf4i8E',
                'CAACAgIAAxkBAAEItytkRxcUaZ0LWulsYre7ay3tw6CPtwACsA0AAiIDAAFL-P_1ebo1ULMvBA',
                'CAACAgIAAxkBAAEIty5kRxcjph09ema4M0gmXIn0-rDemQACxw8AAu7vAAFL7tmquYdXjWEvBA',
                'CAACAgIAAxkBAAEItzBkRxcrmL6YP36O11w9-CrMduPaGwACWQoAAilEAAFLaDiG_r-6TNQvBA',
                'CAACAgIAAxkBAAEItzJkRxdcYCyUQH5QQBsckJSro7SIqAAC6BUAAudxCUq9Pqa8ghsaDy8E',
                'CAACAgIAAxkBAAEItzRkRxeINKqO6bOuWvIiKZSmeEakcgAC1xAAAsrxQUiyse4LT01jwC8E',
                'CAACAgIAAxkBAAEItzZkRxfP7Wx1csbaPRcEn3C6NKiuZAAC0hQAAs-jaUnpaJZ2eEuAKy8E',
                'CAACAgIAAxkBAAEItzhkRxfdOOOyNUHoGRH50UjvQDcx0AACKhYAAlGCaEmjSZ6XD-w9bi8E',
                'CAACAgIAAxkBAAEItzpkRxfxBhsb7a-jV90rQKgINYqscwACBAADmWuhLSkE6AJSQ16WLwQ',
                'CAACAgIAAxkBAAEItzxkRxf3dkdBAQNLIbqB6QcUgtT_OQACFAADmWuhLRgNnoREOlHkLwQ',
                'CAACAgIAAxkBAAEItz5kRxf7t1MJ8DwTsZSS11k2Kp5THAACIAADmWuhLRCe-WiDOf70LwQ',
                'CAACAgIAAxkBAAEIt0BkRxgBNyspdYGZ-HaJCUvGiBKpNQACPAADmWuhLZvDhYqZmQcyLwQ',
                'CAACAgIAAxkBAAEIt0JkRxgEG-cpZkcJyDJplSedVgMvSwACNAADmWuhLVRFN0hy4mHmLwQ',
                'CAACAgIAAxkBAAEIt0RkRxgMtsIOgh-9zx32wQhrLxOqjgACTwADmWuhLT3Hxsvdix0WLwQ',
                'CAACAgIAAxkBAAEIt0ZkRxgXcTjFz0KDDUkomY2kyFCs0wACVBQAAjDa2Emgh0TQRB6LVC8E',
                'CAACAgIAAxkBAAEIt0hkRxgoktLNuJqMYbQguJKepLnllwACiA8AAqhQ0Elsa6js_I3KmS8E',
                'CAACAgIAAxkBAAEIt0pkRxpwe77vTnfyS5JN9_Jylg3xKAACuykAArOY6EonzuwNs2QMFC8E',
                'CAACAgIAAxkBAAEIt0xkRxqoifj_wFbN8nBfjdRpxNRJbwAC4RoAAu2aaUnGnq970QABxPovBA',
                'CAACAgIAAxkBAAEIt05kRxqusqWeLqlR2ptspYEEJRdOCwACXhkAArFJYEm5dXyqu3yomS8E',
                'CAACAgIAAxkBAAEIt1BkRxq9giEx5IUCvy1h9PhByTm2PQACHA8AAstfsEs2YxMMDIhcGC8E']
# 23 стикеров

ayka_genshin = ['CAACAgIAAxkBAAEIeqdkLq0AASfp6K9mJnwRQhOVhOUe1FMAAlsVAAI87hBICorpBtK6BKUvBA',
                'CAACAgIAAxkBAAEIeqlkLq0QRGUvtcLiNMVyB7zDPoGVogACGRYAAvbzEEiWqk42ajPLNS8E',
                'CAACAgIAAxkBAAEIeqtkLq0THGF2UskbnCzCEtEO5rOkxQACfxkAAio6EUgOuzO0zpE4ci8E',
                'CAACAgIAAxkBAAEIeq1kLq0WU5dAVchnd2ZiXDnTunih0gAC0xYAAscAAQlIx792OsfF2-IvBA',
                'CAACAgIAAxkBAAEIeq9kLq0aK4H4LEULhM1UwtHD50usZAACTBUAAlYjCUhScZqZ6mupFS8E',
                'CAACAgIAAxkBAAEIerFkLq0d6frRo7x4wk8mQG0wccveNgAC0hQAAs0LCEjY8lbUCPvrMy8E',
                'CAACAgIAAxkBAAEIerNkLq05OLl5KRfeEqZ3FiuRZastIgACgBQAArhTCUjjs-3p-5TL4C8E',
                'CAACAgIAAxkBAAEIerVkLq0-mf2xT75J9nHnTK0x3430mQAC1BIAAs4GCUgC_ShdP0-PTy8E',
                'CAACAgIAAxkBAAEIerdkLq1B8AXN5dLd6c67z9zeJ7PbIAACRxYAAgEwEEiUelcbOE9SSy8E',
                'CAACAgUAAxkBAAEIweZkSxArM6XrrfsJfevLv8IR4b2OMQACNgoAAjvCgVTBIeMw51C6wi8E',
                'CAACAgUAAxkBAAEIwehkSxAw_W1E1qPADmYeoOiWFfAokwACPQMAAlhViFT4fEVAXHsaHy8E',
                'CAACAgUAAxkBAAEIwepkSxA1p42wl04qbN3znQ0gY5mwNQACdQIAAoX2gVTfxma3mmnbwi8E',
                'CAACAgUAAxkBAAEIwexkSxA4b5Gn3lzs9Em3n4tEJuqZsAACVgMAAgExgFSefzIgdcHPvy8E',
                'CAACAgUAAxkBAAEIwe5kSxA8p5v4sQovjt1PKxgozEh-CwACxAUAAgfugVSYI9xdvRcHQy8E',
                'CAACAgUAAxkBAAEIwe9kSxA8mm2S0izgGF7h9-ZjdkHYhwACqgMAAsHrgVRHKAVxKIYAAWovBA',
                'CAACAgUAAxkBAAEIwfJkSxBUmnl2UgnMOEtyBAXQWz8X1AACuwIAAlnKgVSiKSPpP03I1C8E',
                'CAACAgIAAxkBAAEIwfZkSxE7yn17dbDMqcLD2_FMF2i2YgAC5xMAAhAOkEqc-ImbY80GKC8E',
                'CAACAgIAAxkBAAEIwfhkSxE9dWTMxaqiPXm8tYqOCfAoGAACORYAAslpkUpVIHrNryQDbS8E',
                'CAACAgIAAxkBAAEIwfpkSxE_DjsbF9gXAAGb0wPacmSlwlIAAqsXAALQgZBKh_Nlnpk4eGgvBA']
# 19 стикеров

honkai_sr = ['CAACAgIAAxkBAAEI0D9kUFl84WF_WQfeDsPlTWnA2EZIAgACVCcAAkHoCEsXkWMpmSTCei8E',
             'CAACAgIAAxkBAAEI0EFkUFmFEIlv7AOhmxhPut8GiK3HjwACNicAAvd1CEsd-kWrz_nQSi8E',
             'CAACAgIAAxkBAAEI0ENkUFmKi6oZtQVXJQMZh0fbGFA1XAACfCUAAsgUCEsmt1WC7rPwCi8E',
             'CAACAgIAAxkBAAEI0EVkUFmWczQYaYLdc7cg7Ues850qdQACZysAAgQoUUoa0wIdwsx-7i8E',
             'CAACAgIAAxkBAAEI0EdkUFmYl0qBLpQQIVRK_JRpGpGekAAC6icAAscWUErHaPwwtJ16JS8E',
             'CAACAgIAAxkBAAEI0ElkUFmhzS_kQfw5tXxZ1Lq3jDa9oQACdCcAAmslUEoNianCia2dwS8E',
             'CAACAgIAAxkBAAEI0EtkUFmymoWiIPgHjOBUOUTwz_pAZQACJSoAAj0v4UkAAddzYXPjWNIvBA',
             'CAACAgIAAxkBAAEI0E1kUFm7fEx-WYy7SY0I3Af2pUaluQACWygAAn0K4EktpcAdlyLaSy8E',
             'CAACAgIAAxkBAAEI0E9kUFpU-_9XUYoKlNpGrFXeoWfBCQACySUAAqOLsEogjQvELfh9by8E',
             'CAACAgIAAxkBAAEI0FFkUFpdXkUkGO0eMWSYqdK7qvgOTwAC9CEAAohZsUq9Rc8ukYhejC8E',
             'CAACAgIAAxkBAAEI0FJkUFpdPo8LWKT7sRy5NkoNvcGRjwACWiMAAtR6uUqD1hJa-n_sRS8E',
             'CAACAgIAAxkBAAEI0FRkUFpel8VFFCvcNYwYg-D739y__AACJCIAAo6YsUrp1MOOrD4rJS8E',
             'CAACAgIAAxkBAAEI0FdkUFpm5IpwtD-vMq_OVkREERotMgAC-ycAAiMasUrI4OkL-cDXOS8E',
             'CAACAgIAAxkBAAEI0FlkUFpo5CSfF22td606rQABYOqjbGIAAlIqAAIXDnlIvVepLnmFib0vBA',
             'CAACAgIAAxkBAAEI0FtkUFpqrlkCe-TEJg2rpIXY1gAB5sMAAoQnAAKJMHhIcwABTjtS_r95LwQ',
             'CAACAgIAAxkBAAEI0F1kUFpupyeUUUBeH8_AYH3PqGEDSQACUS4AAtgycUjeS9fOkCM_Ji8E',
             'CAACAgIAAxkBAAEI0F9kUFpyrR_xsKFICZxFUUEzwDGmLQACdiUAAoCleEg17-0N1h6Ahy8E',
             'CAACAgIAAxkBAAEI0GFkUFp02KbwdFyblgTIWOIOrOzZuwAC2ScAAqEPeEgvyHw5UEr0Ci8E']
# 18 стикеров

haikyuu = ['CAACAgIAAxkBAAEIwbhkSwdxD48HeeWTVqHGeNMIjXxuFAAChRAAAtTUYUsjZbSnToFi8y8E',
           'CAACAgIAAxkBAAEIwbpkSwd9NuuJa16V6PICRTohkz9dsgACtRMAAo66aEt1NS4G_dhaGC8E',
           'CAACAgIAAxkBAAEIwbxkSwi8FkgSKJ9_VAgJqbFxdMP6fgACAQAD0Iw9J8iY5sP-ssbtLwQ',
           'CAACAgIAAxkBAAEIwb5kSwjFUrcKXR-Zf1kJDGs_rxjj_AACBwAD0Iw9J6n-K-xv5XFCLwQ',
           'CAACAgIAAxkBAAEIwcJkSwjSczHwCesF-QucWr9DQKZ7WAACIgAD0Iw9J6o_YFXbruzwLwQ',
           'CAACAgIAAxkBAAEIwcRkSwjUET41hRiBgFK3QPvpd2mqZgACJQAD0Iw9J66Id1D5jbM3LwQ',
           'CAACAgIAAxkBAAEIwcZkSwjf9alKkQrdkprXrZYL_UWNKgACNgAD0Iw9J6pYZsN2Pb8MLwQ',
           'CAACAgIAAxkBAAEIwchkSwjj4-iODOpHkl8dG-O4mlIKkgACQwAD0Iw9J3-xhunYQOymLwQ',
           'CAACAgIAAxkBAAEIwcpkSwjlQqjQej9WBo3dJvbbTfY6_gACSQAD0Iw9JykqP2R1SHteLwQ',
           'CAACAgIAAxkBAAEIwcxkSwjrrCfH2vF-FspjfvZzg2Wb8AACtgsAAnDtiUuFrvq4cKOdSy8E',
           'CAACAgIAAxkBAAEIwc5kSwjzWSCOFWzpKjjdSu221rhwDwACdQwAAp06kEu-uPrVIlYnbS8E',
           'CAACAgIAAxkBAAEIwdBkSwj7KmHX4L5NN33VY2o8hl9iDAACVw4AAtBAiEstScgT9kYK_y8E',
           'CAACAgIAAxkBAAEIwdJkSwj_1al0D--CBDnd1Ms8QiktwQACHAwAAvyqkUvCyRfBNQnY6S8E',
           'CAACAgIAAxkBAAEIwdRkSwkAARrOqRKmLHBOM6yBX7BRCJ8AAi8MAAL9V4hLvCLE2AP-DPQvBA',
           'CAACAgIAAxkBAAEIwdZkSwkIZ70bmWmls5PxjWZEj0cVZwACCgsAAmPGCUjooFq8QYrQqS8E',
           'CAACAgUAAxkBAAEIwdhkSwoGG3_SBJJfsckTayFl-3Am3AACgQYAAvjeCFbEgrWZNCYEDC8E',
           'CAACAgUAAxkBAAEIwdpkSwoI4nJEzg90PpRCaDbLz5aUOgAC6AYAAkDRCVaHNNG0I3JvgS8E',
           'CAACAgIAAxkBAAEIwdxkSwoVZirRCORmNS5o06KvYRkPbQAC3BUAAonT2Ej94_TBtySNbS8E',
           'CAACAgIAAxkBAAEIwd5kSwoq3v9fbXuy_X2OoWRSENpIiwACiBYAAk0_4EgyDquR5EhN0S8E',
           'CAACAgIAAxkBAAEIweBkSwo6HkYY5YCqZ8S4MQ0ynm7UgQACRAAD0Iw9JxTWmcpmdqEkLwQ']
# 20 стикеров

tokyorevengers = ['CAACAgIAAxkBAAEIesZkLrb_qlsNFvBMNtggKluSIOPvkwACdw8AAmC-kEt1R8BU-GD85i8E',
                  'CAACAgIAAxkBAAEIeshkLrcGdMXpA43vUsbTya-ZCa2ZXQACpRAAAt12mUv-M6dXmAn4ly8E',
                  'CAACAgIAAxkBAAEIiPxkNKwvd8LxbjoqhSVgq0z_0t0EegACaxEAAjVeiEuMIilWj6LYTS8E',
                  'CAACAgIAAxkBAAEIiP5kNKxP8aYR9XQju59mID3xbHE2vAACwQ0AAoelkEtpZD8fve6Sjy8E',
                  'CAACAgIAAxkBAAEIiQABZDSsXBIgFmCDzi5ANQ6ybzTmlNYAAk8MAAJUCvBISBVr4kFDMGsvBA',
                  'CAACAgIAAxkBAAEIiQJkNKxfmt8-u-Oac3Xar5QNS-kiSQAC-w4AAryD8UgUDTZyIBip1i8E',
                  'CAACAgIAAxkBAAEIiQRkNKxhVtBzjZbf2DFfBJ3EL8g28gACbA4AAp4J8Uiotm7R4L5e8y8E',
                  'CAACAgIAAxkBAAEIiQZkNKxuh_4l3q9CZPDiYzqeMzI-8wACixQAAgE76EgFLbdLRwJwOi8E',
                  'CAACAgIAAxkBAAEIiQhkNKxyCuIOaHJ64ncqh8y0512mDwACGQ8AAoOw8UgyQkN_pW5k5S8E',
                  'CAACAgIAAxkBAAEIiQpkNKx071Xq21cviUBSo94qTDpNegACdxEAAuWY8Ej6AAEv4__ssvMvBA',
                  'CAACAgQAAxkBAAEIiQxkNKz9AaNs0sk0IPz5pbfwFlgC0QACewwAAoIkAVFSINVrP1LvHC8E',
                  'CAACAgIAAxkBAAEIiQ5kNK0Ynr7YkTkowHXZP6b_DHTE4gACQBIAAjiGOUhu9wMjsbkNmS8E',
                  'CAACAgIAAxkBAAEIiRBkNK0aCGGTCfZhCu-52jSQio_hugACwQ4AAop0QUg0WxBJoa14ay8E',
                  'CAACAgIAAxkBAAEIiRJkNK0f684pxjq-b0jpGuOCr7kpngACPhEAApyuQUi1dTzHBXiZoS8E',
                  'CAACAgIAAxkBAAEIiRRkNK0quIA1ggmdB3HQc2uL1MHOEQACPRAAAqgeOUgcGqxYpP1bMi8E',
                  'CAACAgIAAxkBAAEI0AlkUE-aCGzdoSmh97zk4p7eVJMhgAACPQ4AApjhOEgyU50Iff08Ai8E',
                  'CAACAgIAAxkBAAEI0A1kUE-k02bo4fkE_xB_NId7FvE8UwACcg4AAof3QEjeiL60GAGLki8E',
                  'CAACAgIAAxkBAAEI0BBkUE-mBRqHuFD-H_w21I__VUKLNgACGxAAAtVrQUhGRTiY1P3ZaC8E',
                  'CAACAgIAAxkBAAEI0BNkUE-uG9mpuyjQ2qYdFNFAWx42-AACgQ4AAoMCOEg0X2Z0GEB17S8E',
                  'CAACAgIAAxkBAAEI0BVkUE-y0bngKWm8gY3yBa3kzu_dYwACRBEAAsB7OUi0vnIZPV6rui8E',
                  'CAACAgIAAxkBAAEI0BdkUE-7mcRrLIHkuKc_uXMM2BedCgACdA8AAn62OUgWFQhZ-cDQzy8E',
                  'CAACAgIAAxkBAAEI0BhkUE-7xxlA0a9H6LHKQOCm9frNYAACwQ4AAmPVQUi5DVQsnCPOVS8E',
                  'CAACAgIAAxkBAAEI0BtkUE_MqdSb5M38UOJzB3rP5FO6sgACPRAAArEWgUvR9G6IFp5ZCS8E',
                  'CAACAgIAAxkBAAEI0B1kUE_XBa3pUyIJkzA4PdqdWk8YRgACsg0AAtsUkUuduj60_xhW_S8E',
                  'CAACAgIAAxkBAAEI0B9kUE_ZjYxkcP_GXmXq4iasnnloiwACUA8AAkAXiUuICnHhVk6z2i8E',
                  'CAACAgIAAxkBAAEI0CFkUE_b124nFvzpNeZES4Y8GwcWeQACxQ4AAoyhkEswSLS5IxcESS8E',
                  'CAACAgIAAxkBAAEI0CNkUFE6mokkvyt-mNbWqOm7HfJVQQACsg4AApPJaUtJBu_UEi9pdy8E',
                  'CAACAgIAAxkBAAEI0CVkUFE_5V2Cwrm5D5gUvgGbmrbmAgACFQ0AAmZCcUuaAkPmtiy58S8E',
                  'CAACAgIAAxkBAAEI0CZkUFE_p9kPwh24nRdphWOwSyGl2gACBg4AAotpeUuOMMG7l90fCS8E',
                  'CAACAgIAAxkBAAEI0ClkUFFwVJKGp7VyrgEdd1zKvHPDxwACVRAAAn0VoEgnkkNfzKVUpi8E',
                  'CAACAgIAAxkBAAEI0CtkUFF4Osdb0rwXPb3bc7Mqbtme8wAC1xQAAlam-UpTw4EqmDwJii8E',
                  'CAACAgIAAxkBAAEI0C9kUFGRuckWtxQeNMm2mTadGKj0uQACwxEAAv_HwUvcSTEVoTEn4i8E',
                  'CAACAgIAAxkBAAEI0DFkUFH_UfvD2S7pV-Bk9ohCPp3KYwACvxEAAmsGcEp8-N3bysml0C8E',
                  'CAACAgIAAxkBAAEI0DNkUFIJd_YHNmbHneFY1TuFPUwTuQACJgwAAgpf6EsiMhlYQyEYhi8E',
                  'CAACAgIAAxkBAAEI0DVkUFIVvFo08wlHnuA5dIDlcIIJIAAC0w8AAk9A0Ei8chYttkuOAS8E',
                  'CAACAgIAAxkBAAEI0DdkUFIss2xpKOj4UxzNxZ3hsvtDnwAC1Q0AAlor8UgWZMHM_rsasy8E',
                  'CAACAgIAAxkBAAEI0DlkUFJclxemCyt2GJ_rZVAeIOfqBQACXxAAAkgq-ElBjCJkISCazi8E',
                  'CAACAgIAAxkBAAEI0DtkUFJ29prQYDFOpPuUJ_D6F9w2rAACHw8AAtVIwUkAAZpG6RhrmisvBA']
# 38 стикеров

yellowboy = ['CAACAgEAAxkBAAEIqbhkQdDjN_NCYgh3dY5onQEF0vERnAACWwEAAnY3dj-FIaR_hp8psi8E',
             'CAACAgEAAxkBAAEIqbpkQdDlOceOZ-4sxvFOg5amsbRl8gACrwEAAnY3dj-O8cvJH85sRC8E',
             'CAACAgEAAxkBAAEIqbxkQdDng1I4wU8SYNIDwZ4Y8vjjPQACbgEAAnEJsEftZZQWTtuY6i8E',
             'CAACAgEAAxkBAAEIqb5kQdDq-OW09vZt39EwMJsNKL2kbQACkQEAAnY3dj8mHoL0iCCHOi8E',
             'CAACAgEAAxkBAAEIqcBkQdDxKwLLeubo95Fm2WQWu1zT0gACFQEAAnY3dj_d8P9Nk2c2JS8E',
             'CAACAgEAAxkBAAEIqcJkQdDzxu2vjr2phbD3XFsLE0HfOQACEQEAAnY3dj8PX08Hh0bD5i8E',
             'CAACAgEAAxkBAAEIqcRkQdD-5nnErMZ8R4Au1R2uzBv9BgACtgEAAnY3dj8Kl238upuOrS8E',
             'CAACAgEAAxkBAAEIqcZkQdEAAUK2cc3SrtFKIAABMBn2ArhWAAK7AQACdjd2PwpL6gUxA5kdLwQ',
             'CAACAgEAAxkBAAEIqchkQdECAwaVRFg4YKcszilqDFxRDgACYgEAAnY3dj-CB0Htfixfri8E',
             'CAACAgEAAxkBAAEIqcpkQdEFg8jmUE4jN4I4UVrQ7ibMDQACpQEAAnY3dj8o0JeVaE-DQS8E',
             'CAACAgEAAxkBAAEIqcxkQdEJBkjgAzzdUJgeUYFmsv3qPAACFwIAApv2qEQGoSfTP9aJVy8E',
             'CAACAgEAAxkBAAEIqc5kQdEMblxJqxgtkVlVJeokhveXMAACbAEAAnY3dj_zMTm53e9VDi8E',
             'CAACAgEAAxkBAAEIqdBkQdESLA0bmz-sX72wqBaSIgqhzQACswEAAnY3dj-H7hK_1dB0LS8E',
             'CAACAgEAAxkBAAEIqdJkQdETdPl5G-pOHJYX4N7eRHSboAACBAIAAp1kmUfrSWgLknQ0oy8E',
             'CAACAgEAAxkBAAEIqdRkQdEkMPY6K0-Ukgv5u1aJJY3lWAACjAEAAnY3dj9voa_1zYo_sy8E',
             'CAACAgEAAxkBAAEIqdZkQdEnESgHxqDVxoPIikkmL6qCVQACsQEAAnY3dj-kdqoozr_pcy8E',
             'CAACAgEAAxkBAAEIqdhkQdEvCIMvhhIRs5XwwV8hBjQZyAACwgEAAnY3dj99-AsPaVYkoC8E',
             'CAACAgEAAxkBAAEIqdpkQdE8LJQvOU9TKHy30eUFPUPNqgACegEAAsCAyUW0C953uDVphi8E',
             'CAACAgEAAxkBAAEIqdxkQdFGqutMNopM4G3mvcfrsdn1BAACjgEAAnEVmEcnXbb0QYHlZC8E',
             'CAACAgEAAxkBAAEIqd5kQdFIHOE4IJMgq_EehEc_BWp_DQACZQEAAnY3dj9hlcwZRAnaOi8E']
# 20 стикеров

bot.polling(none_stop=True)  # запускаем бота
