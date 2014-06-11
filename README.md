latentmodels
============

# Small experiment (7 days, 10 topics)

1.  `bash 000_tab_to_text.sh /datadrive/kkk_2014_paper/mc_dumps/2014_04_24_to_2014_05_02_d2/ > /datadrive/derived_data/data_gensim/text_only_for_gensim.txt`
2. `python 001_create_gensim_data.py /datadrive/derived_data/data_gensim/text_only_for_gensim.txt /datadrive/derived_data/data_gensim/text_only.mm`
3. `python 002_train_gensim_lda.py /datadrive/derived_data/data_gensim/text_only.mm/text_only_for_gensim.txt.mm /datadrive/derived_data/data_gensim/text_only.mm/text_only_for_gensim.txt.dict /datadrive/output/gensim_7days_10topics/gensim_7days_10topics 10`

Outputs:
`gensim_7days_10topics`  
`gensim_7days_10topics-doc-topics.txt`  
`gensim_7days_10topics.state`  
`gensim_7days_10topics-topic-terms.txt`  
`gensim_7days_10topics-topic-terms-with-probs.txt`


# Large experiment