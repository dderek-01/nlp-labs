
def make_tokens(input_text):
    
    """
    Take an input text, split it into tokens, find the
    token's shape, make a feature
    vector with the token itself and its shape, return
    a list of all token feature vectors found in the input.
    :param input_text: A character string containing spaces
    :return: A list of token feature vectors (token, shape).
        Sample output: [('a', 'alpha'), ('7', 'digit'), ('A27', 'alnum')]
    """
    
    # Now it's up to the split_tokes function to decide what a token is.
    # List comprehension creates a list by extracting elements from
    # an iterable object, in this case Python automatically converts the
    # split_tokens function into an iterable object because it uses the "yield" statement:
    
    tokens = [token for token in split_tokens(input_text)]
    return map(make_token_feature_vector, tokens)


def make_token_feature_vector(token):
    
    """
    Given a token, extract its shape and return a
    vector with the token itself and its shape
    :param token: A character string
    :return: A tuple (token, shape)
    """
    
    if token.isalpha():
        return (token, "alpha")
    elif token.isdigit():
        return (token, "digit")
    elif token.isalnum():
        return (token, "alnum")
    elif token in ",:;":  
        return (token, "punctuation")
    elif token in ".!?":  
        return (token, "sentence_end")
    elif token == "\n":  
        return (token, "paragraph_end")
    else:
        return (token, "other")



def split_tokens(input_text):
    
    """
    This function decides how to delimit a token. It takes an input
    string, iterates over it character by character; it collects
    constituent characters in the output token; punctuation characters
    are considered delimiters therefore become tokens of their own; the
    space character is removed from tokens. Yield each found token at
    a time.
    :param input_text: A character string containing a mix of text and delimiter characters.
    :yield A character string which is either free from delimiters or
        is a delimiter itself.
    """
    
    # First decide what characters delimit a token:
    DELIMITERS = ",:!?.\n"
    
    token = ""
    for char in input_text:
        
        if char in DELIMITERS:  # test if the input character is a delimiter (substring presence)
            
            # Character strings, lists, etc, have a logical truth value in Python;
            # an empty string is False, if it has characters it is True.
            
            if not token:  # same as token == ""
                yield char
            else:
                
                # Return token to the calling program, but next time this function
                # is called, continue from
                # the next statement rather than from the beginning of the function:
                
                yield token  # After yielding control to the calling program,
                             # this function will execute the next statement:
                token = ""  # Pick up execution from here.
                yield char
        elif char == " ":
            if token:  # same as token != ""
                yield token
                token = ""
        else:
            token += char
            
sample_text = "This is a sample sentence01 showing 7 different token types: alphabetic, numeric, alphanumeric, Title, UPPERCASE, CamelCase and punctuation!\nSentences like that should not exist. They're too artificial.\nA REAL sentence looks different. It has flavour to it. You can smell it; it's like Pythonic code, you know?\nHave you heard of 'code smell'? Google it if you haven't."            
noone = "expects the Spanish Inquisition"

if __name__ == "__main__":
    for token in make_tokens(sample_text):
        print(token)
