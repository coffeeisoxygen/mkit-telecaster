import asyncio

import telegram

from app.config import get_settings

settings = get_settings()


async def main():
    bot = telegram.Bot(settings.bot_token)
    async with bot:
        print(await bot.get_me())


if __name__ == "__main__":
    asyncio.run(main())
