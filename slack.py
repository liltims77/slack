import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime

#import slack slack_sdk
 


# client = WebClient(token=os.environ.get("xoxb-294379454134-6630280445287-A6H7DEn30RqpjOmOtmF8hABp"))

client = WebClient(token=os.environ.get("xoxe-1-My0xLTMwNTg5MDYxMjA5MTctODI3MjIwMjA4MTg3Mi04MjUxOTAyNDcwNzg4LWQ0ZTA5MmU1MTJiNTQxNDJmODkxNmNjOGI0NjlhYzA5MmFmMGRiMTZmM2FmNzQzMzg2ZjkwZmJmODViOGEzN2U"))
#client = WebClient(token="xoxb-294379454134-6630280445287-A6H7DEn30RqpjOmOtmF8hABp")
logger = logging.getLogger(__name__)
#Purpose: Sets up a logger to log messages, making it easier to debug.
#Details: logging.getLogger(__name__) creates a logger named after the current module (__name__), so you can write logs like info, warning, or error.

# Store conversation history
conversation_history = []
# ID of the channel you want to send the message to
# channel_id = "C06HAJWGLEP" C031TPXHPK4
channel_id = "C031TPXHPK4"


try:
    # Call the conversations.history method using the WebClient
    # conversations.history returns the first 100 messages by default
    # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
    result = client.conversations_history(channel=channel_id)
    #A parameter is a placeholder or input name defined in a function (or method) declaration. eg "channel" is a parameter
    #It fetches the conversation history from Slack using the client, and the channel_id specifies which channel to fetch it from
    #it fetches the conversation_history from client using the channel_id
    #Parameter: The name defined in the function declaration to specify what kind of input the function expects. In this case, channel is the parameter expected by the conversations_history() method.
    #Purpose: Fetches the message history from the specified Slack channel.
    #client.conversations_history: Makes an API call to fetch messages.
    #channel=channel_id: Sends the request for a specific channel by its ID.


    #The ["messages"] part retrieves the value associated with the key "messages" in the result dictionary
    conversation_history = result["messages"]
    #Purpose: Extracts messages from the API response dictionary. The API response includes a messages key that contains all messages.

    # Print results
    logger.info("{} messages found in {}".format(len(conversation_history), channel_id))
    #Purpose: Logs how many messages were found in the specified channel.

except SlackApiError as e:
    logger.error("Error creating conversation: {}".format(e))
#Purpose: Captures errors if the API call fails and logs the error message.
#Details: SlackApiError is specific to Slack’s Python SDK, and .error(...) logs the error.

print(conversation_history)





output = []

for message in conversation_history:
    formatted_message = {
        "id": message["ts"],
        "datetime": datetime.fromtimestamp(float(message["ts"])).strftime('%Y-%m-%d %H:%M:%S'),
        "user": message["user"],
        "text": message["text"],
    }

    #Iterates through each message in conversation_history and formats it.
    #for message in conversation_history: loops over every message (i.e., every dictionary) in the conversation_history list.
    #Inside the loop, the script creates a formatted_message dictionary to organize important data from the message dictionary.
    
     
    formatted_replies = []
    if 'reply_count' in message:
        result = client.conversations_replies(channel=channel_id, ts=message['ts'])
        replies = result['messages']
        #Purpose: Checks if the current message has replies (using reply_count). If yes:
        #Calls conversations_replies to get replies to the message using its timestamp (ts).
        #Retrieves those replies in result['messages'].       
          
        for reply in replies:
            formatted_reply = {
        "id": reply["ts"],
        "datetime": datetime.fromtimestamp(float(reply["ts"])).strftime('%Y-%m-%d %H:%M:%S'),
        "user": reply["user"],
        "text": reply["text"],
    }
            formatted_replies.append (formatted_reply)
           #  Loops through the list of replies, formats each reply, and appends it to formatted_replies
        formatted_message['replies'] = formatted_replies #Attaches all formatted replies as a key (replies) to the original formatted_message.
    output.append (formatted_message) #Adds the formatted message (with its replies) to the output list.
   
          
print(output)




# import logging
# import os
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Initialize the Slack client using an environment variable for the token
# client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))

# # Function to fetch conversation history
# def fetch_conversation_history(client, channel_id):
#     """
#     Fetch conversation history from a specified Slack channel.
    
#     Args:
#     - client: The Slack WebClient used to communicate with Slack's API.
#     - channel_id: The ID of the Slack channel to fetch messages from.
    
#     Returns:
#     - List of messages retrieved from the channel.
#     """
#     try:
#         # Fetch conversation history from the specified channel
#         result = client.conversations_history(channel=channel_id)
        
#         # Extract and return the messages from the result
#         messages = result["messages"]
        
#         # Log the number of messages found
#         logger.info(f"{len(messages)} messages found in channel {channel_id}")
        
#         return messages

#     except SlackApiError as e:
#         # Log an error if the API request fails
#         logger.error(f"Error fetching conversation history: {e.response['error']}")
#         return []  # Return an empty list if there is an error

# # Channel ID of the channel you want to fetch messages from
# channel_id = "C06HAJWGLEP"

# # Call the function and print the result
# conversation_history = fetch_conversation_history(client, channel_id)
# print(conversation_history)








