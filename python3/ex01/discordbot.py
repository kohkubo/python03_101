# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODU1MjY2NzE1NDAzNDE5NjQ4.YMv_Mw.wQ6kq6T4xKiigs37ebk-PDt6_3Y'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == 'Hello':
        await message.channel.send('Hello!')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
