import csv
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import re
from sklearn.linear_model import LogisticRegression

# Part 1: Process data, use MultinomialNB example using CountVectorizer
# Part 2: Use more baselines: Logistic Regression, XGBoost, and MultinomialNB and use TfidfVectorizer
# Part 3: Finally add a new feature to our model, review length, to see if this improves our model

def show_label_balance(y):    
    values = y.value_counts()
    print(values)
    print("Percent true " +  str(values[1]/(values[1]+values[0])))
    print("Percent false " + str(values[0]/(values[1]+values[0])))
    
    plt.clf()
    display = ["Spam","Ham"]
    plt.bar(display, values, align='center', label='Labels')
    plt.xticks(display,display)
    plt.ylim(ymin=900,ymax=1050)
    plt.ylabel('Frequency')
    plt.xlabel('Classification')
    plt.title('Data Distribuation')
    plt.legend()
    plt.show()
   
def data_split(X,y): 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,shuffle=True)
   
    return X_train, X_test, y_train, y_test

def vector_data(X_train): 
    vectorizer = CountVectorizer(ngram_range = (1, 1),lowercase=True,token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b' ,stop_words='english'))
    X_train = vectorizer.fit_transform(X_train)
    return X_train,vectorizer    

def model_fit_predict_and_results(X_train,y_train,X_test,y_test,vectorizer):
    #clf = MultinomialNB()
    clf = LogisticRegression(random_state=0, solver='lbfgs') #MultinomialNB()
    clf = clf.fit(X_train, y_train)
    
    X_test = vectorizer.transform(X_test)
    results = clf.predict(X_test)
    print("Our MultinomialNB model")
    print(accuracy_score(y_test, results))
   
    
def get_data_library(myList):
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


def get_data_no_library(myList):
    X = []
    y = []
    i = -1
    for csv_file in myList:
        with open(csv_file, newline="\n") as csv_file_open:
            csv_reader = csv.reader(csv_file_open, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
            csv_reader = iter(csv_reader)
            next(csv_reader)
            for row in csv_reader:
                i = -1
                for item in row:
                    i+=1
                    if i == 0:
                        pass
                    elif i == 1:
                        pass
                    elif i == 2:
                        pass
                    elif i == 3:
                        item = re.sub("[^a-zA-Z ]+", "", item)
                        item = item.lower()
                        X.append(item)
                    elif i == 4:
                        y.append(int(item))
    return X,y

def main():
    #Files
    myList = ["Youtube01-Psy.csv","Youtube02-KatyPerry.csv","Youtube03-LMFAO.csv","Youtube04-Eminem.csv","Youtube05-Shakira.csv"]
    #Comment out the slower way
    #X,y= get_data_no_library(myList)
    X,y= get_data_library(myList)
    X_train, X_test, y_train, y_test = data_split(X,y)
    X_train,vectorizer = vector_data(X_train)
    model_fit_predict_and_results(X_train,y_train,X_test,y_test,vectorizer)

if __name__ == "__main__":
    main()


