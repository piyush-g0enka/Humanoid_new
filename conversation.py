
from dialogflow_modules import get_response_from_dialogflow
from nltk_modules import output_nltk_text
from speech_api import SpeakText , listen


def convo(name_of_person):

    le_text =""

    captured_text = listen()

    if captured_text == "terminate":
        le_text = "off"

    else:    

        try:

            

        
            dialog_response = get_response_from_dialogflow(captured_text)

            if dialog_response == "nltk":

                nltk_response = output_nltk_text(name_of_person ,captured_text )

                print("Bot: "+ nltk_response)
                SpeakText(nltk_response)



            elif dialog_response == "clsprg":

                print("Bot: Goodbye "+ name_of_person)
                SpeakText("Goodbye " + name_of_person)

                le_text="bye"
                
                

            else:
                
                print("Bot: "+ dialog_response)
                SpeakText(dialog_response)
            


        except Exception:
            
            print("Bot: Could you please repeat?")
            SpeakText("Could you please repeat?")






    return le_text



if __name__ == "__main__":
    
        while True:
                print(convo("piyush"))
