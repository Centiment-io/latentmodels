
# Instructions:
# 
# For the Tableau plots, I currently read in a tab-delimited file with the following columns, in addition to the media_cloud_{document|metadata}.tab files provided by David/Sands.  For performance reasons, I keep only the top 250,000 entries by value.  The full matrix would require N * M number of rows where M = number of documents, N = number of topics.
# 
# doc_id: string
# 
# topic_index: integer between 1 and N (or 0 and N-1)
# 
# value: float representing the topical proportion for "topic_index" in "doc_id"
# 
# topic_desc: string representing the top 5 terms in a topic
# 
# To reduce file size, please free to strip the field "topic_desc" from the above file, and store them separately.  Perhaps as another tab-delimited file with two columns, say:
# 
# topic_index: integer between 1 and N
# topic_desc: string representing the top 5 terms in a topic
# 

# In[42]:

import os, sys, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger('Archive.LDA')


# In[43]:

doctopics_fields = [ "doc_id", "topic_index", "value" ]
topicdesc_fields = [ "topic_index", "topic_desc" ]


# In[27]:

# filepaths
HOME = "/Users/wli/"
DROPBOX_FOLDER = "Dropbox/kkk_2014_paper/"
DATA_FOLDER = "topic_experiments_william/"
DAYS = 90
TOPICS = 100

EXPERIMENT_NAME = "gensim_%sdays_%stopics" % ( DAYS, TOPICS )

ARTICLE_IDS = "article-ids.txt"
DOC_TOPICS = "doc-topics.txt"
TOPIC_TERMS = "topic-terms.txt"

OUTPUT_DOC = "doc_id-topic_index-value.txt"
NUM_ENTRIES = 250000

OUTPUT_TOPICDESC = "topic_index-topic_desc.txt"


# In[4]:

article_filepath = os.path.join( HOME, DROPBOX_FOLDER, DATA_FOLDER, EXPERIMENT_NAME, EXPERIMENT_NAME + "-" + ARTICLE_IDS ) 

with open( article_filepath ) as f:
    article_ids = [ int( i.strip('\n') ) for i in f.readlines() ]


# In[5]:

doc_topics_filepath = os.path.join( HOME, DROPBOX_FOLDER, DATA_FOLDER, EXPERIMENT_NAME, EXPERIMENT_NAME + "-" + DOC_TOPICS )
doc_topic_probs = []
with open( doc_topics_filepath ) as f:
    x = [ i.strip('\r\n') for i in f.readlines() ]


# In[6]:

for line in x:
    doc_topic_probs.append( [ float( i ) for i in line.split(',') ] )


# In[44]:

NUM_TOPICS_TO_KEEP = 4
top_doc_topic_probs = []
for doc_idx, topic_values in enumerate( doc_topic_probs ):
    if doc_idx % 20000 == 0:
        sys.stderr.write( "%s..." % doc_idx )
    idx_topic_values = [ (idx,i) for idx,i in enumerate( topic_values ) ]
    idx_topic_values.sort( key=lambda x:x[1], reverse=True )
    top_doc_topic_probs.append( idx_topic_values[:NUM_TOPICS_TO_KEEP] ) 


# Out[44]:

#     0...20000...40000...60000...

# In[45]:

docs_topics_values = []
for idx, doc_id in enumerate( article_ids ):
    if idx % 20000 == 0:
        sys.stderr.write( "%s..." % idx )
    for topic_index, topic_value in top_doc_topic_probs[idx]:
        docs_topics_values.append( ( doc_id, topic_index, topic_value ) )
sys.stderr.write( "done.\n" )
                


# Out[45]:

#     0...20000...40000...60000...80000...

# In[46]:

docs_topics_values.sort( key=lambda x:x[2], reverse=True )


# In[48]:

output_doc_topic_values_filepath = os.path.join( HOME, DROPBOX_FOLDER, DATA_FOLDER, EXPERIMENT_NAME, "viz", EXPERIMENT_NAME + "-"                                                + OUTPUT_DOC )


NUM_ENTRIES = len( docs_topics_values )
with open( output_doc_topic_values_filepath, 'wb' ) as f:
    f.write( "\t".join( doctopics_fields ) + "\n" )
    for i in range( NUM_ENTRIES ):
        f.write( "\t".join( [ str(i) for i in docs_topics_values[i] ] ) + "\n" )


# In[49]:

topicdesc_filepath = os.path.join( HOME, DROPBOX_FOLDER, DATA_FOLDER, EXPERIMENT_NAME, EXPERIMENT_NAME + "-" + TOPIC_TERMS )
output_topicdesc_filepath = os.path.join( HOME, DROPBOX_FOLDER, DATA_FOLDER, EXPERIMENT_NAME, "viz", EXPERIMENT_NAME + "-" + OUTPUT_TOPICDESC )

output_desc = []

with open( topicdesc_filepath ) as f:
    x = [ i.strip('\n') for i in f.readlines() ]
    
    for line in x:
        split_line = line.split(', ')
        topic_id = split_line[0]
        top_words = ", ".join( split_line[1:6] )
        output_desc.append( ( topic_id, top_words ) )
        
with open( output_topicdesc_filepath, 'wb' ) as f:
    f.write( "\t".join( topicdesc_fields ) + "\n" )
    for line in output_desc:
        f.write( "\t".join( line ) + "\n" )
        


# In[ ]:



