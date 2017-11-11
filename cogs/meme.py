import discord
from discord.ext import commands
from random import randint, choice
import re
import time

class Meme:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.last_author = None
        self.ayy_pattern = re.compile(r'^ay{2,}$')
        self.hmm_pattern = re.compile(r'^hm{2,}$')
        self.anyway_pattern = re.compile(r'^anyway(s)?(\.\.\.)?$')
        self.mad_pattern = re.compile(r'.*(fuck (you|off)|stfu|shut (the fuck up|up)|go (away|fuck yourself)|gtfo|you suck|(suck|eat) a dick).*')
        self.how_pattern = re.compile(r'.*how [a-z]+ (is|are|was|do you) .*')
        self.thinking = '''
```⠀⠰⡿⠿⠛⠛⠻⠿⣷
⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀
⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷
⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁
⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀
⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗
⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄
⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁
⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟
⠀⠀⠀⠀⠀⠉⠉⠉```
'''

    @commands.command()
    async def memes(self):
        await self.bot.say('''Available !memes: shrug, disgusting, dab, clg, na, g2, eu, dank, dreams, yes, faith, kate, tite, support.''')

    @commands.command()
    async def shrug(self):
        await self.bot.say('''¯\_(ツ)_/¯''')

    @commands.command()
    async def disgusting(self):
        await self.bot.say("https://i.imgur.com/1N0UjV3.jpg")

    @commands.command()
    async def dab(self):
        await self.bot.say("https://gfycat.com/TotalBleakBarasinga")
        
    @commands.command()
    async def clg(self):
        await self.bot.say("https://gfycat.com/RewardingConsiderateGraywolf")
        
    @commands.command()
    async def na(self):
        await self.bot.say("https://gfycat.com/ThoughtfulPhonyGlassfrog")

    @commands.command()
    async def g2(self):
        await self.bot.say("https://i.imgur.com/DoGP7yp.png")

    @commands.command()
    async def eu(self):
        await self.bot.say("https://i.imgur.com/WfApIm2.gifv")

    @commands.command()
    async def dank(self):
        await self.bot.say("https://gfycat.com/FrankSpectacularDuck")
        
    @commands.command()
    async def dreams(self):
        await self.bot.say("https://i.imgur.com/UuUWWzn.jpg")

    @commands.command()
    async def kate(self):
        await self.bot.say("http://www.theonion.com/article/beautiful-cinnamon-roll-too-good-for-this-world-to-35038")

    @commands.command()
    async def kate(self):
        await self.bot.say("http://www.theonion.com/article/beautiful-cinnamon-roll-too-good-for-this-world-to-35038")

    @commands.command()
    async def tite(self):
        await self.bot.say("http://i.imgur.com/MQNWHJG.jpg")

    @commands.command()
    async def support(self):
        await self.bot.say("https://i.imgur.com/Nes1bsP.gif")

    @commands.command()
    async def faith(self):
        await self.bot.say("https://i.imgur.com/yEHTzpv.jpg")

    @commands.command()
    async def yes(self):
        await self.bot.say("https://i.imgur.com/mY0l6vy.jpg")      

    @commands.command()
    async def sin(self):
        await self.bot.say("http://i.imgur.com/irNt02G.png")

    @commands.command()
    async def hmm(self):
        await self.bot.say(self.thinking)

    @commands.command()
    async def o_o(self):
        await self.bot.say("https://i.imgur.com/ZkHGWn3.jpg")

    @commands.command()
    async def todd(self):
        await self.bot.say("https://i.imgur.com/4c5j7mt.png")

    @commands.command()
    async def korea(self):
        await self.bot.say("https://streamable.com/sla9c")
    

async def check_messages(message):
    current_author = message.author.id
    prev_author = meme_bot.last_author
    meme_bot.last_author = current_author
    
    if current_author != meme_bot.bot.user.id:
        content = message.content.lower()
        if meme_bot.ayy_pattern.fullmatch(content) is not None:
            await meme_bot.bot.send_message(message.channel, "lmao")
            return
        if meme_bot.hmm_pattern.fullmatch(content) is not None:
            await meme_bot.bot.add_reaction(message, '\U0001F914')
            return
        if meme_bot.anyway_pattern.fullmatch(content) is not None:
            await meme_bot.bot.send_message(message.channel, "Here's Wonderwall\nhttps://www.youtube.com/watch?v=6hzrDeceEKc")
            return
        if (prev_author == meme_bot.bot.user.id) or ("chloe" in content):   
            if meme_bot.mad_pattern.search(content) is not None:
                await meme_bot.bot.send_message(message.channel, "http://i.imgur.com/wCXMzHP.gif")
                return
            if "thanks" in content or "thank you" in content:
                await meme_bot.bot.send_message(message.channel, "np")
                return
            if (meme_bot.how_pattern.search(content) is not None) and ("chloe" in content):
                word_list = content.split(" ")
                word = word_list[word_list.index("how") + 1]
                await meme_bot.bot.send_message(message.channel, "Hella " + word)
        if "aphro" in content:
            await meme_bot.bot.send_message(message.channel, "https://gfycat.com/BasicNarrowBlackcrappie")
            return
        if "stixxay" in content:
            await meme_bot.bot.send_message(message.channel, "https://gfycat.com/TotalValuableBumblebee")
            return
        if "darshan" in content:
            await meme_bot.bot.send_message(message.channel, "https://gfycat.com/ImmaculateAlarmingFlamingo")
            return
        if "zikz" in content:
            await meme_bot.bot.send_message(message.channel, "https://68.media.tumblr.com/2b3659b30ecff875bd3d73bdb38c11f5/tumblr_os83nwSpL11w06raco5_500.gif")
            return
        if ("daguerreotype" in content) or ("louis daguerre" in content):
            await meme_bot.bot.send_message(message.channel, "https://i.imgur.com/Ic0nezw.gif")
            return
        if (content == "tight") or (content == "crisp"):
            await meme_bot.bot.send_message(message.channel, ":ok_hand:")
            return
        if (content == "clg") or (content == "clg!"):
            await meme_bot.bot.send_message(message.channel, choice(["CLG", "#CLGWIN"]))
            return
        if "pathetic" in content:
            await meme_bot.bot.send_message(message.channel, "https://i.imgur.com/YvrTSQq.jpg")
            return
        if "hanzo" in content:
            await meme_bot.bot.send_message(message.channel, "Hanzo? https://i.imgur.com/YvrTSQq.jpg")
            return
        if "genji" in content:
            if randint(1,2) == 1:
                await meme_bot.bot.send_message(message.channel, '''"I need healing!" - Genji''')
            else:
                await meme_bot.bot.send_message(message.channel, '''"Yosh" - Genji''')
            return
        if "amberprice" in content:
            await meme_bot.bot.send_message(message.channel, "Pricefield > Amberprice")
            return
        if "my man" in content:
            await meme_bot.bot.send_message(message.channel, "https://i.imgur.com/0XZ93Zx.jpg")
            return
        if (content == "thinking") or (meme_bot.ayy_pattern.fullmatch(content)) is not None:
            await meme_bot.bot.add_reaction(message, '\U0001F914')
            return
        if "pricefield" in content:
            await meme_bot.bot.add_reaction(message, '\U00002764')
            return
        if "dank" in content:
            await meme_bot.bot.add_reaction(message, '\U0001F44C')
            return
        if "spicy" in content:
            await meme_bot.bot.add_reaction(message, '\U0001F525')
            return
        '''if ("christmas" in content) or ("xmas" in content):
            await meme_bot.bot.add_reaction(message, '\U0001F384')
            return'''
        if "vegan" in content:
            await meme_bot.bot.add_reaction(message, '\U0001F951')
            return
        if " xd" in content or content == "xd":
            await meme_bot.bot.add_reaction(message, '\U0001F1FD')
            await meme_bot.bot.add_reaction(message, '\U0001F1E9')
            return
        for x in ['would', 'could', 'should', 'must']:
            if (x + " of ") in content:
                await meme_bot.bot.send_message(message.channel, x + " have*")
                return

def setup(bot):
    global meme_bot
    meme_bot = Meme(bot)
    bot.add_listener(check_messages, "on_message")
    bot.add_cog(meme_bot)
