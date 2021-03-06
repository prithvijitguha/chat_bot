"""
Chat_Bot model
"""

import os
from transformers import pipeline, Conversation


class ChatBot:
    """Chat Bot Class used to
    Instantiate chatbot with ChatBot()
    Args: None
    Returns: print(Response)

    Usage:
    ```
    chat_bot_object = ChatBot()
    chat_bot_object.start_conversation()
    Ask me something:
    ```
    """
    def __init__(self):
        # create conversational pipeline and establish counter
        # for current conversation
        # and create Converastion() object
        # check for model
        if os.path.isdir("model"):
            # if model found use it
            self.conversational_pipeline = pipeline(
                model="./model", task="conversational"
            )
        # otherwise download model
        else:
            self.conversational_pipeline = pipeline("conversational")
        self.keep_short_conversation = 0
        self.conversation = Conversation()

    def start_conversation(self):
        """
        start_conversation is used to start a conversation
        with chat_bot_object

        Args: None
        Returns: None

        Usage:
        ```
        chat_bot_object = ChatBot()
        chat_bot_object.start_conversation()
        ```
        """
        question = input("Ask me something: ")
        self.answer_question(question)

    def answer_question(self, question):
        """
        Inbuilt method to answer question given by user
        If user input is one word it ends the conversation
        Keep conversation token for only 2 reponses

        Args: Question
        Returns: print_response()
        """
        # if length of question is one word or no input then end conversation
        if len(question.split()) <= 1:
            pass
        else:
            # keep limit of reponses per conversation
            if self.keep_short_conversation <= 2:
                self.conversation.add_user_input(question)
                response = self.conversational_pipeline(self.conversation)
                self.keep_short_conversation += 1
                self.print_response(response)
            # if limit crossed then restart conversation and reset counter
            else:
                self.conversation = Conversation()
                self.conversation.add_user_input(question)
                self.keep_short_conversation = 0
                response = self.conversational_pipeline(self.conversation)
                self.print_response(response)

    def print_response(self, response):
        """
        Used to print the latest response
        from chat_bot_object

        Args: response
        Returns: print(response)
        """
        # print the latest generated response
        print(response.generated_responses[-1])
        # print response calls for another question
        self.start_conversation()


