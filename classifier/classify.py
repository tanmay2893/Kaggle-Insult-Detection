from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.feature_selection import SelectPercentile, f_classif,chi2
from sklearn.pipeline import Pipeline
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import ShuffleSplit
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.stem import SnowballStemmer
english_stemmer=SnowballStemmer('english')
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import f1_score
from sklearn.base import BaseEstimator

def grid_search_model(clf_factory, X, Y):
    X,Y=get_trains()
    cv = ShuffleSplit(n=len(X), n_iter=5, test_size=0.3, indices=True, random_state=0)
    param_grid = dict(vect__ngram_range=[(1, 1), (1, 2), (1, 3)],
    vect__min_df=[1, 2],
    vect__stop_words=[None, "english"],
    vect__smooth_idf=[False, True],
    vect__use_idf=[False, True],
    vect__sublinear_tf=[False, True],
    vect__binary=[False, True],
    )
    grid_search = GridSearchCV(clf_factory(),param_grid=param_grid,cv=cv,score_func=f1_score,verbose=10)
    grid_search.fit(X, Y)
    return grid_search.best_estimator_


class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedTfidfVectorizer,self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))
class Densifier(BaseEstimator):
    def fit(self, X, y=None):
        pass
    def fit_transform(self, X, y=None):
        return self.transform(X)
    def transform(self, X, y=None):
        return X.toarray()
def create_ngram_model():
    tfidf_ngrams = StemmedTfidfVectorizer(ngram_range=(1, 3),analyzer="word", binary=False,stop_words='english')
    clf = MultinomialNB(alpha=1.0,class_prior=None,fit_prior=True)
    selector = SelectPercentile(f_classif, percentile=4.4)
    pipeline = Pipeline([('vect', tfidf_ngrams), ('select',selector), ('densify',Densifier()), ('clf', clf)])
    return pipeline


def get_trains():
    data=open('../cleaning data/cleaning the sentences/cleaned_comments.csv','r').readlines()[1:]
    lines=len(data)
    features_train=[]
    labels_train=[]
    for i in range(lines):
        l=data[i].split(',')
        labels_train+=[int(l[0])]
        a=l[2]
        features_train+=[a]
    return features_train,labels_train
    
def train_model(clf_factory,features_train,labels_train):
    features_train,labels_train=get_trains()
    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features_train, labels_train, test_size=0.1, random_state=42)
    
    clf=clf_factory()
    clf.fit(features_train,labels_train)
    
    pred = clf.predict(features_test)
    accuracy = accuracy_score(pred,labels_test)
    return accuracy

X,Y=get_trains()
print train_model(create_ngram_model,X,Y)
#clf = grid_search_model(create_ngram_model, X, Y)
#print clf
