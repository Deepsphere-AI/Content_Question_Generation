import streamlit as st
from nltk import tokenize
from nltk.tree import Tree
from nltk.tokenize import sent_tokenize
from allennlp.predictors.predictor import Predictor
import re
import heapq
import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import nltk
from fuzzywuzzy import fuzz
import time, sys
from datetime import timedelta, datetime
nltk.download('punkt')

predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/elmo-constituency-parser-2018.03.14.tar.gz")



def file_selector_tf():
    file = st.file_uploader('Upload the text file',type=['txt'],key='1')
    if file is not None:
        text = file.read().decode("utf-8")
        st.write('File Content: '+ text)
        return text

    

def get_context_tf(quest,unit,grade,title):
    return {
      "unit": unit,
      "grade" : grade,
      "title" : title,
      "type" : "True Or False",
      "quest": quest,
      "length":len(quest),

  }
# Tokenizing sentence using nltk sent_tokenize
#@st.cache
def tokenize_sentences_tf(text):
    sentences = sent_tokenize(text)
    sentences = [sentence.strip() for sentence in sentences if len(sentence) > 20]
    return sentences[0]

# Method returns parts of speech tree for given sentence
#@st.cache(show_spinner=False)
def pos_tree_from_sentence(text):
    sentence = tokenize_sentences_tf(text)
    sentence = sentence.rstrip('?:!.,;')
    parser_output = predictor.predict(sentence=sentence)
    tree_string = parser_output["trees"]
    try:
        tree = Tree.fromstring(tree_string)
    except ValueError as e:
        tree_string +=")"
        tree = Tree.fromstring(tree_string)
    return tree






# split at right most nounphrase or verbphrase
#@st.cache
def get_flattened(t):
    sent_str_final = None
    if t is not None:
        sent_str = [" ".join(x.leaves()) for x in list(t)]
        sent_str_final = [" ".join(sent_str)]
        sent_str_final = sent_str_final[0]
    return sent_str_final

#@st.cache
def get_right_most_VP_or_NP(parse_tree,last_NP = None,last_VP = None):
    if len(parse_tree.leaves()) == 1:
        return last_NP,last_VP
#    st.write(len(parse_tree[-1]))
    last_subtree = parse_tree[-1]
    if last_subtree.label() == "NP":
        last_NP = last_subtree
    elif last_subtree.label() == "VP":
        last_VP = last_subtree
    return get_right_most_VP_or_NP(last_subtree,last_NP,last_VP)

# def get_right_most_VP_or_NP(parse_tree,last_NP = None,last_VP = None):
#     if len(parse_tree.leaves()) == 1:
#         return last_NP,last_VP
#     last_subtree = parse_tree[-1]
#     if last_subtree.label() == "NP":
#         last_NP = last_subtree
#     elif last_subtree.label() == "VP":
#         last_VP = last_subtree
#     return get_right_most_VP_or_NP(last_subtree,last_NP,last_VP)


# sub_string - sipping coffee
# main_string - The old woman was sitting under a tree and sipping coffee
# compare like below
# Theoldwomanwassittingunderatreeandsippingcoffee  || sippingcoffee
# oldwomanwassittingunderatreeandsippingcoffee || sippingcoffee
# womanwassittingunderatreeandsippingcoffee || sippingcoffee
# ...............
# andsippingcoffee || sippingcoffee
# sippingcoffee || sippingcoffee
#@st.cache
def get_termination_portion(main_string, sub_string):
    combined_sub_string = sub_string.replace(" ", "")
    main_string_list = main_string.split()
    last_index = len(main_string_list)
    for i in range(last_index):
        check_string_list = main_string_list[i:]
        check_string = "".join(check_string_list)
        check_string = check_string.replace(" ", "")
        if check_string == combined_sub_string:
            return " ".join(main_string_list[:i])

    return None




#@st.cache(show_spinner=False)
def get_np_vp(tree,sentence):
    print('%%%%%%%%%% - ',sentence)
    last_nounphrase, last_verbphrase =  get_right_most_VP_or_NP(tree)
    last_nounphrase_flattened = get_flattened(last_nounphrase)
    last_verbphrase_flattened = get_flattened(last_verbphrase)
    if last_nounphrase is not None and last_verbphrase is not None:
        longest_phrase_to_use = max(last_nounphrase_flattened, last_verbphrase_flattened)      
    elif last_nounphrase is not None:
        longest_phrase_to_use = last_nounphrase_flattened      
    elif last_verbphrase is not None:
        longest_phrase_to_use = last_verbphrase_flattened
    else:
        print('-----------------Noun phrase & Verb Phrase both are None--------------------')
        print('noun phrase - ',last_nounphrase)
        print('verb phrase- ',last_verbphrase)
    if last_nounphrase is None and last_verbphrase is None:
        return None
    longest_phrase_to_use = re.sub(r"-LRB- ", "(", longest_phrase_to_use)
    longest_phrase_to_use = re.sub(r" -RRB-", ")", longest_phrase_to_use)
    sentence = sentence.rstrip('?:!.,;')
    split_sentence = get_termination_portion(sentence, longest_phrase_to_use)
    return split_sentence


#@st.cache
def summarize_text(article_text):
    # Removing Square Brackets and Extra Spaces
#    vAR_article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
#    vAR_article_text = re.sub(r'\s+', ' ', vAR_article_text)
    vAR_article_text = re.sub("[()]","", article_text)
    vAR_article_text = re.sub(r'\[[0-9]*\]', ' ', vAR_article_text)
    vAR_article_text = re.sub(r'\s+', ' ', vAR_article_text)
    # Removing special characters and digits
#    vAR_formatted_article_text = re.sub('[^a-zA-Z]', ' ', vAR_article_text )
#    vAR_formatted_article_text = re.sub(r'\s+', ' ', vAR_formatted_article_text)
    vAR_formatted_article_text = re.sub('[^a-zA-Z]', ' ', vAR_article_text )
    vAR_formatted_article_text = re.sub(r'\s+', ' ', vAR_formatted_article_text)
    vAR_formatted_article_text = re.sub(' +', ' ', vAR_formatted_article_text)
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
                if len(sent.split(' ')) > 20 and len(sent.split(' ')) < 35:
                    if sent not in vAR_sentence_scores.keys():
                        vAR_sentence_scores[sent] = vAR_word_frequencies[word]
                    else:
                        vAR_sentence_scores[sent] += vAR_word_frequencies[word]
    vAR_summary_sentences = heapq.nlargest(15, vAR_sentence_scores, key=vAR_sentence_scores.get)
    vAR_summary = ' '.join(vAR_summary_sentences)
    return vAR_summary

#@st.cache
def fuzzy_dup_remove(sentences):

    for i,sentence in enumerate(sentences):
        if i<len(sentences)-1:
            score = fuzz.WRatio(sentences[i],sentences[i+1])
            if score > 90:
                sentences.remove(sentences[i+1])
    return sentences



#@st.cache(show_spinner=False)
def alternate_sentences(pos,sentence):
    GPT2tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    GPT2model = TFGPT2LMHeadModel.from_pretrained("gpt2",pad_token_id=GPT2tokenizer.eos_token_id)
#    GPT2tokenizer = GPT2Tokenizer.from_pretrained("distilgpt2")
#    GPT2model = TFGPT2LMHeadModel.from_pretrained("distilgpt2",pad_token_id=GPT2tokenizer.eos_token_id)
    
    s1 = datetime.now()
    
    partial_sentence = get_np_vp(pos,sentence)
    e1 = datetime.now()
    st.write("Time elapsed Sentence Construction is:",e1-s1)
    print('######333',partial_sentence)
    if partial_sentence is not None:
        input_ids = GPT2tokenizer.encode(partial_sentence,return_tensors='tf')
        maximum_length = len(partial_sentence.split())+100
        # Activate top_k sampling and top_p sampling with only from 90% most likely words
        sample_outputs = GPT2model.generate(
            input_ids, 
            do_sample=True, 
            max_length=maximum_length, 
            top_p=1.0, # 0.85 
            top_k=30,   #30
            repetition_penalty  = 10.0,
            num_return_sequences=10)
        generated_sentences=[]
        sentence = sentence.replace("\n","")
        for i, sample_output in enumerate(sample_outputs):
            decoded_sentence = GPT2tokenizer.decode(sample_output, skip_special_tokens=True)
            # final_sentence = decoded_sentence
            final_sentence = tokenize.sent_tokenize(decoded_sentence)[0]
            final_sentence = final_sentence.replace("\r\n","")
            final_sentence = final_sentence.replace("\n","")
            final_sentence = final_sentence.replace("\r","")
            generated_sentences.append(final_sentence)
        generated_sentences.append(sentence)

        if len(generated_sentences)>2:
            return generated_sentences[-2:]

        else:
            return generated_sentences
    else:
        return []

