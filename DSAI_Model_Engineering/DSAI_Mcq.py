########################################################

#Copyright (c) DeepSphere.AI 2021

# All rights reserved

# We are sharing this partial code for learning and research, and the idea behind us sharing the source code is to stimulate ideas #and thoughts for the learners to develop their MLOps.

# Author: # DeepSphere.AI | deepsphere.ai | dsschoolofai.com | info@deepsphere.ai

# Release: Initial release

#######################################################


import json
import requests
import string
import re
import heapq
import nltk
import string
import itertools
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt') 
import pke
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import traceback
from flashtext import KeywordProcessor
from sense2vec import Sense2Vec
from collections import OrderedDict
import random
# from transformers import T5ForConditionalGeneration,T5Tokenizer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import streamlit as st
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from similarity.normalized_levenshtein import NormalizedLevenshtein  ##module required is "strsim"


# If we want to perform MCQ - we need below files/libraries
# !pip install --quiet sense2vec==1.0.2
# !wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
# !tar -xvf  s2v_reddit_2015_md.tar.gz

def file_selector_mcq():
    vAR_file = st.file_uploader('Upload the text file',type=['txt'],key='4')
    if vAR_file is not None:
        vAR_text = vAR_file.read().decode("utf-8")
        st.text('File Content: '+ vAR_text)
        return vAR_text
    

def get_context_mcq(quest,unit,grade,title):
    return {
      "unit": unit,
      "grade" : grade,
      "title" : title,
      "type" : "MCQ",
      "quest": quest,
      "length":len(quest),

  }

@st.cache(show_spinner=False)
def summarize_text_mcq(article_text):
    # Removing Square Brackets and Extra Spaces
    vAR_article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    vAR_article_text = re.sub(r'\s+', ' ', vAR_article_text)
    # Removing special characters and digits
    vAR_formatted_article_text = re.sub('[^a-zA-Z]', ' ', vAR_article_text )
    vAR_formatted_article_text = re.sub(r'\s+', ' ', vAR_formatted_article_text)
    # Converting Text To Sentences
    vAR_sentence_list = nltk.sent_tokenize(article_text)
    vAR_stopwords = nltk.corpus.stopwords.words('english')
    # Find Weighted Frequency of Occurrence
    vAR_word_frequencies = {}
    for word in nltk.word_tokenize(vAR_formatted_article_text):
        if word not in vAR_stopwords:
            if word not in vAR_word_frequencies.keys():
                vAR_word_frequencies[word] = 1
            else:
                vAR_word_frequencies[word] += 1
    if len(vAR_word_frequencies) >0:
        maximum_frequncy = max(vAR_word_frequencies.values())
    else:
        maximum_frequncy = 1

    for word in vAR_word_frequencies.keys():
        vAR_word_frequencies[word] = (vAR_word_frequencies[word]/maximum_frequncy)
    # Calculating Sentence Scores
    vAR_sentence_scores = {}
    for sent in vAR_sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in vAR_word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in vAR_sentence_scores.keys():
                        vAR_sentence_scores[sent] = vAR_word_frequencies[word]
                    else:
                        vAR_sentence_scores[sent] += vAR_word_frequencies[word]
    vAR_summary_sentences = heapq.nlargest(10, vAR_sentence_scores, key=vAR_sentence_scores.get)
    vAR_summary = ' '.join(vAR_summary_sentences)
    return vAR_summary

@st.cache(show_spinner=False)
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
  keyphrases = extractor.get_n_best(n=50)
  keyphrases_res = zip(*keyphrases)
  keyphrases = list(list(keyphrases_res)[0])
  return keyphrases


@st.cache(show_spinner=False)
def get_keywords_mcq(text):
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
  keyphrases = extractor.get_n_best(n=50)
  wingnus_res = zip(*keyphrases)
  keyphrases = list(list(wingnus_res)[0])
  sr = set(get_noun_adj_verb_sr(text))
  common = list(sr.intersection(keyphrases))
  z = []
  common.sort()
  print(common)
  for x, y in zip(common, common[1:]):
    print(x,y)
    if fuzz.partial_ratio(x,y)!=100:
        z.append(x)
  z = set(z)
  print('-----------------Keywords from Single Rank in MCQ---------------------\n',sr)
  print('-----------------Keywords from wingnus in MCQ---------------------\n',z)
  print('-----------------Common Keywords from both in MCQ---------------------\n',common)
  return common

#       # define the set of valid Part-of-Speeches
#   pos = {'NOUN', 'PROPN', 'ADJ'}

#   # 1. create a SingleRank extractor.
#   extractor = pke.unsupervised.SingleRank()

#   # 2. load the content of the document.
#   extractor.load_document(input=text,
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
#Extract sentences having the keywords that is extracted before.
@st.cache(show_spinner=False)
def get_sentences_for_keyword(keywords, sentences):
    vAR_keyword_processor = KeywordProcessor()
    vAR_keyword_sentences = {}
    for word in keywords:
        vAR_keyword_sentences[word] = []
        vAR_keyword_processor.add_keyword(word)
    for sentence in sentences:
        vAR_keywords_found = vAR_keyword_processor.extract_keywords(sentence)
        for key in vAR_keywords_found:
            vAR_keyword_sentences[key].append(sentence)

    for key in vAR_keyword_sentences.keys():
        vAR_values = vAR_keyword_sentences[key]
        vAR_values = sorted(vAR_values, key=len, reverse=False)
        vAR_keyword_sentences[key] = vAR_values
    return vAR_keyword_sentences

# @st.cache(allow_output_mutation=True)
def sense2vec_get_words(word,vAR_s2v):
    vAR_output = []
    vAR_word = word.lower()
    vAR_word = vAR_word.replace(" ", "_")

    vAR_sense = vAR_s2v.get_best_sense(vAR_word)
    if vAR_sense:
        vAR_most_similar = vAR_s2v.most_similar(vAR_sense, n=20)
        for each_word in vAR_most_similar:
            vAR_append_word = each_word[0].split("|")[0].replace("_", " ").lower()
            if vAR_append_word.lower() != word.lower():
                vAR_output.append(vAR_append_word.title())

    vAR_out = list(OrderedDict.fromkeys(vAR_output))
    return vAR_out

# @st.cache(show_spinner=False)
def kw_distractors(keyword_list,text):
    vAR_distr = {}
    vAR_s2v = Sense2Vec().from_disk('s2v_old')
    keywords = get_keywords_mcq(text)
    list_len = len(keywords)
    for kw in keyword_list:
        vAR_distractors = sense2vec_get_words(kw,vAR_s2v)
	#####Change of code starts here
        distractors = vAR_distractors
        all_edits = edits (kw.lower())
        filtered_distractors_edit_distance = [x for x in distractors if x.lower() not in all_edits]
        normalized_levenshtein = NormalizedLevenshtein()
        threshold = 0.7
        filtered_distractors_edit_distance_and_levenshtein_distance =[[x for x in filtered_distractors_edit_distance if normalized_levenshtein.distance(x.lower(),kw.lower())>threshold] ]
        vAR_distractors = filtered_distractors_edit_distance
	#####Change of code over
        if len(vAR_distractors)>=3:
#             vAR_distr[kw] = random.sample(vAR_distractors,3)
            vAR_distr[kw] = vAR_distractors[:3]
            vAR_distr[kw].append(kw)
        elif len(vAR_distractors) >= 1 and len(vAR_distractors) < 3:
            vAR_distr[kw] = vAR_distractors
            vAR_distr[kw].append(kw)
        # Assiging random keywords for no distractors
        else:
            print('Random Distractor Calling for Keyword - ',kw)
            keywords = list(get_keywords_mcq(text))
            if len(keywords[list_len:list_len+3])==0:
                list_len = list_len-3
            options = keywords[list_len:list_len+3]
            list_len = list_len-3
            if kw in options:
                options = options.remove(kw)
            print('options for kw - ',kw,' is ',options)
            vAR_distr[kw] = options
            vAR_distr[kw].append(kw)
    return vAR_distr

#Generate a question using context and answer with T5
# @st.cache(show_spinner=False)
def get_question(sentence,answer,vAR_question_model,vAR_question_tokenizer):
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print('train starts - ',current_time)
    # vAR_question_model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_squad_v1')
    # vAR_question_tokenizer = T5Tokenizer.from_pretrained('t5-base')
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print('train ends - ',current_time)
    vAR_text = "context: {} answer: {} </s>".format(sentence,answer)
    vAR_max_len = 256
    vAR_encoding = vAR_question_tokenizer.encode_plus(vAR_text,\
        max_length=vAR_max_len, padding="max_length", return_tensors="pt",\
        return_attention_mask = True, truncation = True)

    vAR_input_ids, vAR_attention_mask = vAR_encoding["input_ids"], vAR_encoding["attention_mask"]

    vAR_outs = vAR_question_model.generate(input_ids=vAR_input_ids,
                                    attention_mask=vAR_attention_mask,
                                    early_stopping=False,
                                    num_beams=5,
                                    num_return_sequences=1,
                                    no_repeat_ngram_size=2,
                                    max_length=200)

    vAR_dec = [vAR_question_tokenizer.decode(ids) for ids in vAR_outs]


    vAR_Question = vAR_dec[0].replace("question:","")
    vAR_Question= vAR_Question.strip()
    vAR_Question = vAR_Question.replace('<pad>','')
    vAR_Question = vAR_Question.replace('</s>','')
    print('vAR_Question in get_question - ',vAR_Question)
    return vAR_Question

# @st.cache(show_spinner=False)
def getMCQ(keyword_sentence_mapping,choices):
    vAR_ques = {}
  
    vAR_question_tokenizer = AutoTokenizer.from_pretrained("ramsrigouthamg/t5_squad_v1")

    vAR_question_model = AutoModelForSeq2SeqLM.from_pretrained("ramsrigouthamg/t5_squad_v1")
  
    # vAR_question_tokenizer = AutoTokenizer.from_pretrained("ramsrigouthamg/t5_squad_v1")

    # vAR_question_model = AutoModelForSeq2SeqLM.from_pretrained("ramsrigouthamg/t5_squad_v1")
    # vAR_question_model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_squad_v1')
    # vAR_question_tokenizer = T5Tokenizer.from_pretrained('t5-base')
    for k,v in keyword_sentence_mapping.items():
        if v:
            vAR_sentence_for_T5 = " ".join(random.sample(v,1)[0].split()) 
            vAR_ques[k.title()] = get_question(vAR_sentence_for_T5,k,vAR_question_model,vAR_question_tokenizer)
    print('Sentence Mapping - ',keyword_sentence_mapping)
    print('Choices - ',choices)
    print('vAR_ques - ',vAR_ques)
    vAR_final_out = {v:choices[k.lower()] for k,v in vAR_ques.items()}
    for k,v in vAR_final_out.items():
        if v:
            v.append("ANSWER: "+v[-1])
        else:
            for kw,que in vAR_ques.items():
                if que == k:
                    v.append("ANSWER: "+kw)
    return vAR_final_out
