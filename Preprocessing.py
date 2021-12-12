import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA


# Dataset for cross validation
def Load_mushroom_dataset():
    # loading mushoroom dataset from UCI
    path="https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
    df = pd.read_csv(path)
    column_names = ['class', 'cap shape', 'cap surface', 'cap color', 'bruised', 'odor', 'gill attachment', 'gill spacing',
               'gill size', 'gill color', 'stalk shape', 'stalk root', 'stalk surface above ring', 'stalk surface below ring',
               'stalk color above ring', 'stalk color below ring', 'veil type', 'veil color', 'ring number', 'ring type',
               'spore print color', 'population', 'habitat']
    df.columns = column_names

    x = df.copy(deep=True)
    x.drop(['class'], inplace=True, axis=1)

    x.drop(['veil type'], inplace=True, axis=1)   #column veil-type has the same value for all samples.So this is removed.
    y = df['class'].copy(deep=True)

    # Converting categorical features into binary values using get_dummies()
    x = pd.get_dummies(x)

    # Converting the categorical labels into integers
    label_Encoder = LabelEncoder()
    y = label_Encoder.fit_transform(y)

    # Applying PCA with 98% variance
    x_pca = x
    pca = PCA(n_components=0.98)
    sc = StandardScaler()
    x_pca = sc.fit_transform(x_pca)
    x_pca = pca.fit_transform(x_pca) # Reduced to 68 features.

    return x, y, x_pca


# Dataset split to check for the accuracies without cross validation
def Load_MushroomDataset_with_Splits():
    x, y, x_pca = Load_mushroom_dataset()
    # split the x and y
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
    # split the x_pca and y
    x_train_pca, x_test_pca, y_train_pca, y_test_pca = train_test_split(x_pca, y, test_size=0.20, random_state=42)

    return x_train, x_test, y_train, y_test, x_train_pca, x_test_pca, y_train_pca, y_test_pca


# Dataset split for Random Forest classifier with train test split
def Load_mushroom_dataset_RF():
    x_data, y_data, x_data_pca = Load_mushroom_dataset()
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.20, random_state=42)

    return x_train, x_test, y_train, y_test

