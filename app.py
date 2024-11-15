"""
Simple Falsk application to test out deploying application in the cloud
If you don't use the file name "app.py" then create an environment variable "FLASK_APP"
and set it to the value of your file that you want to be served up.
"""
# import re
from flask import Flask
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# create instance of the Flask object
app = Flask(__name__)

# decorator is used to connect URL endpoints with code in functions
# argument to @app.route() defines the URL's path component, which is root in this case
@app.route("/")
def home():
    """
    f() is wrapped with a decorator and defines what should be executed if
    the defined URL endpoint is requested by the user
    We have attached this function to the route ("/") which is home page
    """
    return "Hello, Flask!"


@app.route("/about/<name>")
def about(name):
    """
    decorator argument "/about/<name>" defines the endpoint "/about/" that can
    accept any additional value. The identifier within the angled brackets
    defines a variable that is passed to the function and can be used in the code

    Always filter user-provided information to avoid attacks on the app. If you use
    Templates then Flask does this for you automatically
    """

    # the following code has been commented out so that a new feature can be added
    # to ensure secure values are passed to the function.

    # filter the name argument to ensure safe letters are passed into function
    # filtered_arg = re.match("[a-zA-Z, . ']+", name)

    # as long as filtered_arg is not None then get the data
    #if filtered_arg:
    #    clean_arg = filtered_arg.group(0)
    #else:
    #    clean_arg = "Something went wrong"

    clean_arg = name

    # send what the user sent to the end point to word frequency function
    # a dictionary is returned
    return_content = word_frequency(clean_arg.lower())

    # send the top used tokens that the user sent back to the browser
    return return_content

def word_frequency(content):
    """
    function takes the argument and generates the frequency count of the words
    """
    # tokenize the text
    words = word_tokenize(content)

    stop_words = set(stopwords.words("english"))
    punctuation = [",", " ", ".", "!", ":", ";"]
    
    # get rid of punctuation (could use RE, going to use list comprehension)
    # could also get rid of 1 character tokens
    words = [w for w in words if w not in punctuation]

    # get rid of stop words, using a loop instead of list comprehension 
    filtered_sentence = []
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)

    # create a frequency distribution
    freq_dist = nltk.FreqDist(filtered_sentence)

    # Return the distribution
    return freq_dist.most_common()
