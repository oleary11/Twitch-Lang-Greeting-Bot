import irc.bot
import random
import time
import logging

# List of words for "hello, friend" in different languages
hello_friend_words = {
"Afrikaans": "Hallo, vriend",
    "Albanian": "Përshëndetje, mik",
    "Amharic": "Selam, guadenya",
    "Arabic": "Marhaban, sadiq",
    "Armenian": "Barev, ynker",
    "Azerbaijani": "Salam, dost",
    "Basque": "Kaixo, lagun",
    "Belarusian": "Pryvitannie, syabar",
    "Bengali": "Hyalo, bondhu",
    "Bosnian": "Zdravo, prijatelju",
    "Bulgarian": "Zdravey, priyatel",
    "Catalan": "Hola, amic",
    "Cebuano": "Kumusta, amigo",
    "Chinese (Simplified)": "Nihao, pengyou",
    "Chinese (Traditional)": "Nihao, pengyou",
    "Corsican": "Bonghjornu, amicu",
    "Croatian": "Pozdrav, prijatelju",
    "Czech": "Ahoj, příteli",
    "Danish": "Hej, ven",
    "Dutch": "Hallo, vriend",
    "English": "Hello, friend",
    "Esperanto": "Saluton, amiko",
    "Estonian": "Tere, sõber",
    "Filipino": "Kamusta, kaibigan",
    "Finnish": "Hei, ystävä",
    "French": "Bonjour, ami",
    "Frisian": "Hallo, freon",
    "Galician": "Ola, amigo",
    "Georgian": "Gamarjoba, megobaro",
    "German": "Hallo, Freund",
    "Greek": "Geia sou, file",
    "Gujarati": "Hello, mitra",
    "Haitian Creole": "Alo, zanmi",
    "Hausa": "Sannu, aboki",
    "Hawaiian": "Aloha, hoa",
    "Hebrew": "Shalom, chaver",
    "Hindi": "Namaste, dost",
    "Hmong": "Nyob zoo, phooj ywg",
    "Hungarian": "Szia, barátom",
    "Icelandic": "Halló, vinur",
    "Igbo": "Nnọọ, enyi",
    "Indonesian": "Halo, teman",
    "Irish": "Dia dhuit, a chara",
    "Italian": "Ciao, amico",
    "Japanese": "Konnichiwa, tomodachi",
    "Javanese": "Halo, kanca",
    "Kannada": "Hallo, snehitha",
    "Kazakh": "Salem, dosym",
    "Khmer": "Suasdey, mitt",
    "Korean": "Annyeong, chingu",
    "Kurdish": "Silav, heval",
    "Kyrgyz": "Salam, dos",
    "Lao": "Sabaidee, phuen",
    "Latin": "Salve, amice",
    "Latvian": "Sveiki, draugs",
    "Lithuanian": "Sveiki, drauge",
    "Luxembourgish": "Moien, Frënd",
    "Macedonian": "Zdravo, prijatelju",
    "Malagasy": "Salama, namako",
    "Malay": "Hai, kawan",
    "Malayalam": "Halo, suhrith",
    "Maltese": "Bongu, ħabib",
    "Maori": "Kia ora, hoa",
    "Marathi": "Helo, mitra",
    "Mongolian": "Sain baina uu, naiz aa",
    "Myanmar (Burmese)": "Hello, mit",
    "Nepali": "Namaste, saathi",
    "Norwegian": "Hallo, venn",
    "Odia": "Namaskara, bandhu",
    "Pashto": "Salam, malgari",
    "Persian": "Salam, doost",
    "Polish": "Cześć, przyjacielu",
    "Portuguese": "Olá, amigo",
    "Punjabi": "Hallo, dost",
    "Romanian": "Salut, prietene",
    "Russian": "Privet, drug",
    "Samoan": "Talofa, uō",
    "Scots Gaelic": "Halò, charaid",
    "Serbian": "Zdravo, prijatelju",
    "Sesotho": "Lumela, motsoalle",
    "Shona": "Mhoro, shamwari",
    "Sindhi": "Hello, dost",
    "Sinhala": "Hello, mithura",
    "Slovak": "Ahoj, priateľu",
    "Slovenian": "Živjo, prijatelj",
    "Somali": "Salaan, saaxiib",
    "Spanish": "Hola, amigo",
    "Sundanese": "Halo, babaturan",
    "Swahili": "Hujambo, rafiki",
    "Swedish": "Hej, vän",
    "Tajik": "Salom, dust",
    "Tamil": "Vanakkam, nanba",
    "Tatar": "Salem, dus",
    "Telugu": "Hallo, snehituda",
    "Thai": "Sawasdee, puean",
    "Turkish": "Merhaba, arkadaş",
    "Turkmen": "Salam, dostum",
    "Ukrainian": "Pryvit, druže",
    "Urdu": "Hello, dost",
    "Uyghur": "Yaxshimusiz, dost",
    "Uzbek": "Salom, do'st",
    "Vietnamese": "Xin chào, bạn",
    "Welsh": "Helo, ffrind",
    "Xhosa": "Molo, umhlobo",
    "Yiddish": "Hela, freynd",
    "Yoruba": "Pele o, ore",
    "Zulu": "Sawubona, umngane"
}

# Twitch IRC server details
SERVER = "irc.twitch.tv"
PORT = 6667
NICKNAME = ""  # Your bot's Twitch account username
TOKEN = ""  # Your OAuth token
CHANNEL = "#"  # Your Twitch channel name

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, nickname, token, channel):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], nickname, nickname)
        self.channel = channel
        self.index = 0  # To track the current word

    def on_welcome(self, connection, event):
        logging.info("Connected to server, joining channel...")
        connection.join(self.channel)

    def on_join(self, connection, event):
        if irc.client.NickMask(event.source).nick == NICKNAME:
            logging.info(f"Bot has joined {self.channel}")
            while True:
                if self.index >= len(hello_friend_words):
                    self.index = 0  # Reset to the start of the list if we finish it

                # Get the language and greeting
                language, greeting = list(hello_friend_words.items())[self.index]
                message = f"{language}: {greeting}"

                # Send the message to the channel
                connection.privmsg(self.channel, message)
                logging.info(f"Sent message: {message}")

                # Move to the next word
                self.index += 1
                time.sleep(1)  # Wait 10 seconds between each message

    def on_disconnect(self, connection, event):
        logging.warning("Disconnected from server. Attempting to reconnect...")
        time.sleep(1)
        try:
            connection.reconnect()
        except Exception as e:
            logging.error(f"Failed to reconnect: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting Twitch Bot...")
    bot = TwitchBot(SERVER, PORT, NICKNAME, TOKEN, CHANNEL)
    bot.start()