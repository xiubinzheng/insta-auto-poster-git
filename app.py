from instabot import Bot
from os.path import exists
from datetime import datetime
import os
import time
import random


os.system("rm -rf config")

bot = Bot()
bot.login(username="", password="")

dir_image = "img/"


my_hashtags = """

"""

my_caption = ""
for content_file in os.listdir(dir_image):
    if content_file.endswith("jpg"):
        
        caption_file = content_file[:-4] + ".txt"
        if exists(dir_image + caption_file):
            print("Start Time =", datetime.now())
            random_seconds = random.randint(560, 999)
            time.sleep(random_seconds)
            with open(dir_image + caption_file) as f:
                lines = f.readlines()
                buffer_lines = []
                for line in lines:
                    # print("LINE")
                    # print(line)
                    new_line = line.replace("", "")
                    new_line = new_line.replace("", "")
                    new_line = new_line.replace("", "")
                    buffer_lines.append(new_line)
            buffer_lines.pop()
            buffer_lines.append(my_hashtags)
            my_caption = "".join(buffer_lines)
            bot.upload_photo(dir_image + content_file, caption=my_caption)
            print(dir_image + content_file, " was uploaded.")
            print("End Time =", datetime.now())


'''

'''