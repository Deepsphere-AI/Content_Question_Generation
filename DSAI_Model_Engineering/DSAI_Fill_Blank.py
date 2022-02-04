########################################################

#Copyright (c) DeepSphere.AI 2021

# All rights reserved

# We are sharing this partial code for learning and research, and the idea behind us sharing the source code is to stimulate ideas #and thoughts for the learners to develop their MLOps.

# Author: # DeepSphere.AI | deepsphere.ai | dsschoolofai.com | info@deepsphere.ai

# Release: Initial release

#######################################################



import streamlit as st
import json
import requests
import string
import re
import nltk
import string
import itertools
import base64
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
import pke
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import traceback
from pprint import pprint
# from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor
from datetime import datetime

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def file_selector_fill():
    vAR_file = st.file_uploader('Upload the text file',type=['txt'],key='2')
    if vAR_file is not None:
        vAR_text = vAR_file.read().decode("utf-8").strip()
        st.write('File Content: '+ vAR_text)
        return vAR_text
    
    
    
def get_context_fill(quest,answers,unit,grade,title):
    return {
      "unit": unit,
      "grade" : grade,
      "title" : title,
      "type" : "FillInTheBlanks",
      "quest": quest,
      "length":len(quest),
      "answers":answers

  }

# keyword extraction using pke's TopicRank Algorithm
# Working principle of MultipartiteRank Algorithm - https://www.aclweb.org/anthology/N18-2105.pdf
@st.cache(show_spinner=False)
# def get_noun_adj_verb(text_content):
#       # define the set of valid Part-of-Speeches
#   pos = {'NOUN', 'PROPN', 'ADJ'}

#   # 1. create a SingleRank extractor.
#   extractor = pke.unsupervised.SingleRank()

#   # 2. load the content of the document.
#   extractor.load_document(input=text_content,
#                           language='en',
#                           normalization=None)

#   # 3. select the longest sequences of nouns and adjectives as candidates.
#   extractor.candidate_selection(pos=pos)

#   # 4. weight the candidates using the sum of their word's scores that are
#   #    computed using random walk. In the graph, nodes are words of
#   #    certain part-of-speech (nouns and adjectives) that are connected if
#   #    they occur in a window of 10 words.
#   extractor.candidate_weighting(window=10,
#                                 pos=pos)

#   # 5. get the 10-highest scored candidates as keyphrases
#   keyphrases = extractor.get_n_best(n=20)
#   keyphrases_res = zip(*keyphrases)
#   keyphrases = list(list(keyphrases_res)[0])
#   #The below block of code written for substring removal of keywords
#   z = []
#   keyphrases.sort()
# #   print(keyphrases)
#   for x, y in zip(keyphrases, keyphrases[1:]):
#     print(x, y)
#     if fuzz.partial_ratio(x,y)!=100:
#       z.append(x)
#   return z
# def get_noun_adj_verb(text):
    # vAR_out=[]
    # try:
    #     # pos = {'NOUN'}
    #     vAR_extractor = pke.unsupervised.TopicRank()
    #     vAR_extractor.load_document(input=text_content)
    #     vAR_pos = {'NOUN', 'PROPN', 'ADJ'}
    #     vAR_stoplist = list(string.punctuation)
    #     vAR_stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
    #     vAR_stoplist += stopwords.words('english')
    #     vAR_extractor.candidate_selection(pos=vAR_pos, stoplist=vAR_stoplist)
    #     vAR_extractor.candidate_weighting(threshold=0.74, method='average')
    #     vAR_keyphrases = vAR_extractor.get_n_best(n=20)
        
    #     for val in vAR_keyphrases:
    #         vAR_out.append(val[0])
    # except BaseException as e:
    #     print(e)
    # z = []
    # vAR_out.sort()
    # #   print(keyphrases)
    # for x, y in zip(vAR_out, vAR_out[1:]):
    #     if fuzz.partial_ratio(x,y)!=100:
    #         z.append(x)
    # return z
def get_noun_adj_verb_sr(text):
  # define the set of valid Part-of-Speeches
  pos = {'NOUN', 'PROPN', 'ADJ'}

  # 1. create a SingleRank extractor.
  extractor = pke.unsupervised.SingleRank()

  # 2. load the content of the document.
  extractor.load_document(input=text,
                          language='en',
                          normalization=None)

  # 3. select the longest sequences of nouns and adjectives as candidates.
  extractor.candidate_selection(pos=pos)

  # 4. weight the candidates using the sum of their word's scores that are
  #    computed using random walk. In the graph, nodes are words of
  #    certain part-of-speech (nouns and adjectives) that are connected if
  #    they occur in a window of 10 words.
  extractor.candidate_weighting(window=10,
                                pos=pos)

  # 5. get the 10-highest scored candidates as keyphrases
  keyphrases = extractor.get_n_best(n=40)
  keyphrases_res = zip(*keyphrases)
  keyphrases = list(list(keyphrases_res)[0])
  z = []
  keyphrases.sort()
  for x, y in zip(keyphrases, keyphrases[1:]):
    if fuzz.partial_ratio(x,y)!=100:
        z.append(x)
  return z
# def get_noun_adj_verb(text_content):
#     out=[]
#     try:
#         pos = {'NOUN'}
#         extractor = pke.unsupervised.TextRank()
#         extractor.load_document(input=text_content,language="en",
#                         normalization='stemming')
#         # pos = {'NOUN','PROPN'}
#         stoplist = list(string.punctuation)
#         stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
#         stoplist += stopwords.words('english')
#         # extractor.candidate_selection(pos=pos, stoplist=stoplist)
#         extractor.candidate_weighting(window=2,
#                               pos=pos,
#                               top_percent=0.33)
#         keyphrases = extractor.get_n_best(n=20)
        
#         for val in keyphrases:
#             out.append(val[0])
#     except BaseException as e:
#         print(e)

#     return out
# def get_noun_adj_verb(text_content):
#     out=[]
#     try:
#         extractor = pke.unsupervised.MultipartiteRank()
#         extractor.load_document(input=text_content,language="en", max_length=10000000,
#                         normalization='stemming')
#         pos = {'NOUN'}
#         stoplist = list(string.punctuation)
#         stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
#         stoplist += stopwords.words('english')
#         extractor.candidate_selection(pos=pos, stoplist=stoplist)
#         extractor.candidate_weighting(alpha=1.1,
#                                       threshold=0.75,
#                                       method='average')
#         keyphrases = extractor.get_n_best(n=20)
        
#         for val in keyphrases:
#             out.append(val[0])
#     except:
#         out = []
#         traceback.print_exc()

#     return out
# def get_noun_adj_verb(text):
    # vAR_out=[]
    # try:
    #     vAR_extractor = pke.unsupervised.YAKE()
    #     vAR_extractor.load_document(input=text)
    #     # pos = {'VERB', 'ADJ', 'NOUN'}
    #     vAR_pos ={'NOUN','VERB', 'ADJ'}
    #     vAR_stoplist = list(string.punctuation)
    #     vAR_stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
    #     vAR_stoplist += stopwords.words('english')
    #     vAR_extractor.candidate_selection(n=2,pos=vAR_pos, stoplist=vAR_stoplist)

    #     vAR_extractor.candidate_weighting(window=3,
    #                                   stoplist=vAR_stoplist,
    #                                   use_stems=False)

    #     vAR_keyphrases = vAR_extractor.get_n_best(n=20)
        

    #     for val in vAR_keyphrases:
    #         vAR_out.append(val[0])
    # except:
    #     vAR_out = []
    #     traceback.print_exc()
    # z = []
    # vAR_out.sort()
    # #   print(keyphrases)
    # for x, y in zip(vAR_out, vAR_out[1:]):
    #     if fuzz.partial_ratio(x,y)!=100:
    #         z.append(x)
    # return z
@st.cache(show_spinner=False)
def get_noun_adj_verb(text):
  # 1. create a WINGNUS extractor.
  extractor = pke.supervised.WINGNUS()

  # 2. load the content of the document.
  extractor.load_document(input=text)

  # 3. select simplex noun phrases as candidates.
  extractor.candidate_selection()

  # 4. classify candidates as keyphrase or not keyphrase.
  df = pke.load_document_frequency_file(input_file='df-semeval2010.tsv.gz')
  model_file = 'WINGNUS-semeval2010.py3.pickle'
  extractor.candidate_weighting( model_file=model_file, df=df)

  # 5. get the 10-highest scored candidates as keyphrases
  keyphrases = extractor.get_n_best(n=40)
  wingnus_res = zip(*keyphrases)
  keyphrases = list(list(wingnus_res)[0])
  z = []
  keyphrases.sort()
  for x, y in zip(keyphrases, keyphrases[1:]):
    if fuzz.partial_ratio(x,y)!=100:
        z.append(x)
  z = set(z)
  sr = set(get_noun_adj_verb_sr(text))
  common = sr.intersection(z)
  print('-----------------Keywords from Single Rank in FIB---------------------\n',sr)
  print('-----------------Keywords from wingnus in FIB---------------------\n',z)
  print('-----------------Common Keywords from both in FIB---------------------\n',common)
  return common

# Identify and matching sentence for each keyword
@st.cache(show_spinner=False)
def get_sentences_for_keyword(vAR_keywords, vAR_sentences):
    vAR_keyword_processor = KeywordProcessor()
    vAR_keyword_sentences = {}
    for word in vAR_keywords:
        vAR_keyword_sentences[word] = []
        vAR_keyword_processor.add_keyword(word)
    for sentence in vAR_sentences:
        if len(sentence)>50 and len(sentence)<150:
            sentence = re.sub(".*:","",sentence)
            sentence = re.sub("\d.","",sentence)
            vAR_keywords_found = vAR_keyword_processor.extract_keywords(sentence)
            for key in vAR_keywords_found:
                vAR_keyword_sentences[key].append(sentence)

    for key in vAR_keyword_sentences.keys():
        vAR_values = vAR_keyword_sentences[key]
        vAR_values = sorted(vAR_values, key=len, reverse=True)
        vAR_keyword_sentences[key] = vAR_values
        print('sentences --------------- ',vAR_keyword_sentences)
    return vAR_keyword_sentences



# Handling case sensitive and removing duplicate keywords
@st.cache(show_spinner=False)
def get_fill_in_the_blanks(vAR_sentence_mapping):
    vAR_out={"title":"Fill in the blanks for these sentences with matching words at the top"}
    vAR_blank_sentences = []
    vAR_processed = []
    vAR_keys=[]
    for key in vAR_sentence_mapping:
        if len(vAR_sentence_mapping[key])>0:
            vAR_sent = vAR_sentence_mapping[key][0]
            # Compile a regular expression pattern into a regular expression object, which can be used for matching and other methods
            vAR_insensitive_sent = re.compile(re.escape(key), re.IGNORECASE)
            vAR_no_of_replacements =  len(re.findall(re.escape(key),vAR_sent,re.IGNORECASE))
            vAR_line = vAR_insensitive_sent.sub(' _________ ', vAR_sent)
            vAR_line = vAR_line.replace('\r\n','')
            if (vAR_sentence_mapping[key][0] not in vAR_processed) and vAR_no_of_replacements<2:
                vAR_blank_sentences.append(vAR_line)
                vAR_processed.append(vAR_sentence_mapping[key][0])
                vAR_keys.append(key)
    vAR_out["sentences"]=vAR_blank_sentences[:20]
    vAR_out["keys"]=vAR_keys[:20]
    return vAR_out