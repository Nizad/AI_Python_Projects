import nltk
from nltk.chat.util import Chat , reflections

pairs = [
         ['(.*)help(.*)' , ['I can help you']],
         ['(hi|salam|hey|hello)', ['Hey there','Hi','Hello']],
         ['(.*)(location|city|country)', ['Tehran, Iran']],
         ['(.*)(address)', ['No.6 , Maryam Building , 17th St (Behzad Shafagh)Ahmad Ghasir(Bokharest) Av. Arjantin Sq.']],
         ['(.*)(phone|tel|telephone)', ['+98 (21) 85760']],
         ['(.*)(fax)', ['+98 (21) 88706606']],
         ['(.*)(email)' , ['extranet@amadeusiran.net']],
         ['(.*)(order|invoice|finance|financial)' , ['http://www.amadeusiran.net/Account/FinancialRecords.aspx']],
         ['quit' , ['Bye', 'See you soon']]
]

def chatbot():
    # print("Hi, I'm the chatbot you built") 
    chat = Chat(pairs, reflections)
    chat.converse()    


# chatbot()



#  > python -m py_compile NI_Chatbot.py


