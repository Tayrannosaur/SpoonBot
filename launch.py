#!/usr/bin/env python3

import logging

import dotenv
import discord

from spoonbot import spoonbot

dotenv.load_dotenv()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='spoonbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

spoonbot.launch()
