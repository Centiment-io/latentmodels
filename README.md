latentmodels
============

# Small experiment

python 001_create_gensim_data.py /datadrive/derived_data/data_gensim/text_only_for_gensim.txt /datadrive/derived_data/data_gensim/text_only

7 days, 10 topics:

python 002_train_gensim_lda.py /datadrive/derived_data/data_gensim/text_only.mm/text_only_for_gensim.txt.mm /datadrive/derived_data/data_gensim/text_only.mm/text_only_for_gensim.txt.dict /datadrive/output/gensim_7days_10topics/gensim_7days_10topics 10

# Large experiment