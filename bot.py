import logging

from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self, irc_token, client_id, nick, prefix, initial_channels, suggestion_service):
        super().__init__(irc_token=irc_token, client_id=client_id, nick=nick, prefix=prefix,
                         initial_channels=[initial_channels])
        self.suggestion_service = suggestion_service

    def run(self):
        logging.info('Bot is running')
        super().run()

    # bot.py, below event_ready
    async def event_message(self, ctx):
        # make sure the bot ignores itself and the streamer
        # if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        #    return
        await self.handle_commands(ctx)

    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send('test passed!')

    @commands.command(name='suggestion')
    async def suggestion(self, ctx):
        command = ctx.message.raw_data.split('!suggestion ')
        if len(command) > 1:
            game_suggestion = command[1]
            author = ctx.message.author.name
            steamer = ctx.channel.name
            self.suggestion_service.addSuggestion(steamer, author, game_suggestion)
            await ctx.send('Merci {0}, ta suggestion de {1} a bien été prise en compte'.format(ctx.message.author.name,
                                                                                               game_suggestion))
        else:
            await ctx.send(
                'Pour faire une suggestion ajouter un jeu après !suggestion (par exemple !suggestion mario) et retrouvez la liste des suggestions sur ce lien https://stream-2549c.web.app/')
