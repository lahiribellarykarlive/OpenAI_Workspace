###################################
# This python script connects to openai
# and generates a knowledge base article from PIR
# Input: PIR
# Output: Knowledge base article
# Limitations: The number of tokens allowed in Input
# depend on the chosen model. If Input has more tokens than 1000,
# it is advisable to check the Context Window of model used.
###################################
from openai import OpenAI
import json
from jproperties import Properties

def getPropertiesReader():
    configs= Properties()
    with open('kbase.properties',"rb") as config_file:
        configs.load(config_file)
    return configs

#Connect to OpenAI with the Key in the os path
def openaiConnect():
    client = OpenAI()
    return client

#Get the pir data
def getPir():
    pir= getPropertiesReader().get("PIR").data
    return pir

#get prompts engineered for usecase
def getPrompts():
    prompts = ["Start Output with Knowledge Base article for incidnet number wait for next message","Generate Knowledge base article from next message"]
    return prompts

#get final response from OpenAI
def getOpenAiResponse(modelName, message):
    client = openaiConnect()
    response = client.chat.completions.create(model=modelName, messages=message)
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

print(openAIresponse)