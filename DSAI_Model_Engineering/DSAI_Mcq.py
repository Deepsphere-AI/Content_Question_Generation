import json
import requests
import string
import re
import nltk
import string
import itertools
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt') 
# import pke
import yake
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import traceback
from flashtext import KeywordProcessor
from sense2vec import Sense2Vec
from collections import OrderedDict
import random
from transformers import T5ForConditionalGeneration,T5Tokenizer
import streamlit as st
from similarity.normalized_levenshtein import NormalizedLevenshtein



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

# @st.cache(show_spinner=False)
def get_keywords(text):
    vAR_out=[]
    try:
        
        
        kw_yake = yake.KeywordExtractor(top=10,lan="en", n=3, dedupLim=0.3)
        keywords_yake = kw_yake.extract_keywords(text)
        for val in keywords_yake:
            vAR_out.append(val[0])
            
        
    except:
        vAR_out = []
        traceback.print_exc()
    

    return vAR_out

#Extract sentences having the keywords that is extracted before.
# @st.cache(show_spinner=False)
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
def sense2vec_get_words(word):
    vAR_s2v = Sense2Vec().from_disk('s2v_old')
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

import string
# A function to get all the edits for a word
def edits(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz '+string.punctuation
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)




# @st.cache(show_spinner=False)
def kw_distractors(keyword_list):
    vAR_distr = {}
    for kw in keyword_list:
        vAR_distractors = sense2vec_get_words(kw)
        distractors = vAR_distractors
        all_edits = edits (kw.lower())
        filtered_distractors_edit_distance = [x for x in distractors if x.lower() not in all_edits]
        normalized_levenshtein = NormalizedLevenshtein()
        threshold = 0.85 ##HyperParameter
        filtered_distractors_edit_distance_and_levenshtein_distance =[x for x in filtered_distractors_edit_distance if normalized_levenshtein.distance(x.lower(),kw.lower())>threshold] 
        filtered_distractors_edit_distance_and_levenshtein_distance
        if len(filtered_distractors_edit_distance_and_levenshtein_distance)>=3:
#             vAR_distr[kw] = random.sample(vAR_distractors,3)
            vAR_distr[kw] = filtered_distractors_edit_distance_and_levenshtein_distance[:3]
            vAR_distr[kw].append(kw)
        elif len(filtered_distractors_edit_distance_and_levenshtein_distance) >= 1 and len(filtered_distractors_edit_distance_and_levenshtein_distance) < 3:
            vAR_distr[kw] = filtered_distractors_edit_distance_and_levenshtein_distance
            vAR_distr[kw].append(kw)
        # else:
        #     vAR_distr[kw] = random.sample(distractors,3)
    return vAR_distr

#Generate a question using context and answer with T5
def get_question(sentence,answer):
    vAR_question_model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_squad_v1')
    vAR_question_tokenizer = T5Tokenizer.from_pretrained('t5-base')
    vAR_text = "context: {} answer: {} </s>".format(sentence,answer)
    vAR_max_len = 256
    vAR_encoding = vAR_question_tokenizer.encode_plus(vAR_text,max_length=vAR_max_len, pad_to_max_length=True, return_tensors="pt")

    vAR_input_ids, vAR_attention_mask = vAR_encoding["input_ids"], vAR_encoding["attention_mask"]

    vAR_outs = vAR_question_model.generate(input_ids=vAR_input_ids,
                                    attention_mask=vAR_attention_mask,
                                    early_stopping=True,
                                    num_beams=5,
                                    num_return_sequences=1,
                                    no_repeat_ngram_size=2,
                                    max_length=200)

    vAR_dec = [vAR_question_tokenizer.decode(ids) for ids in vAR_outs]


    vAR_Question = vAR_dec[0].replace("question:","")
    vAR_Question= vAR_Question.strip()
    return vAR_Question

# @st.cache(show_spinner=False)
def getMCQ(keyword_sentence_mapping,choices):
    vAR_ques = {}
    for k,v in keyword_sentence_mapping.items():
        if len(v)>=2:

            vAR_sentence_for_T5 = " ".join(random.sample(v,2)[0].split()) 
            vAR_ques[k] = get_question(vAR_sentence_for_T5,k)
            vAR_final_out = {v:choices[k] for k,v in vAR_ques.items() if k in choices}
    return vAR_final_out
