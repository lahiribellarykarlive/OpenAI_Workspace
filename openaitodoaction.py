###################################
# This python script connects to openai
# and extracts TODO actions the PIR
# Input: PIR
# Output: List of TODO actions
# Limitations: The number of tokens allowed in Input
# depend on the chosen model. If Input has more than 1000 tokens,
# it is advisable to check the Context Window of model used.
###################################
from openai import OpenAI
import json
from jproperties import Properties

def getPropertiesReader():
    configs= Properties()
    with open('todoaction.properties',"rb") as config_file:
        configs.load(config_file)
    return configs

#Connect to OpenAI with the Key in the os path
def openaiConnect():
    client = OpenAI()
    return client

#Get the pir data
def getPir():
    pir= getPropertiesReader().get("TRANSCRIPT").data
    return pir

#get prompts engineered for usecase
def getPrompts():
    prompts = ["ChatCompletion object MUST be JSON","Find out to do actions from my next message"]
    return prompts

#get final response from OpenAI
def getOpenAiResponse(modelName, message):
    client = openaiConnect()
    response = client.chat.completions.create(
        model=modelName, 
        response_format={"type":"json_object"},
        messages=message)
    return response

#get Input message to be sent to OpenAI
def getInputMessage():
    prompts = getPrompts()
    pir = getPir()
    message=[]    
    for prompt in prompts:
        jsonObject = {}
        jsonObject["role"]="user"
        jsonObject["content"]=prompt
        message.append(jsonObject) 
    jsonObjectIOMessage={}
    jsonObjectIOMessage["role"]="user"
    jsonObjectIOMessage["content"]=pir

    message.append(jsonObjectIOMessage)
    return message

#get Model Name
def getModelName():
    return getPropertiesReader().get("MODELNAME").data

modelName = getModelName()
message = getInputMessage()

openAIresponse = getOpenAiResponse(modelName, message)
jsonResponse = openAIresponse.model_dump_json()

print(jsonResponse)