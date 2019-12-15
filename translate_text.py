"""
Created on Sun Dec 15 12:19:15 2019

@author: Yuliya

SET env variable GOOGLE_APPLICATION_CREDENTIALS = 'Path with an API credentials json file from GCP'

"""

# -*- coding: utf-8 -*-
from google.cloud import translate_v2 as translate

def translate_new(text, target = 'en'):
    
    tr_client = translate.Client()
    translation = tr_client.translate(text, target_language = target)
    
    print(translation['input'], '\n', 
          'Language: ', translation['detectedSourceLanguage'], '\n', 
          'Translation: ', translation['translatedText'], sep = '')
    
text = 'Здравствуйте! Xорошего дня.'

translate_new(text)

'''
OUTPUT:

Здравствуйте! Xорошего дня.
Language: ru
Translation: Hello! Have a nice day.
'''