import csv
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import re
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier


# Part 1: Process data, use MultinomialNB example using CountVectorizer
# Part 2: Use more baselines: Logistic Regression, XGBoost, and MultinomialNB and use TfidfVectorizer
# Part 3: Finally add a new feature to our model, review length, to see if this improves our model


def data_split(X,y): 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,shuffle=True)
    return X_train, X_test, y_train, y_test

def CountVectorizer_data(X_train): 
    #vectorizer = CountVectorizer(ngram_range = (1, 1),lowercase=True,token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b' ,stop_words='english')    
    vectorizer = CountVectorizer(ngram_range = (1, 1),lowercase=True)
    X_train = vectorizer.fit_transform(X_train)
    return X_train,vectorizer    

def TfidfVectorizer_data(X_train): 
    #vectorizer = TfidfVectorizer(ngram_range = (1, 1),lowercase=True,token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b' ,stop_words='english')
    vectorizer = TfidfVectorizer(ngram_range = (1, 1),lowercase=True) 
    X_train = vectorizer.fit_transform(X_train)
    return X_train,vectorizer    

def model_fit_predict_and_results(X_train,y_train,X_test,y_test,vectorizer,models,names):
    X_test = vectorizer.transform(X_test)
    for i,clf in enumerate(models):
        clf = clf.fit(X_train, y_train)
        results = clf.predict(X_test)
        print(names[i] + " accuracy " + str(accuracy_score(y_test, results)))
       
    
def get_data(myList):
    i = -1
    data = []
    myList = ["Youtube01-Psy.csv","Youtube02-KatyPerry.csv","Youtube03-LMFAO.csv","Youtube04-Eminem.csv","Youtube05-Shakira.csv"]
    for csv_file in myList:
        with open(csv_file, newline="\n") as csv_file_open:

            data.append(pd.read_csv(csv_file))
    data = pd.concat(data)
    X = data.CONTENT
    y = data.CLASS
    return X,y



def main():
    #Files
    myList = ["Youtube01-Psy.csv","Youtube02-KatyPerry.csv","Youtube03-LMFAO.csv","Youtube04-Eminem.csv","Youtube05-Shakira.csv"]
    #Comment out the slower way
    X,y= get_data(myList)
    X_train, X_test, y_train, y_test = data_split(X,y)
    
    #Bag of Words Model using Count Vectorizer
    models = [MultinomialNB(),LogisticRegression(random_state=0, solver='lbfgs'),GradientBoostingClassifier(n_estimators=500,max_depth=3)]
    names = ["MultinomialNB","LogisticRegression","GradientBoostingClassifier"]
    
    X_train_vect,vectorizer = CountVectorizer_data(X_train)
    model_fit_predict_and_results(X_train_vect,y_train,X_test,y_test,vectorizer,models,names)
    
    #Bag of Words Model using
    models = [LogisticRegression(random_state=0, solver='lbfgs'),GradientBoostingClassifier(n_estimators=500,max_depth=3)]
    
    names = ["LogisticRegression","GradientBoostingClassifier"]
    X_train_Tfidf,TfidfVectorizer = TfidfVectorizer_data(X_train)
    model_fit_predict_and_results(X_train_Tfidf,y_train,X_test,y_test,TfidfVectorizer,models,names)

if __name__ == "__main__":
    main()


