from twitchio.ext import commands
import logging

# Виводимо все в консоль для дебагу
# logging.basicConfig(level=logging.DEBUG)

# Словник для зберігання останніх повідомлень
user_messages = {}

# Функція для перекодування розкладки
def eng_to_ukr_layout(text):
    mapping = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н',
        'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ї',
        'a': 'ф', 's': 'і', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р',
        'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'є',
        'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т',
        'm': 'ь', ',': 'б', '.': 'ю', '/': '.', '`': 'ʼ', '?': ','
    }

    result = ''
    for char in text:
        lower = char.lower()
        if lower in mapping:
            converted = mapping[lower]
            result += converted.upper() if char.isupper() else converted
        else:
            result += char
    return result

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token='oauth:kltnj43vgp37ytd2zibc2hjccv8hz1', prefix="!", initial_channels=["t0temka"])

    @commands.command(name='бля')
    async def fix_command(self, ctx):
        username = ctx.author.name
        if username in user_messages:
            prev_msg = user_messages[username]
            fixed = eng_to_ukr_layout(prev_msg)
            await ctx.send(f"{username}: {fixed}")
            print(f"[FIXED] {username}: {prev_msg} -> {fixed}")
        else:
            await ctx.send(f"{username}, немає попереднього повідомлення для виправлення.")
            print(f"[MISS] Немає збереженого повідомлення для {username}", user_messages)


    async def event_message(self, message):
        print(message.author.name, message.content)
        if message.echo:
            return

        print(f"[DEBUG] {message.author.name}: {message.content}")

        # Спочатку зберігаємо звичайне повідомлення
        if not message.content.startswith('!'):
            user_messages[message.author.name] = message.content
            print(f"[STORE] Збережено: {message.author.name} -> {message.content}")
        else:
            print(f"[SKIP] Команда: {message.content}")

        # Потім передаємо в систему команд
        await bot.handle_commands(message)

bot = Bot()
bot.run()
