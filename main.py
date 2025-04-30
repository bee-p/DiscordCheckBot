import discord
import datetime
import os

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
CHANNEL_ID = int(os.environ["DISCORD_CHANNEL_ID"])

client = discord.Client(intents=discord.Intents.default())

# 한글 요일
weekdays_ko = ['월', '화', '수', '목', '금']

# 이모지
emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']

@client.event
async def on_ready():
    today = datetime.date.today()
    # 다음 월요일 ~ 금요일
    next_monday = today + datetime.timedelta(days=(7 - today.weekday()))
    dates = [(next_monday + datetime.timedelta(days=i)) for i in range(5)]

    # 메시지 생성
    date_range = f"{dates[0].month}/{dates[0].day} ~ {dates[-1].month}/{dates[-1].day}"
    message = f"**📢 [{date_range}] 코어타임 참석 여부 표시**\n\n"
    for i, d in enumerate(dates):
        date_str = f"{d.month}/{d.day} ({weekdays_ko[d.weekday()]})"
        message += f"{emojis[i]} {date_str}\n\n"
    message += "참석할 수 있는 날짜에 반응을 남겨주세요 :>"

    channel = client.get_channel(CHANNEL_ID)
    sent_message = await channel.send(message)

    for emoji in emojis:
        await sent_message.add_reaction(emoji)

    await client.close()  # 한 번만 실행하고 종료

client.run(TOKEN)