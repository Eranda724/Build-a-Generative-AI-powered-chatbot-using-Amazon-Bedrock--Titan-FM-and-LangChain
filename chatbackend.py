#langchain function
from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
#from langchain_aws import ChatBedrock

#invoke model
def titan_llm(input_text):
    llm=BedrockChat(
    model_id="amazon.titan-t5-large",
    model_kwargs={
        "temperature":0.5, #reative maxSD  = 1
        "maxTokenCount":100,
        "topP":1,
        }
        )
    #return llm

#test

    return llm.invoke(input_text)
response=titan_llm("What is your name? ")
print(response)
































