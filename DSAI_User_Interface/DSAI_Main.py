########################################################

#Copyright (c) DeepSphere.AI 2021

# All rights reserved

# We are sharing this partial code for learning and research, and the idea behind us sharing the source code is to stimulate ideas #and thoughts for the learners to develop their MLOps.

# Author: # DeepSphere.AI | deepsphere.ai | dsschoolofai.com | info@deepsphere.ai

# Release: Initial release

#######################################################


from re import sub
import streamlit as st
import traceback
from PIL import Image
# Utils Pkgs
import textwrap
import pandas as pd
import base64
import numpy as np
from datetime import datetime
from nltk.tokenize import sent_tokenize
import spacy
from tabulate import tabulate
# from streamlit import caching
# import SessionState
# import pyautogui
import random
from docxtpl import DocxTemplate
from home import mainfn
import pickle as pkle
import os.path
import string
import random


spacy.load("en_core_web_sm")

from fill_blank import get_noun_adj_verb,get_sentences_for_keyword,get_fill_in_the_blanks,file_selector_fill,get_context_fill
from matchthefollowing import  get_context_mtf,write_table,sentence_answers,quest_ans,get_keywords_mtf,get_sentences_for_keyword,question,file_selector_match
from mcq import summarize_text_mcq,get_keywords_mcq, get_sentences_for_keyword, kw_distractors, getMCQ,file_selector_mcq,get_context_mcq
from true_false import pos_tree_from_sentence,get_np_vp,alternate_sentences,summarize_text,fuzzy_dup_remove,get_context_tf


# from word_sim import remove_stopwords,sent_tokenize, remove_special_Charac, Train_Model, Model_Outcome

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def file_selector():
    file = st.file_uploader('Upload the text file',type=['txt'])
    if file is not None:
        text = file.read().decode("utf-8")
        st.write('File Content: '+ text)
        return text

def dtime():
      return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    
# Tokenizing sentence using nltk sent_tokenize
@st.cache(show_spinner=False)
def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    sentences = [sentence.strip() for sentence in sentences if len(sentence) > 20]
    return sentences    
    
def output_file(out, quest_type):
      with open("output.txt","a",encoding="utf-8") as f:
        if quest_type == "Input Text":
              f.write("="*100+"\n")
        else:
              f.write("-"*100+"\n")
        dt = dtime()
        f.write(f"{dt} {quest_type}:\n")
        f.write("-"*100+"\n\n")
        if quest_type == "Match the Following":
            
            f.write(tabulate(out,showindex=False, headers=out.columns, tablefmt="grid"))
            # out.to_string(f,index = False)
            f.write("\n")
        elif quest_type == "Input Text":
            f.write(f"{out}")
            f.write("\n")
        elif quest_type == "Fill in The Blanks":
            for i,sent in enumerate(out["sentences"]):
                f.write(f"{str(i+1)}. {sent}\n")
            f.write("\n"+str(out["keys"])+"\n")
        elif quest_type == "MCQ":
            count = 1
            for quest,options in out.items():
                asci = 97
                f.write(f"{str(count)}. {quest}")
                if options:
                    for opt in options:
                        f.write(chr(asci)+")"+" "+opt.title()+"\r\n")
                        asci += 1
                    f.write("\r\n")
                count += 1
        else:
            for i,que in enumerate(out):
                f.write(f"{str(i+1)}. {que}\r\n")
        f.write("\r\n")
        
             
def download_link(object_to_download, download_filename, download_link_text,quest_type):
    """
    Generates a link to download the given object_to_download.
    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.
    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!','required_question_type')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!','required_question_type')
    """
#     if isinstance(object_to_download,pd.DataFrame):
#         object_to_download = object_to_download.to_csv(index=False)
#     object_to_download = str(object_to_download)
    object_to_download1 = ""
    if quest_type == "Input Text":
        object_to_download1 = "="*100+"\r\n"
    else:
        object_to_download1 = "-"*100+"\r\n"
    dt = dtime()
    object_to_download1+=f"{dt} {quest_type}:\r\n"
    object_to_download1+="-"*100+"\r\n\r\n"
    if quest_type == "Match the Following":
        # object_to_download1+=f"{str(object_to_download)}\r\n"
        print('$$$$$$$$$$$$$$$$$$$$$$',quest_type)
        print('-'*100)
        print(type(object_to_download))
        print('-'*100)
        # object_to_download1+=object_to_download.to_markdown()
        # object_to_download1 += tabulate(object_to_download.values.tolist(), list(object_to_download.columns), tablefmt="grid")
        object_to_download1+=tabulate(object_to_download,showindex=False,headers=object_to_download.columns,tablefmt="grid")
    elif quest_type == "Input Text":
            object_to_download1+=f"{object_to_download}"
    elif quest_type == "Fill in The Blanks":
        for i,sent in enumerate(object_to_download["sentences"]):
            object_to_download1+=f"{str(i+1)}. {sent}\r\n"
        object_to_download1+="\n"+str(object_to_download["keys"])+"\r\n"
    elif quest_type == "Content Generation":
        object_to_download1 = object_to_download
    elif quest_type == "MCQ":
        count = 1
        for quest,options in object_to_download.items():
            asci = 97
            object_to_download1+=f"{str(count)}. {quest}\n"
            if options:
                for opt in options:
                    object_to_download1+=chr(asci)+")"+" "+opt.title()+"\n"
                    asci += 1
                object_to_download1+=f"\r\n"
            count += 1
    else:
        for i,que in enumerate(object_to_download):
            object_to_download1+=f"{str(i+1)}. {que}\r\n"
    object_to_download1+=f"\r\n"
    b64 = base64.b64encode(object_to_download1.encode()).decode()
    
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'
    # return f'<a href="data:file/Microsoft Word;base64,{b64}" download="{download_filename}">{download_link_text}</a>'
    
def match_the_foll():
    option = st.selectbox('',['Select Text Input or File Upload','Text Input','File Upload'])
    text = None
    if option=='Text Input':
        text = st.text_area('Enter your text here')
    elif option=='File Upload':
        text = file_selector_fill()
    if text is not None and len(text)>=20:
        unit = st.text_input("Enter unit")
        grade = st.text_input("Enter grade")
        title = st.text_input("Enter title")
        quest = "Match the Following"
        ts_col1,ts_col2,ts_col3 = st.beta_columns((1,1,2))
        ts_col1.success("Run Model")
        ts_col2.success("Step 1")
        if ts_col3.button('Tokenize sentences'):
            if text is not None:
                with st.spinner("Processing input to tokenize sentence"):
                    sentences = tokenize_sentences(text)
                    st.write(sentences)
                st.success('Tokenizing completed ')
            else:
                st.error("Please select input file!")
        ek_col1,ek_col2,ek_col3 = st.beta_columns((1,1,2))
        ek_col1.success("Run Model")
        ek_col2.success("Step 2")
        if ek_col3.button('Extract Keywords'):
            if text is not None:
                with st.spinner("Processing input to extract keywords"):
                    keywords = list(get_keywords_mtf(text))[:6]
                    print('$$$$$$$$$ - ',keywords)
                    st.write(keywords)
                st.success('Keywords Extracted')
            else:
                st.error("Please select input file!")
        km_col1,km_col2,km_col3 = st.beta_columns((1,1,2))
        km_col1.success("Run Model")
        km_col2.success("Step 3")
        if km_col3.button('Sentence Keyword Match'):
            if text is not None:
                with st.spinner("Processing input to match keywords with sentences"):
                    sentences = tokenize_sentences(text)
                    keywords = list(get_keywords_mtf(text))[:6]
                    keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                    st.write(keyword_sentence_mapping)
                st.success('Sentence Keyword Match Completed')
            else:
                st.error("Please select input file!")
        fq_col1,fq_col2,fq_col3 = st.beta_columns((1,1,2))
        fq_col1.success("Run Model")
        fq_col2.success("Step 4")
        if fq_col3.button('Match the Following Questions'):
            if text is not None:
                with st.spinner("Processing input to generate questions"):
                    sentences = tokenize_sentences(text)
                    keywords = list(get_keywords_mtf(text))[:20]
                    keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                    sol = sentence_answers(keyword_sentence_mapping)
                    print('sol - - - ',sol)
                    question,ansr = quest_ans(sol)
                    # mtf_table= question(keyword_sentence_mapping)
                    # st.write(str(mtf_table))
                    st.table(question)
                    st.table(ansr)
                    output_file(text,"Input Text")
                    output_file(question, quest)
                    doc = DocxTemplate("MTF_template.docx")
                    context = get_context_mtf(unit,title,grade)
                    doc.render(context)
                    # doc.save(f"/content/gdrive/My Drive/questions/{folder}/{grade}th_unit{unit}_mtf.docx")
                    doc.save("School-Questions/8th/"+"unit"+context["unit"]
                             +"_mtf.docx")
                    file_path = "School-Questions/8th/"+"unit"+context["unit"]+"_mtf.docx"
                    write_table(file_path,question,ansr)
            else:
                st.error("Please select input file!")
        vm_col1,vm_col2,vm_col3 = st.beta_columns((1,1,2))
        vm_col1.success("Validate Model")
        vm_col2.success("Step 5")
        if vm_col3.button('View Model Outcome'):
            if text is not None:
                sentences = tokenize_sentences(text)
                keywords = list(get_keywords_mtf(text))[:6]
                keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                mtf_table = question(keyword_sentence_mapping)
                st.markdown(download_link(mtf_table, 'model_output.txt', 'Click here to download your output!',quest),unsafe_allow_html=True)
            else:
                st.error("Please select input file!")

def mcq():
    option = st.selectbox('',['Select Text Input or File Upload','Text Input','File Upload'])
    text = None
    if option=='Text Input':
        text = st.text_area('Enter your text here')
    elif option=='File Upload':
        text = file_selector_fill()
    if text is not None and len(text)>=20:
        text = summarize_text_mcq(text)
        quest = "MCQ"
        # unit = st.text_input("Enter unit")
        # grade = st.text_input("Enter grade")
        # title = st.text_input("Enter title")
        ts_col1,ts_col2,ts_col3 = st.beta_columns((1,1,2))
        ts_col1.success("Run Model")
        ts_col2.success("Step 1")
        if ts_col3.button('Tokenize sentences'):
            if text is not None:
                with st.spinner("Processing input to tokenize sentence"):
                    sentences = tokenize_sentences(text)
                    st.write(sentences)
                st.success('Tokenizing completed ')
            else:
                st.error("Please select input file!")
        ek_col1,ek_col2,ek_col3 = st.beta_columns((1,1,2))
        ek_col1.success("Run Model")
        ek_col2.success("Step 2")
        if ek_col3.button('Extract Keywords'):
            if text is not None:
                with st.spinner("Processing input to extract keywords"):
                    keywords = list(get_keywords_mcq(text))[:10]
                    st.write(keywords)
                st.success('Keywords Extracted')
            else:
                st.error("Please select input file!")
        km_col1,km_col2,km_col3 = st.beta_columns((1,1,2))
        km_col1.success("Run Model")
        km_col2.success("Step 3")
        if km_col3.button('Sentence Keyword Match'):
            if text is not None:
                with st.spinner("Processing input to match keywords with sentences"):
                    sentences = tokenize_sentences(text)
                    keywords = list(get_keywords_mcq(text))[:10]
                    keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                    st.write(keyword_sentence_mapping)
                st.success('Sentence Keyword Match Completed')
            else:
                st.error("Please select input file!")
        fq_col1,fq_col2,fq_col3 = st.beta_columns((1,1,2))
        fq_col1.success("Run Model")
        fq_col2.success("Step 4")
        if fq_col3.button('Multiple Choice Questions'):
            if text is not None:
                with st.spinner("Processing input to generate questions"):
                    sentences = tokenize_sentences(text)
                    keywords = list(get_keywords_mcq(text))[:10]
                    keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                    choices = kw_distractors(keywords,text)
                    mcq_ques = getMCQ(keyword_sentence_mapping,choices)
                    print(mcq_ques)
                    st.write(mcq_ques)
                    # output_file(text,"Input Text")
                    # output_file(mcq_ques, quest)
    #                 doc = DocxTemplate("MCQ_template.docx")
    #                 quest = mcq_ques
    #                 print('questttttttttttttttttt - ',quest)
    #                 context = get_context_mcq(quest,unit,grade,title)
    #                 doc.render(context)
    # #                 doc.save("complex_case_management_true_or_false.docx")
    #                 doc.save("QuestionsInWord/"+"unit"+context["unit"]+"_mcq.docx")
            else:
                st.error("Please select input file!")
        vm_col1,vm_col2,vm_col3 = st.beta_columns((1,1,2))
        vm_col1.success("Validate Model")
        vm_col2.success("Step 5")
        if vm_col3.button('View Model Outcome'):
            if text is not None:
                sentences = tokenize_sentences(text)
                keywords = list(get_keywords_mcq(text))[:10]
                keyword_sentence_mapping = get_sentences_for_keyword(keywords, sentences)
                choices = kw_distractors(keywords,text)
                mcq_ques = getMCQ(keyword_sentence_mapping,choices)
                st.markdown(download_link(mcq_ques, 'model_output.txt', 'Click here to download your output!',quest),unsafe_allow_html=True)
            else:
                st.error("Please select input file!")


def fill_blank(sentence,noun_verbs_adj,keyword_sentence_mapping_noun_verbs_adj):
    option = st.selectbox('',['Select Text Input or File Upload','Text Input','File Upload'])
    text = None
    if option=='Text Input':
        text = st.text_area('Enter your text here')
    elif option=='File Upload':
        text = file_selector_fill()
    if text is not None and len(text)>=20:
        text = text.replace('\n',' ')
        quest = "Fill in The Blanks"
        unit = st.text_input("Enter unit")
        grade = st.text_input("Enter grade")
        title = st.text_input("Enter title")
        ts_col1,ts_col2,ts_col3 = st.beta_columns((1,1,2))
        ts_col1.success("Step 1")
        ts_col2.success("Run Model")
        if ts_col3.button('Tokenize sentences'):
            if text is not None:
                with st.spinner("Processing input to tokenize sentence"):
                    sentences = tokenize_sentences(text)
                    st.write(sentences)
                st.success('Tokenizing completed ')
            else:
                st.error("Please select input file!")
        ek_col1,ek_col2,ek_col3 = st.beta_columns((1,1,2))
        ek_col1.success("Step 2")
        ek_col2.success("Run Model")
        if ek_col3.button('Extract Keywords'):
            if text is not None:
                with st.spinner("Processing input to extract keywords"):
                    noun_verbs_adj = get_noun_adj_verb(text)
                    st.write(noun_verbs_adj)
                st.success('Keywords Extracted')
            else:
                st.error("Please select input file!")
        sk_col1,sk_col2,sk_col3 = st.beta_columns((1,1,2))
        sk_col1.success("Step 3")
        sk_col2.success("Run Model")
        if sk_col3.button('Sentence Keyword Match'):
            if text is not None:
                with st.spinner("Processing input to match keywords with sentences"):
                    sentences = tokenize_sentences(text)
                    noun_verbs_adj = get_noun_adj_verb(text)
                    keyword_sentence_mapping_noun_verbs_adj = get_sentences_for_keyword(noun_verbs_adj, sentences)
                    st.write(keyword_sentence_mapping_noun_verbs_adj)
                st.success('Sentence Keyword Match Completed')
            else:
                st.error("Please select input file!")
        fb_col1,fb_col2,fb_col3 = st.beta_columns((1,1,2))
        fb_col1.success("Step 4")
        fb_col2.success("Run Model")
        if fb_col3.button('Fill in the Blank Questions'):
            if text is not None:
                with st.spinner("Processing input to generate Fill in the blank questions"):
                    sentences = tokenize_sentences(text)
                    noun_verbs_adj = get_noun_adj_verb(text)
                    keyword_sentence_mapping_noun_verbs_adj = get_sentences_for_keyword(noun_verbs_adj, sentences)
                    fill_in_the_blanks = get_fill_in_the_blanks(keyword_sentence_mapping_noun_verbs_adj)
                    st.write(fill_in_the_blanks)
                    output_file(text,"Input Text")
                    output_file(fill_in_the_blanks, quest)
                    doc = DocxTemplate("FIB_Template.docx")
                    quest = fill_in_the_blanks
                    quest_ans = list(zip(quest['sentences'],quest['keys']))
                    answers = quest['keys']
                    context = get_context_fill(quest_ans,answers,unit,grade,title)
                    doc.render(context)
    # #                 doc.save("complex_case_management_fib.docx")
                    doc.save("School-Questions/8th/"+"unit"+context["unit"]
                             +"_fill_in_the_blanks.docx")
            else:
                st.error("Please select input file!")
        vm_col1,vm_col2,vm_col3 = st.beta_columns((1,1,2))
        vm_col1.success("Step 5")
        vm_col2.success("Validate Model")
        if vm_col3.button('View Model Outcome'):
            if text is not None:
                sentences = tokenize_sentences(text)
                noun_verbs_adj = get_noun_adj_verb(text)
                keyword_sentence_mapping_noun_verbs_adj = get_sentences_for_keyword(noun_verbs_adj, sentences)
                fill_in_the_blanks = get_fill_in_the_blanks(keyword_sentence_mapping_noun_verbs_adj)
                st.markdown(download_link(fill_in_the_blanks, 'model_output.txt', 'Click here to download your output!',quest),unsafe_allow_html=True)
            else:
                st.error("Please select input file!")
                
def true_false():
    option = st.selectbox('',['Select Text Input or File Upload','Text Input','File Upload'])
    text = None
    if option=='Text Input':
        text = st.text_area('Enter your text here')
    elif option=='File Upload':
        text = file_selector_fill()
    if text is not None and len(text)>=20:
        text = text.replace('\n',' ')
        quest = "True or False"
        unit = st.text_input("Enter unit")
        grade = st.text_input("Enter grade")
        title = st.text_input("Enter title")
        st_col1,st_col2,st_col3 = st.beta_columns((1,1,2))
        st_col1.success("Run Model")
        st_col2.success("Step 1")
        if st_col3.button('Summarize Input'):
            if text is not None:
                with st.spinner("Summarizing input text based on weighted frequency"):
                    sentences = summarize_text(text)
                    st.write(sentences)
                st.success('Generated summarized sentences from given input')
            else:
                st.error("Please select input file!")
        ts_col1,ts_col2,ts_col3 = st.beta_columns((1,1,2))
        ts_col1.success("Run Model")
        ts_col2.success("Step 2")
        if ts_col3.button('Tokenize sentences'):
            if text is not None:
                with st.spinner("Processing input to tokenize sentence and get 1st sentence to generate question"):
                    sentences = summarize_text(text)
                    sentences = [i for n, i in enumerate(tokenize_sentences(sentences)) if i not in tokenize_sentences(sentences)[:n]]
                    sentences = fuzzy_dup_remove(sentences)
                    st.write(sentences)
                st.success('Tokenization completed')
            else:
                st.error("Please select input file!")
        wc_col1,wc_col2,wc_col3 = st.beta_columns((1,1,2))
        wc_col1.success("Run Model")
        wc_col2.success("Step 3")
        if wc_col3.button('Words Construction'):
            if text is not None:
                with st.spinner("Parsing input to construct words"):
                    sentences = summarize_text(text)
                    sentences = [i for n, i in enumerate(tokenize_sentences(sentences)) if i not in tokenize_sentences(sentences)[:n]][0]
                    pos = pos_tree_from_sentence(sentences)
                    st.write(pos)
                st.success('Sample Grammatical parsing completed')
            else:
                st.error("Please select input file!")
        sc_col1,sc_col2,sc_col3 = st.beta_columns((1,1,2))
        sc_col1.success("Run Model")
        sc_col2.success("Step 4")
        if sc_col3.button('Sentence Construction'):
            if text is not None:
                split_list = []
                with st.spinner("Splitting sentence in-progress"):
                    sentences = summarize_text(text)
                    sentences = [i for n, i in enumerate(tokenize_sentences(sentences)) if i not in tokenize_sentences(sentences)[:n]]
                    sentences = fuzzy_dup_remove(sentences)
                    for i,sentence in enumerate(sentences):
                        if i <5:
                            pos = pos_tree_from_sentence(sentence)
                            split_sentence = get_np_vp(pos,sentence)
                            split_list.append(split_sentence)
                    print('split_sentence in app.py- ',split_list)
                    st.write(split_list)
                st.success('Sentences are splitted')
            else:
                st.error("Please select input file!")
        as_col1,as_col2,as_col3 = st.beta_columns((1,1,2))
        as_col1.success("Run Model")
        as_col2.success("Step 5")
        if as_col3.button('Alternate Sentences'):
            if text is not None:
                alt_sent_list = []
                with st.spinner("Generating Alternate sentences"):
                    sentences = summarize_text(text)
                    sentences = [i for n, i in enumerate(tokenize_sentences(sentences)) if i not in tokenize_sentences(sentences)[:n]]
                    sentences = fuzzy_dup_remove(sentences)
                    flat_list = alternate_sentences(sentences)
                    print('flat list in main.py - ',flat_list)
                    # list_write = flat_list
                    # random.shuffle(list_write)
                    # for i,sentence in enumerate(sentences):
                    #     if i <5:
                    #         pos = pos_tree_from_sentence(sentence)
                    #         alt_sentence = alternate_sentences(pos,sentence)
                    #         alt_sent_list.append(alt_sentence)
                    #         flat_list = [item for sublist in alt_sent_list for item in sublist]
                    st.write(flat_list)
    #                 output_file(text,"Input Text")
    #                 output_file(flat_list,quest)
                    li2 = []
                    # for i in flat_list:
                    #     for j in list_write:
                    #         print('i value - ',i)
                    #         print('j value - ',j)
                    #         if i==j:
                    #             li2.append('True')
                    #         else:
                    #             li2.append('False')
                    #         break
                    for i,itm in enumerate(flat_list):
                        if i%2==0:
                            li2.append('False')
                        else:
                            li2.append('True')
                    doc = DocxTemplate("TrueFalse_Template.docx")
                    quest = list(zip(flat_list,li2))
    #                 print('questttttttttttttttttt - ',quest)
                    context = get_context_tf(quest,unit,grade,title)
                    doc.render(context)
    # #                 doc.save("complex_case_manageme   nt_true_or_false.docx")
                    doc.save("School-Questions/8th/"+"unit"+context["unit"]+"_true_or_false.docx")
            else:
                st.error("Please select input file!")
        vm_col1,vm_col2,vm_col3 = st.beta_columns((1,1,2))
        vm_col1.success("Validate Model")
        vm_col2.success("Step 6")
        if vm_col3.button('View Model Outcome'):
            if text is not None:
                alt_sent_list = []
                sentences = summarize_text(text)
                sentences = [i for n, i in enumerate(tokenize_sentences(sentences)) if i not in tokenize_sentences(sentences)[:n]]
                sentences = fuzzy_dup_remove(sentences)
                flat_list = list(alternate_sentences(sentences))
                # for i,sentence in enumerate(sentences):
                #     if i <5:
                #         pos = pos_tree_from_sentence(sentence)
                #         alt_sentence = alternate_sentences(pos,sentence)
                #         alt_sent_list.append(alt_sentence)
                #         flat_list = [item for sublist in alt_sent_list for item in sublist]
                st.markdown(download_link(flat_list, 'model_output.txt', 'Click here to download your output!',quest),unsafe_allow_html=True)
            else:
                st.error("Please select input file!")
            
            
def new_fn():
    text = file_selector_fill()
    if text is not None:
        sentences = tokenize_sentences(text)
        noun_verbs_adj = get_noun_adj_verb(text)
        keyword_sentence_mapping_noun_verbs_adj = get_sentences_for_keyword(noun_verbs_adj, sentences)
        fill_in_the_blanks = get_fill_in_the_blanks(keyword_sentence_mapping_noun_verbs_adj)
        quest_ans = {"questions": fill_in_the_blanks["sentences"] ,"answers": fill_in_the_blanks["keys"]}
        print("Keys: ",fill_in_the_blanks["keys"])
        mark,ques = 0,[]
        with st.form(key="fib_form"):
            st.text('1.'+fill_in_the_blanks["sentences"][0])
            a1 = st.text_input("Enter your answer here")
            submitted = st.form_submit_button(label='Submit')
            if submitted:
                st.success(a1)
                print('a1 inside submitted - ',a1)
                if a1 == fill_in_the_blanks["keys"][0]:
                    mark = mark+1
        with st.form(key="fib_form2"):
            st.text('2.'+fill_in_the_blanks["sentences"][1])
            a2 = st.text_input("Enter your answer here")
            submitted = st.form_submit_button(label='Submit')
            if submitted:
                st.success(a2)
                print('a2 inside submitted - ',a2)
                if a2 == fill_in_the_blanks["keys"][1]:
                    mark = mark+1
        print('mark - ',mark)
        st.success('Your mark - '+str(mark))

            
            
            
def word_similarity():
    text = file_selector()
    if st.button("Remove Stopwords"):
        if text is not None:
            with st.spinner("In-Progress"):
                text3 = remove_stopwords(text)
            st.success("Successfully removed stopwords")
        else:
            st.error("Please select input file!")
            
    if st.button("Sentence Tokenization"):
        if text is not None:
            with st.spinner("In-Progress"):
                text3 = remove_stopwords(text)
                text2 = sent_tokenize(text3)
            st.success("Successfully tokenized the text into sentences")
        else:
            st.error("Please check the input file!")
            
    if st.button("Remove Special Characters and Convert the text to Lower Case"):
        if text is not None:
            with st.spinner("In-Progress"):
                text3 = remove_stopwords(text)
                text2 = sent_tokenize(text3)
                clean_text = remove_special_Charac(text2)
            st.success("Successfully removed special characters and converted the text to lower case")
        else:
            st.error("Please check the input file!")
            
    if st.button("Train the Model"):
        if text is not None:
            with st.spinner("In-Progress"):
                text3 = remove_stopwords(text)
                text2 = sent_tokenize(text3)
                clean_text = remove_special_Charac(text2)
                model = Train_Model(clean_text)
            st.success("Model training successful")
        else:
            st.error("Please check the input file!")
            
    word = st.text_input('Input your word here in lower case and press ENTER:')
    if len(word)>0:
        if st.button("Model Outcome"):
            if text is not None:
                with st.spinner("Applying the trained Model"):
                    text3 = remove_stopwords(text)
                    text2 = sent_tokenize(text3)
                    clean_text = remove_special_Charac(text2)
                    model = Train_Model(clean_text)
                    output = Model_Outcome(model,word)
                st.write(output)
            else:
                st.error("Please check the model!")
#    else:
#        st.error("Type some input word")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
def all_initialisations():
    local_css("style.css")
    image = Image.open('DeepSphere_Logo_Final.png')
    
    activities= ['Select Your Question Type','Fill in the Blanks','True or False', 'Match the Following', 'MCQ']
    model_choices = ['Model Implemented','BERT']
    libraries = ['Library Used','spacy','nltk','tensorflow','allennlp','flashtext','streamlit','pke','sense2vec','gensim','selenium','beautiful soup']
    gcp = ['GCP Services Used','VM Instance','Compute Engine']
    operation = ['Select Your Choice','Content Generation','Question Generation']
    new_choice = ['Select Your Choice','Content Generation','Question Generation']
    href = f'<a style="color:black;" href="http://localhost:8501/" class="button">Clear/Reset</a>'
    st.sidebar.markdown(href, unsafe_allow_html=True)
    choice = None
    choice2 = None
#     if os.path.isfile('next.p'):
#         next_clicked = pkle.load(open('next.p', 'rb'))
#         # check if you are at the end of the list of pages
#         if next_clicked == len(new_choice):
#             next_clicked = 0 # go back to the beginning i.e. homepage
#     else:
#         next_clicked = 0 #the start
# #     choice2 = st.sidebar.selectbox('',operation,index=next_clicked)
#     if choice2 is None:
#         st.image(image)
#         mainfn()
#         next1, next2 = st.beta_columns(2)
#         if next1.button("Explore Content"):
#             #increment value to get to the next page
#             next_clicked = 1

#             # check if you are at the end of the list of pages again
#             if next_clicked == len(new_choice):
#                 next_clicked = 0 # go back to the beginning i.e. homepage

#         if next2.button("Explore Question"):
#             #increment value to get to the next page
#             next_clicked = 2

#             # check if you are at the end of the list of pages again
#             if next_clicked == len(new_choice):
#                 next_clicked = 0 # go back to the beginning i.e. homepage
#     choice2 = st.sidebar.selectbox('',new_choice,index=next_clicked)
    choice2 = st.sidebar.selectbox('',new_choice)

    # pickle the index associated with the value, to keep track if the radio button has been used
#     pkle.dump(new_choice.index(choice2), open('next.p', 'wb'))
    
    if choice2 == 'Question Generation':
        st.image(image)    
        st.markdown('<h2>NLP Simplifies Questions and Assignments Construction<br> <font style="color: #5500FF;">Powered by Google Cloud Products</font></h2>',unsafe_allow_html=True)
        st.markdown('<hr style="border-top: 6px solid #8c8b8b; width: 150%;margin-left:-180px">',unsafe_allow_html=True)
#         st.markdown('''<div class="footer">
# <div class="row">
#       <div class="col-sm-12 col-md-12 fourth-part1">
# 		 <div class="footer-copyright  copyryt text-center">© 2021 <a href="https://www.deepsphere.ai/">DeepSphere.ai.</a> All rights reserved</div>
# 	  </div>
# </div>
# </div>''',unsafe_allow_html=True)
        choice = st.sidebar.selectbox('',activities)
    #         model_choice = st.sidebar.selectbox('',model_choices)
        libraries_choice = st.sidebar.selectbox('',libraries)
        gcp_services = st.sidebar.selectbox('',gcp)
    elif choice2 == 'Content Generation':
        st.image(image)
#         st.markdown('''<div class="footer">
# <div class="row">
#       <div class="col-sm-12 col-md-12 fourth-part1">
# 		 <div class="footer-copyright  copyryt text-center">© 2021 <a href="https://www.deepsphere.ai/">DeepSphere.ai.</a> All rights reserved</div>
# 	  </div>
# </div>
# </div>''',unsafe_allow_html=True)
        st.markdown('<h2>Content Generation for the Given Topic using Web Scraping and NLP</h2>',unsafe_allow_html=True)
        st.markdown('<hr style="border-top: 6px solid #8c8b8b; width: 150%;margin-left:-180px">',unsafe_allow_html=True)
        # st.title("Content Generation for the Given Topic using **_Web Scraping_** and **_NLP_**")
#         st.sidebar.title("Content Creation for the Given Topic using Web Scraping and NLP")
        #st.markdown("This application is to extract URLs and text content related to the given topic:")
#         st.markdown("***")
#         st.sidebar.markdown("This application is to extract URLs and text content for the given topic")
#         model_choice = st.sidebar.selectbox('',model_choices)
        libraries_choice = st.sidebar.selectbox('',libraries)
        gcp_services = st.sidebar.selectbox('',gcp)
#         add document gen code
    else:
#         pass
        st.image(image)
        mainfn()
# #         st.image(image)
#         st.title("Content and Question Generation Application")
#         st.markdown('<hr style="border-top: 6px solid #8c8b8b; width: 150%;margin-left:-180px">',unsafe_allow_html=True)
    return choice,choice2
