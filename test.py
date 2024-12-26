from langchain_aws import ChatBedrock

# Invoke model
def titan_llm(input_text):
    # Initialize the ChatBedrock model (new method)
    llm = ChatBedrock(
        model_id="your-correct-model-id",  # Replace with a valid model ID
        model_kwargs={
            "temperature": 0.5,  # Creativity level
            "maxTokenCount": 100,
            "topP": 1,
        }
    )
    # Use the new `invoke` method
    response = llm.invoke(input_text)  # Use invoke() instead of predict()
    return response

# Test
response = titan_llm("What is your name?")
print(response)
