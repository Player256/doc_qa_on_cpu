from langchain.llms import CTransformers
import streamlit as st	
 
@st.cache(allow_output_mutation=True)
def load_llm() :
	llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin', 
	                    model_type='llama', 
	                    config={'max_new_tokens': 256,
	                            'temperature': 0.01})
	return llm

# llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin', 
# 	                    model_type='llama', 
# 	                    config={'max_new_tokens': 256,
# 	                            'temperature': 0.01})