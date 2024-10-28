import chainlit as cl
from message import Message, Format, SubFormat
import requests

@cl.on_message
async def main(message: cl.Message):
    data = Message(
        control=False,
        format=Format.TEXT,
        subformat=SubFormat.ENGLISH,
        content=message.content,
        submessages=[]
    )
    url = "https://druid.eecs.umich.edu:80/text/"
    
    json_data = {
        "format": data.format.value,
        "subformat": data.subformat.value,
        "content": data.content
    }
    response = requests.post(url,json=json_data, verify='/Users/rithikb/Documents/Sugih/Chainlit/rootCA.pem')
    
    # Send a response back to the user
    await cl.Message(
        content=f"{response.json()['content']}",
    ).send()
