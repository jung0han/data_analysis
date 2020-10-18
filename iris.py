import pandas as pd
 
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
 
if __name__ == '__main__':
    iris = datasets.load_iris()
    print('아이리스 종류 :', iris.target_names)
    print('target : [0:setosa, 1:versicolor, 2:virginica]')
    print('데어터 수 :', len(iris.data))
    print('데이터 열 이름 :', iris.feature_names)
 
    # iris data Dataframe으로
    data = pd.DataFrame(
        {
            'sepal length': iris.data[:, 0],
            'sepal width': iris.data[:, 1],
            'petal length': iris.data[:, 2],
            'petal width': iris.data[:, 3],
            'species': iris.target
        }
    )
    print(data.head())
 
    x = data[['sepal length', 'sepal width', 'petal length', 'petal width']]
    y = data['species']
 
    # 테스트 데이터 30%
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    print(len(x_train))
    print(len(x_test))
    print(len(y_train))
    print(len(y_test))
 
    # 학습 진행
    forest = RandomForestClassifier(n_estimators=100)
    forest.fit(x_train, y_train)
 
    # 예측
    y_pred = forest.predict(x_test)
    print(y_pred)
    print(list(y_test))
 
    # 정확도 확인
    print('정확도 :', metrics.accuracy_score(y_test, y_pred))