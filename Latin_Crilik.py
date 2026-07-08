# -*- coding: utf-8 -*-
"""
latin_krill_bot.py
Lotin alifbosidagi o'zbekcha matnni kirill alifbosiga o'giruvchi Telegram bot.

Ishlatishdan oldin:
1) Pydroid3'da terminal orqali kutubxonani o'rnating:
   pip install pyTelegramBotAPI

2) Quyidagi BOT_TOKEN o'rniga @BotFather'dan olgan haqiqiy tokeningizni yozing.
"""

# ==========================================================
# 1) BOT TOKEN
#    (telebot kutubxonasi faqat botni ishga tushirganda kerak,
#    shuning uchun import pastda, __main__ ichida qilinadi)
# ==========================================================
BOT_TOKEN = "BU_YERGA_TOKENINGIZNI_YOZING"

# ==========================================================
# 2) LOTIN -> KIRILL LUG'ATI
#    Uzun birikmalar (sh, ch, oʻ, gʻ, yo, yu, ya) avval tekshiriladi
# ==========================================================
LATIN_TO_CYRILLIC = {
    # ko'p harfli birikmalar (katta harf bilan)
    "Sh": "Ш", "Ch": "Ч",
    "Yo": "Ё", "Yu": "Ю", "Ya": "Я",
    "Oʻ": "Ў", "O'": "Ў", "Oʼ": "Ў",
    "Gʻ": "Ғ", "G'": "Ғ", "Gʼ": "Ғ",

    # ko'p harfli birikmalar (kichik harf bilan)
    "sh": "ш", "ch": "ч",
    "yo": "ё", "yu": "ю", "ya": "я",
    "oʻ": "ў", "o'": "ў", "oʼ": "ў",
    "gʻ": "ғ", "g'": "ғ", "gʼ": "ғ",

    # bitta harflar (katta)
    "A": "А", "B": "Б", "D": "Д", "E": "Е", "F": "Ф",
    "G": "Г", "H": "Ҳ", "I": "И", "J": "Ж", "K": "К",
    "L": "Л", "M": "М", "N": "Н", "O": "О", "P": "П",
    "Q": "Қ", "R": "Р", "S": "С", "T": "Т", "U": "У",
    "V": "В", "X": "Х", "Y": "Й", "Z": "З",

    # bitta harflar (kichik)
    "a": "а", "b": "б", "d": "д", "e": "е", "f": "ф",
    "g": "г", "h": "ҳ", "i": "и", "j": "ж", "k": "к",
    "l": "л", "m": "м", "n": "н", "o": "о", "p": "п",
    "q": "қ", "r": "р", "s": "с", "t": "т", "u": "у",
    "v": "в", "x": "х", "y": "й", "z": "з",

    # tutuq belgisi
    "ʼ": "ъ", "'": "ъ",
}

# Kalitlarni uzunligi bo'yicha kamayish tartibida saralaymiz
# (masalan "sh" "s" dan oldin tekshirilishi kerak)
SORTED_KEYS = sorted(LATIN_TO_CYRILLIC.keys(), key=len, reverse=True)


def transliterate(text: str) -> str:
    """Lotin matnini kirillga o'giradi."""
    result = []
    i = 0
    n = len(text)
    while i < n:
        matched = False
        for key in SORTED_KEYS:
            klen = len(key)
            if text[i:i + klen] == key:
                result.append(LATIN_TO_CYRILLIC[key])
                i += klen
                matched = True
                break
        if not matched:
            result.append(text[i])
            i += 1
    return "".join(result)


# ==========================================================
# 2.1) KIRILL -> LOTIN LUG'ATI (yuqoridagi lug'atning teskarisi)
#      Bir nechta lotin varianti bitta kirill harfga mos kelgani uchun
#      (masalan "o'" va "oʻ" ikkalasi ham "ў"), teskari lug'at uchun
#      har bir kirill harfga eng qulay (standart) lotin variantini tanlaymiz.
# ==========================================================
CYRILLIC_TO_LATIN = {
    "Ш": "Sh", "Ч": "Ch",
    "Ё": "Yo", "Ю": "Yu", "Я": "Ya",
    "Ў": "Oʻ", "Ғ": "Gʻ",

    "ш": "sh", "ч": "ch",
    "ё": "yo", "ю": "yu", "я": "ya",
    "ў": "oʻ", "ғ": "gʻ",

    "А": "A", "Б": "B", "Д": "D", "Е": "E", "Ф": "F",
    "Г": "G", "Ҳ": "H", "И": "I", "Ж": "J", "К": "K",
    "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P",
    "Қ": "Q", "Р": "R", "С": "S", "Т": "T", "У": "U",
    "В": "V", "Х": "X", "Й": "Y", "З": "Z",

    "а": "a", "б": "b", "д": "d", "е": "e", "ф": "f",
    "г": "g", "ҳ": "h", "и": "i", "ж": "j", "к": "k",
    "л": "l", "м": "m", "н": "n", "о": "o", "п": "p",
    "қ": "q", "р": "r", "с": "s", "т": "t", "у": "u",
    "в": "v", "х": "x", "й": "y", "з": "z",

    "ъ": "ʼ",
}

CYRILLIC_SORTED_KEYS = sorted(CYRILLIC_TO_LATIN.keys(), key=len, reverse=True)


def to_latin(text: str) -> str:
    """Kirill matnini lotinga o'giradi."""
    result = []
    i = 0
    n = len(text)
    while i < n:
        matched = False
        for key in CYRILLIC_SORTED_KEYS:
            klen = len(key)
            if text[i:i + klen] == key:
                result.append(CYRILLIC_TO_LATIN[key])
                i += klen
                matched = True
                break
        if not matched:
            result.append(text[i])
            i += 1
    return "".join(result)


def to_cyrillic(text: str) -> str:
    """Lotin matnini kirillga o'giradi (transliterate bilan bir xil)."""
    return transliterate(text)


def is_cyrillic(text: str) -> bool:
    """Matnda kirill harflari bor-yo'qligini tekshiradi."""
    return any(ch in CYRILLIC_TO_LATIN for ch in text)


def auto_convert(text: str) -> str:
    """Matn kirill bo'lsa lotinga, aks holda (lotin/boshqa) kirillga o'giradi."""
    if is_cyrillic(text):
        return to_latin(text)
    return to_cyrillic(text)


# ==========================================================
# 3) TELEGRAM BOTNI ISHGA TUSHIRISH
#    (bu funksiya faqat shu faylni to'g'ridan-to'g'ri ishga
#    tushirganingizda chaqiriladi, oddiy import qilganda
#    telebot kutubxonasi kerak bo'lmaydi)
# ==========================================================
def run_bot():
    import telebot

    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=["start"])
    def handle_start(message):
        bot.reply_to(
            message,
            "Assalomu alaykum!\n"
            "Menga matn yuboring — lotin bo'lsa kirillga, kirill bo'lsa lotinga o'girib beraman.\n\n"
            "Masalan: \"Salom, o'zbek tili go'zal til\""
        )

    @bot.message_handler(commands=["help"])
    def handle_help(message):
        bot.reply_to(
            message,
            "Shunchaki matn yozing va yuboring — "
            "men uni avtomatik ravishda kirill/lotinga o'giraman."
        )

    @bot.message_handler(func=lambda m: True, content_types=["text"])
    def handle_text(message):
        try:
            converted = auto_convert(message.text)
            bot.reply_to(message, converted)
        except Exception as e:
            bot.reply_to(message, f"Xatolik yuz berdi: {e}")

    print("Bot ishga tushdi...")
    bot.infinity_polling()


if __name__ == "__main__":
    run_bot()
