import discord
from discord.ext import commands

class Fila(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fila = []

    @commands.command(name="entrar")
    async def entrar(self, ctx):
        user = ctx.author

        if user.id in self.fila:
            return await ctx.send(f"{user.mention}, você já está na fila!")

        self.fila.append(user.id)
        await ctx.send(f"{user.mention} entrou na fila! ({len(self.fila)}/4)")

        # Auto-completar time
        if len(self.fila) == 4:
            membros = [ctx.guild.get_member(i).mention for i in self.fila]
            embed = discord.Embed(
                title="Time Fechado!",
                description="\n".join(membros),
                color=0x00ff00
            )
            await ctx.send(embed=embed)
            self.fila = []

    @commands.command(name="sair")
    async def sair(self, ctx):
        user = ctx.author

        if user.id not in self.fila:
            return await ctx.send("Você não está na fila.")

        self.fila.remove(user.id)
        await ctx.send(f"{user.mention} saiu da fila. ({len(self.fila)}/4)")

    @commands.command(name="fila")
    async def fila(self, ctx):
        if not self.fila:
            return await ctx.send("A fila está vazia.")

        membros = [ctx.guild.get_member(i).mention for i in self.fila]
        await ctx.send("Jogadores na fila:\n" + "\n".join(membros))


async def setup(bot):
    await bot.add_cog(Fila(bot))
