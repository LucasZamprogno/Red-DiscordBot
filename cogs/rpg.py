import discord
from discord.ext import commands
from random import randint
import json
import os #Necessary?

class InputError(Exception):
    def __init__(self, val):
        self.val = val

    def get_val(self):
        return self.val

class RPG:

    def __init__(self, bot, path):
        self.file_path = path
        self.bot = bot

    def _create_profile(self, user):
        pass

    def _has_profile(self, user):
        pass

    #Get account, or create and return if not initialized
    def _get_account(self, user):
        pass

    def _decode_roll(self, code):
        pass

    def _get_dice(self, dice_array):
        dice_as_int = []
        for die in dice_array:
            try:
                dice_as_int.append(int(die))
            except:
                v = InputError(die)
                raise v
                #Check against user saved
                #Recurse through and add
        return dice_as_int

    #Produces dice roll outcome
    #Assumes inputs checked for vailidy
    def _do_roll(self, dice):
        return [randint(1, x) for x in dice]

    #Produces message to return from !roll
    #Assumes inputs checked for validity
    def _roll_result(self, dice):
        results = self._do_roll(dice)
        results_as_string = ', '.join([str(x) for x in results])
        total = str(sum(results))
        message = '%s (%s)' % (total, results_as_string)
        if sum(dice) == sum(results):
            message += ', aced!'
        elif len(dice) == sum(results):
            message += ', botch!'
        return message

    #Core loop of rollto
    #Assumes inputs checked for validity
    def _roll_to_result(self, target, dice):
        count = 0
        total = 0
        while(total < target):
            count += 1
            total += sum(self._do_roll(dice))
        return str(count)       


    @commands.command(pass_context=True)
    async def roll(self, ctx):
        user = ctx.message.author
        user_acct = self._get_account(user)
        split = ctx.message.content.lower().split(' ')[1:]
        if (len(split) == 0):
            await self.bot.send_message(ctx.message.channel, "You'll need to give me some dice to roll")
            return
        try:
            dice = self._get_dice(split)
        except InputError as v:
            error_message = user.mention + ' ' + "Invalid input: " + v.get_val()
            error_message += " If you need to, define a custom dice set with !addroll [name] [dice]"
            await self.bot.send_message(ctx.message.channel, error_message)
            return
        message = user.mention + ' ' + self._roll_result(dice)
        await self.bot.send_message(ctx.message.channel, message)

    @commands.command(pass_context=True)
    async def rollto(self, ctx):
        user = ctx.message.author
        full_text = ctx.message.content.lower()
        split = full_text.split(' ')
        try:
            target = int(split[1])
        except:
            await self.bot.send_message(ctx.message.channel, "Please invoke command in form !rollto [target] [dice]")
            return
        try:
            dice = self._get_dice(split[2:])
        except InputError as v:
            error_message = user.mention + ' ' + "Invalid input: " + v.get_val()
            error_message += " If you need to, define a custom dice set with !addroll [name] [dice]"
            await self.bot.send_message(ctx.message.channel, error_message)
            return
        if (len(dice) == 0):
            await self.bot.send_message(ctx.message.channel, "You'll need to give me some dice to roll")
            return
        message = '%s %s' % (user.mention, self._roll_to_result(target, dice))
        await self.bot.send_message(ctx.message.channel, message)

    @commands.command(pass_context=True)
    async def addroll(self, ctx):
        user = ctx.message.author
        #TODO

def setup(bot):
    global RPG_Bot
    RPG_bot = RPG(bot, "data\rpg\rolls.json")
    bot.add_cog(RPG_bot)
