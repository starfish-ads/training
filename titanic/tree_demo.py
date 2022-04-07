# # メモ
# こちらを参考に
# https://www.codexa.net/kaggle-titanic-beginner/


# データの型､欠損値､カラム名
# train.info()

# 行列数
# print(train.shape)

# 統計量情報
# print(train.describe())
# -------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import plot_tree


# データフレームの欠損数を確認する関数
def check_missing_table(df):
    cnt_missing_values = df.isnull().sum()
    missing_percent = 100 * cnt_missing_values / len(df)

    missing_table = pd.concat([cnt_missing_values, missing_percent], axis='columns')
    missing_table = missing_table.rename(
        columns={0 : '欠損数', 1 : '%'}
    )

    return missing_table


def main():
    # 必要ファイルのインポート
    train = pd.read_csv(r"C:\myRepository\kaggle\Titanic\train.csv")
    test = pd.read_csv(r"C:\myRepository\kaggle\Titanic\test.csv")

    # # トレーニングデータ
    # 欠損値の補完
    train["Age"] = train["Age"].fillna(train["Age"].median())
    train["Embarked"] = train["Embarked"].fillna("S")

    # カテゴリカルデータの文字列 → 数字
    train["Sex"] = train["Sex"].replace("male", 0)
    train["Sex"] = train["Sex"].replace("female", 1)
    train["Embarked"] = train["Embarked"].replace("S", 0)
    train["Embarked"] = train["Embarked"].replace("C", 1)
    train["Embarked"] = train["Embarked"].replace("Q", 2)

    # # テストデータ
    # 欠損値の補完
    test["Age"] = test["Age"].fillna(test["Age"].median())
    test["Fare"] = test["Fare"].fillna(test["Fare"].median())

    # カテゴリカルデータの文字列 → 数字
    test["Sex"] = test["Sex"].replace("male", 0)
    test["Sex"] = test["Sex"].replace("female", 1)
    test["Embarked"] = test["Embarked"].replace("S", 0)
    test["Embarked"] = test["Embarked"].replace("C", 1)
    test["Embarked"] = test["Embarked"].replace("Q", 2)

    # 分析に不要な列の削除
    del train['Name']
    del train['Ticket']
    del train['Cabin']

    del test['Name']
    del test['Ticket']
    del test['Cabin']

    decision_tree(train, test)


def decision_tree(train, test):
    # 目的変数の取得
    target = train["Survived"].values
    # 説明変数の取得
    # train_features = train[["Pclass", "Sex", "Age", "Fare"]].values
    # test_features = test[["Pclass", "Sex", "Age", "Fare"]].values

    train_features = train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values
    test_features = test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values

    # 決定木の作成
    my_tree = tree.DecisionTreeClassifier()
    max_depth = 10
    min_samples_split = 5
    my_tree = tree.DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split, random_state=1)

    # # 決定木を可視化する
    # plt.figure(figsize=(12, 12))
    # clf = my_tree.fit(train, test)
    # plot_tree(clf, feature_names=train.columns, filled=True, rounded=True)
    # plt.show()

    
    # 決定木に目的変数と説明変数をセット
    my_tree = my_tree.fit(train_features, target)

    # 決定木にテストデータを適応
    my_prediction = my_tree.predict(test_features)
    print(my_prediction)

    # 乗客IDを取得して､生存予想をセット
    PassengerId = np.array(test["PassengerId"]).astype(int)
    my_solution = pd.DataFrame(my_prediction, PassengerId, columns=["Survived"])
    my_solution.to_csv("kaggle/Titanic/output.csv", index_label=["PassengerId"])


main()