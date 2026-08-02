import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,classification_report

df = pd.read_csv("jobs_detailed.csv")

def label_job(title):
    title_lower = title.lower()
    if 'python' in title_lower or 'developer' in title_lower or 'engineer' in title_lower:
        return 0
    elif 'manager' in title_lower or 'director' in title_lower:
        return 1
    else:
        return 2

df['Category'] =df['Job_Title'].apply(label_job)
X = df['Job_Title'] + " " + df["Description"]
y = df['Category']

x_train , x_test , y_train , y_test = train_test_split(X, y , test_size=0.2 , random_state=42)
vectorizer = TfidfVectorizer(max_features=500)
x_train_vec = vectorizer.fit_transform(x_train)
x_test_vec = vectorizer.transform(x_test)

mlp = MLPClassifier(hidden_layer_sizes=(50 , 20) , max_iter=500 , random_state=42)

mlp.fit(x_train_vec,y_train)
y_pred = mlp.predict(x_test_vec)

accuracy = accuracy_score(y_test , y_pred)

print(f"Accuracy of Neural Network : {accuracy* 100:.2f}%\n")
print("Detailed Classification Report")
print(classification_report(y_test,y_pred , target_names=['Python/Data' , 'Management' , 'Other']))