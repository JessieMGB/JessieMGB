import string
import random

#starter greeting that will print when RateBot is first run
greeting = "Hello, I'm RateBot. The completely non-biased movie rating AI."
starter_sentence = "These are the movies currently avialable for rating. Type any name to start:"
goodbye = "When you are finished type 'quit' to exit."

#lists to store different movies by categories based on non-biased opinion
good_movies = ["Avengers", "ToyStory", "Us", "Titanic", "TheConjuring", "AQuietPlace", 
               "Coco", "WonderWoman", "MeanGirls", "Shrek", "TheBasketballDiaries",
               "CatchMeIfYouCan", "LegoMovie"]
bad_movies = ["Avatar", "FantasticFour", "Hereditary", "TheNightmareBeforeChristmas",
              "Justice-League", "BatmanVs.Superman", "SupermanManofSteel",
             "TheCurseOfLaLlorona", "TheNun", "Split", "DarkPheonix"]
never_seen = ["PulpFiction", "BreakfastClub", "Grease", "ForestGump", "Frozen", "Aquaman", 
              "Glass", "DoctorStrange"]

#list of responses
good_responses = ["This movie is awesome!", "I love this movie.","I agree this deserves an Oscar!",
                  "Who knew you would agree with me that this movie is the best!", "Yes, I do love this movie."]
bad_responses = ["This movie is not good, 0/10.", "I agree, this movie is bad.", "Nope. Just nope.",
                 "At least they tried."]
unknown_responses = ["Never seen this movie before", "I have unfortunately, or fortunately, never seen it."
                    "Can't say due to never watching this movie.", "Probably good or bad."]

#from A3
def prepare_text(input_string):
    
    """Makes the input all lower case and removes punctuation
    
    Parameters
    ----------
    input_string: string
        String to make lower case and remove punctuation
    
    Returns
    -------
    output: string
        Lower case and no punctuation string
    """
    out_list = []
    temp_string = " "
    temp_string = input_string.lower()
    out_list = temp_string.split()
    
    return out_list

#from A3
def end_chat(input_string):
    
    """Ends the chatbot interaction
    
    Parameters
    ----------
    input_string: string
        String that ends conversation with chatbot
    
    Returns
    -------
    output: none
        Just ends chat with chatbot
    """
    
    if "quit" in input_string:
        out = True
    else:
        out = False
        
    return out

#made my own version of function from A3 that makes lists into strings
def list_to_string(input_list):
    
    """Makes a list into a string
    
    Parameters
    ----------
    input_list: list
        The list that will be turned into a string.
    
    Returns
    -------
    output: string
        The string that comes from the list that was the input
    """
    
    new_string = " "
    new_string = new_string.join(input_list)
    return new_string

#will combine the three lists of movies to display to user
def list_concatenator(list1, list2, list3):
    
    """Adds three lists together and makes them a string
    
    Parameters
    ----------
    list1: list
        List to add with list2 and list3
       
    list2: list
        List to add with list1 and list3
        
    list3: list
        List to add with list1 and list2
    
    separator: string
        String that will go between list1, list2, and list3
    
    Returns
    -------
    output: string
        String that has list1, list2, and list3 with the seperator between each item
    """
    
    new_list = list1 + list2 + list3
    output = list_to_string(new_list)
    
    return output

#will print out an error message when wrong input is given to RateBot
def error_message():
    
    """Error message that is printed when incorrect movie is inputed by user
    
    Parameters
    ----------
    none
    
    Returns
    -------
    output: string
        Message that will indicate user that their input was incorrect.
    """
    
    error_msg = "This movie does not exists in my database. Please try the another one."
    
    return error_msg


#main function to run RateBot
def activate_ratebot():
    """Main function that will run RateBot"""

    #Greeting that RateBot gives to user
    print(greeting)
    print(starter_sentence + "\n" + list_concatenator(good_movies, bad_movies, never_seen))
    print(goodbye)
    
    #makes the list of movies into string
    good_movies_string = list_to_string(good_movies)
    bad_movies_string = list_to_string(bad_movies)
    never_seen_string = list_to_string(never_seen)
    
    #takes the strings of movies and prepares it to be used by RateBot
    prepared_good_movies = prepare_text(good_movies_string)
    prepared_bad_movies = prepare_text(bad_movies_string)
    prepared_never_seen = prepare_text(never_seen_string)
    
    
    chat = True
    
    while chat:
        
        #Takes in the input from the user
        msg = input("")
        out_msg = None
        
        #Prepares the input to pass through chatbot functions
        msg = prepare_text(msg)
        msg = list_to_string(msg)
        msg = msg.replace(" ", "")
        
        #Checks input to see if user ends chat
        if end_chat(msg):
            
            out_msg = "Have a good day!"
            chat = False
        
        #will answer the rating of the movie that the user gave to RateBot
        if not out_msg:
            
            if msg in prepared_good_movies:
                out_msg = random.choice(good_responses)
                
            elif msg in prepared_bad_movies:
                out_msg = random.choice(bad_responses)
             
            elif msg in prepared_never_seen:
                out_msg = random.choice(unknown_responses)
                
            else:
                out_msg = error_message()
                
            
        print(out_msg)
        
        
        
        
        