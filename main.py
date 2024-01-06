import argparse
import timeit
from utils import setup_dbqa
import streamlit as st
from llm import load_llm

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('input',type=str)
#     args = parser.parse_args()
#     start = timeit.default_timer()

#     dbqa = setup_dbqa()

#     response = dbqa({'query' : args.input})
#     end = timeit.default_timer()

#     print(f'\nAnswer : {response["result"]}')
#     print('='*50)

#     source_docs = response['source_documents']
#     for i,doc in enumerate(source_docs):
#         print(f'\nSource Documents {i+1}\n')
#         print(f'Source Text : {doc.page_content}')
#         print(f'Document Name : {doc.metadata["source"]}')
#         print(f'Page Number : {doc.metadata["page"]}\n')
#         print('='*50)
    
#     print(f"Time to retrieve response : {end - start}")

st.set_page_config(page_title='Doc Q&A')
st.title('Ask the PDF App')

dbqa = setup_dbqa()

query_text = st.text_input('Enter a query: ')
if(st.button('Submit')):
    query_response = dbqa({'query': query_text})
    st.write(query_response["result"])

