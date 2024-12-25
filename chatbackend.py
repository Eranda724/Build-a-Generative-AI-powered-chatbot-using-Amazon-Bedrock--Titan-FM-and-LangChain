#langchain function
from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationSummeryBufferMemory
from langchain.chains import ConversationChain

#invoke model
def titan_llm(input_text):
    llm=BedrockChat(
    model_id="amazon.titan-text-express-v1",
    model_kwargs={
        "maxTokenCount":100,
        "temperature":0.5, #reative max  = 1
        "topP":1,
        }

    )
    #return llm

#test

    return llm.invoke(input_text)
response=titan_llm("What is your name? ")
print(response)
































