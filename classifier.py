import nltk
import random
from collections import defaultdict
from unidecode import unidecode
from nltk.corpus import jeita

numChars = 3

def createTupleDict(w,n=2):
    d = defaultdict(int)
    if len(w)<n:
        return d
    if not w.isalpha():
        return d
    for i in range(0,len(w)-(n-1)):
        d[w[i:i+n]] = 1
    return d


def createData():
    spwords = [unidecode(a.lower()) for a in set(nltk.corpus.cess_esp.words()) if len(a)>3]
    enwords = [a.lower() for a in set(nltk.corpus.brown.words()) if len(a)>3]
    jpwords = [unidecode(a) for a in jeita.words() if (len(unidecode(a)) and unidecode(a)[0].islower())]
    jpwords = [a for a in set(jpwords) if len(a)>3]
    # minLen = min(len(enwords), len(spwords), len(jpwords))

    featuresets = \
        [(createTupleDict(w,numChars),'English') for w in enwords] + \
        [(createTupleDict(w,numChars),'Spanish') for w in spwords] + \
        [(createTupleDict(w,numChars),'Japanese') for w in jpwords]

    random.shuffle(featuresets)

    l=int(len(featuresets)*0.8)

    training_set = featuresets[:l]
    testing_set = featuresets[l:]
    return (training_set, testing_set)


def trainData():
    print("This may take some time. Please be patient.")
    print("...\n"*3)
    print("Preparing feature sets...")
    (training_set, testing_set) = createData()
    print("Training the classifier ...")
    print("...\n"*3)
    global classifier
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    accuracy = nltk.classify.accuracy(classifier, testing_set)
    print("Trained with",accuracy,"percent accuracy on testing set")
    print("...\n"*3)
    print("To classify any word, say 'suyaki', type:\tclassifier.classifyWord('suyaki')")
    return classifier

def classifyWord(w):
    try:
        return classifier.classify(createTupleDict(w,numChars))
    except NameError:
        print("You need to train the classifier first like so:")
        print("classifier.trainData()")
