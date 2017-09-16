import discord
import asyncio
from discord.ext import commands
import praw
import os.path

class Notifier:
    """CPSC 310 notifier"""

    def __init__(self, bot):
        self.bot = bot
        self.dirpath = '''data/notifier'''
        self.filename = '''data/notifier/blacklist.txt'''
        self.reddit = praw.Reddit(client_id='S8kIhHJtWLI2yA', 
            client_secret='4rlH_-s4XSgtWMxBUk-ueAiOLhw', 
            user_agent='windows:personal-notifier-bot:v0.1 (by /u/lucas_py_bot)')
        self.blacklist = []
        if os.path.isfile(self.filename):
            with open(self.filename) as f:
                self.blacklist = f.readlines()
            self.blacklist = [x.strip() for x in self.blacklist]
        else:
            if os.path.exists(self.dirpath):
                open(self.filename, 'a').close()
            else:
                os.makedirs(self.dirpath)
                open(self.filename, 'a').close()

    @commands.command()
    async def foo(self):
        await notifier_bot.bot.send_message(discord.Object(id='227205391816065024'), 'bar')

    @commands.command()
    async def clear_blacklist(self):
        self.blacklist = []
        open(self.filename, 'w').close()
        await self.bot.say('Done')

    async def check(self):
        keywords = ['cpsc', '310']
        sub = 'ubc'
        while self is self.bot.get_cog('Notifier'):
            try:
                recent = []
                for post in self.reddit.subreddit('ubc').new(limit=25):   
                    title_match = self.has_all_in_title(post, keywords)
                    body_match = self.has_all_in_body(post, keywords)
                    try:
                        comment_match = self.comment_matches_all(post, keywords)
                    except:
                        await asyncio.sleep(2)
                        pass
                    if (title_match or body_match) and (not post.id in self.blacklist):
                        prefix = 'New post about 310: '
                        await notifier_bot.bot.send_message(discord.User(id='129718015003459585'), prefix + post.url)
                        recent.append(post.id)
                    elif (comment_match is not None) and (not post.id in self.blacklist):
                        prefix = 'New comment about 310: '
                        await notifier_bot.bot.send_message(discord.User(id='129718015003459585'), prefix + comment_match)
                        recent.append(post.id)
                self.add_to_blacklist(recent)
                await asyncio.sleep(900)
            except:
                await asyncio.sleep(2)

    def add_to_blacklist(self, recent):
        for item in recent:
            self.blacklist.append(item)
            with open(self.filename, 'a') as f:
                f.write(item + '\n')

    def has_all_in_title(self, post, keyword_arr):
        for word in keyword_arr:
            if word not in post.title.lower():
                return False
        return True

    def has_all_in_body(self, post, keyword_arr):
        if not post.is_self:
            return False
        for word in keyword_arr:
            if word not in post.selftext.lower():
                return False
        return True

    def comment_matches_all(self, post, keyword_arr):
        post.comments.replace_more(limit=0)
        comment_queue = post.comments[:]
        while comment_queue:
            found = True
            comment = comment_queue.pop(0)
            for word in keyword_arr:
                if word not in comment.body.lower():
                    found = False
            if found:
                return comment.submission.url + comment.id
            comment_queue.extend(comment.replies)
        return None

def setup(bot):
    global notifier_bot
    notifier_bot = Notifier(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(notifier_bot.check())
    bot.add_cog(notifier_bot)
