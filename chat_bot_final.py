from transformers import pipeline, Conversation

class ChatBot: 
    #Usage 
    #Instantiate chatbot with ChatBot() 
    #start conversation with chat_bot_object.start_conversation()
    def __init__(self): 
      #create conversational pipeline and establish counter for current conversation and create Converastion() object
      #self.conversational_pipeline = pipeline(model="conversational_model", task="conversational")
      self.conversational_pipeline = pipeline("conversational")
      self.keep_short_conversation = 0 
      self.conversation = Conversation()

    def start_conversation(self): 
      #get user input and feed it to answer_question method 
      question = input("Ask me something: ")
      self.answer_question(question)

    def answer_question(self, question): 
      #if length of question is one word or no input then end conversation
      if len(question.split()) <= 1: 
        pass
      else:
        #keep limit of reponses per conversation
        if self.keep_short_conversation <= 2:
          self.conversation.add_user_input(question)
          response = self.conversational_pipeline(self.conversation)
          self.keep_short_conversation += 1
          self.print_response(response) 
        #if limit crossed then restart conversation and reset counter
        else: 
          self.conversation = Conversation()
          self.conversation.add_user_input(question)
          self.keep_short_conversation = 0
          response = self.conversational_pipeline(self.conversation)
          self.print_response(response) 

    def print_response(self, response): 
      #print the latest generated response 
      print(response.generated_responses[-1])
      #print response calls for another question
      self.start_conversation()

#instantiate chatbot
chat_bot = ChatBot()
#start a conversation    
chat_bot.start_conversation()


        
        

