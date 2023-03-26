import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
allowed_roles = ['Admin', 'Moderator'] # Роли, которые могут использовать команду
delay_seconds = 5 # Задержка в секундах

@bot.slash_command(description="Удалить сообщения из канала")
@commands.has_any_role(*allowed_roles)
async def clear(ctx, amount: int, member: discord.Member = None):
    channel = ctx.channel
    if member is None:
        deleted = await channel.purge(limit=amount)
        message = f'Удалено {len(deleted)} сообщений в канале {channel.mention}.'
    else:
        def is_member(msg):
            return msg.author == member
        deleted = await channel.purge(limit=amount, check=is_member)
        message = f'Удалено {len(deleted)} сообщений от {member.mention} в канале {channel.mention}.'
    
    embed = discord.Embed(
        title="Очистка сообщений",
        description=message,
        color=discord.Color.dark_red()
    )
    
    await ctx.defer() # Отложить ответ на команду на 5 секунд
    await asyncio.sleep(delay_seconds)
    await ctx.send(embed=embed)

bot.run('ваш токен')
