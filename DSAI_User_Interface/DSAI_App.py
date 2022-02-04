########################################################

#Copyright (c) DeepSphere.AI 2021

# All rights reserved

# We are sharing this partial code for learning and research, and the idea behind us sharing the source code is to stimulate ideas #and thoughts for the learners to develop their MLOps.

# Author: # DeepSphere.AI | deepsphere.ai | dsschoolofai.com | info@deepsphere.ai

# Release: Initial release

#######################################################
  
import streamlit as st
import traceback
from PIL import Image
# Utils Pkgs
import codecs
import streamlit.components.v1 as stc
import textwrap
import pandas as pd
import base64
from datetime import datetime

from main import all_initialisations,mcq,match_the_foll,fill_blank,true_false,word_similarity,new_fn
from content_create import main


if __name__=='__main__':
    try:
        vAR_choice,vAR_operation = all_initialisations()
        vAR_sentences= []
        vAR_noun_verbs_adj=[]
        vAR_keyword_sentence_mapping_noun_verbs_adj = {}
        if vAR_choice=='Fill in the Blanks':
            st.subheader(vAR_choice)
            fill_blank( vAR_sentences,vAR_noun_verbs_adj,vAR_keyword_sentence_mapping_noun_verbs_adj)
        if vAR_choice=='True or False':
            st.subheader(vAR_choice)
            true_false()
        if vAR_choice == 'Match the Following':
            st.subheader(vAR_choice)
            match_the_foll()
        if vAR_choice == 'MCQ':
            st.subheader('Multiple Choice Questions')
            mcq()
        if vAR_choice == 'Word Similarity':
            st.subheader('Word Similarity')
            word_similarity()
        if vAR_operation == 'Content Generation':
            st.subheader('Enter Your Topic Here')
            main()
        # if vAR_choice == 'Questions':
        #     st.subheader('Questions')
        #     new_fn()
    except BaseException as e:
        print('error in main method - ',e)
        traceback.print_exc()
