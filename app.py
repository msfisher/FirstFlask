"""
Simple Falsk application to test out deploying application in the cloud
If you don't use the file name "app.py" then create an environment variable "FLASK_APP"
and set it to the value of your file that you want to be served up.
"""
# import re
from flask import Flask, request, render_template
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download('stopwords')

# create instance of the Flask object
app = Flask(__name__)

# decorator is used to connect URL endpoints with code in functions
# argument to @app.route() defines the URL's path component, which is root in this case
@app.route("/", methods=['GET'])
def home():
    """
    f() is wrapped with a decorator and defines what should be executed if
    the defined URL endpoint is requested by the user
    We have attached this function to the route ("/") which is home page
    """
    return render_template("index.html")


@app.route("/read_form", methods=["POST"])
def read_form():
    """
    Always filter user-provided information to avoid attacks on the app. If you use
    Templates then Flask does this for you automatically
    """
    # get the forma data
    data = request.form

    # filter the user data to ensure safe letters are passed into function
    # filtered_text = re.match("[a-zA-Z, . ']+", data['textSubmit'])

    # as long as filtered_text is not None then we can use the data
    #if filtered_text:
    #    clean_text = filtered_arg.group(0)
    #else:
    #    clean_text = "Something went wrong"

    clean_text = data['textSubmit']

    # send what the user sent to the end point to word frequency function
    # a dictionary is returned
    return_content = word_frequency(clean_text.lower())

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
