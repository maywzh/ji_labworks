from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, log_loss
from eval_metrics import all_metrics
from collections import defaultdict
from scipy.sparse import load_npz
from datetime import datetime
from eval_metrics import avgstd
from dataio import load_folds
import argparse
import numpy as np
import pandas as pd
import os.path
import math
import glob
import time
import json
import sys
import yaml


parser = argparse.ArgumentParser(description='Run LR')
parser.add_argument('X_file', type=str, nargs='?', default='dummy')
parser.add_argument('--test', type=str, nargs='?', default='')
options = parser.parse_args()


# SENSITIVE_ATTR = "school_id"
SENSITIVE_ATTR = "timestamp"

# df = pd.read_csv("data/openlab-train/needed.csv")  # Should fix this
# df["weight"] = df.groupby(SENSITIVE_ATTR).user_id.transform('nunique')
# df["weight"] = df.groupby(SENSITIVE_ATTR).user_id.transform('count')
# df["weight"] = 1000 * (df[SENSITIVE_ATTR] % 2 == 1) + 1
# df["weight"] = 1
# df["weight"] = 1 / df["weight"]
# sys.exit(0)

FULL = False
X_file = options.X_file
folder = os.path.dirname(X_file)
y_file = X_file.replace('X', 'y').replace('npz', 'npy')

X = load_npz(X_file).tocsr()
nb_samples, _ = X.shape
y = np.load(y_file).astype(np.int32)
print(X.shape, y.shape)

# Know number of users
'''
with open(os.path.join(folder, 'config.yml')) as f:
    config = yaml.load(f)
    X_users = X[:, :config['nb_users']]
    print(X_users.shape)
    assert all(X_users.sum(axis=1) == 1)
    # sys.exit(0)
'''

# Are folds fixed already?
X_trains = {}
sample_weights = {}
y_trains = {}
X_tests = {}
y_tests = {}
FOLD = '50weak'

# folds = glob.glob(os.path.join(folder, 'folds/{}fold*.npy'.format(nb_samples)))
test_folds, valid_folds = load_folds(options)
if test_folds and not FULL:
    print(test_folds)
    for i, filename in enumerate(test_folds):
        i_test = np.load(filename)
        print('Fold', i, i_test.shape)
        i_train = list(set(range(nb_samples)) - set(i_test))
        X_trains[i] = X[i_train]
        y_trains[i] = y[i_train]
        X_tests[i] = X[i_test]
        y_tests[i] = y[i_test]
        # sample_weights[i] = np.array(df["weight"])[i_train]
        print('Weights', i)
        #weights_test[i] = np.array(df["weight"])[i_test]
elif FULL:
    X_trains[0] = X
    X_tests[0] = X
    y_trains[0] = y
    y_tests[0] = y
    # sample_weights[0] = np.array(df["weight"])
else:
    print('No folds so train test split')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        shuffle=False)
    X_trains[0] = X_train
    X_tests[0] = X_test
    y_trains[0] = y_train
    y_tests[0] = y_test
    

results = defaultdict(list)
predictions = []
for i in X_trains:
    X_train, X_test, y_train, y_test = (X_trains[i], X_tests[i],
                                        y_trains[i], y_tests[i])
    model = LogisticRegression(solver='liblinear')  # Has L2 regularization by default
    dt = time.time()

    # weights_train[i] should contain the same value as sample_weights

    nb_samples = len(y_train)
    # nb_users = config['nb_users']
    # nb_groups = df[SENSITIVE_ATTR].nunique()
    
    """
    X_train_users = X_train[:, :config['nb_users']]
    nb_samples_per_user = X_train_users.sum(axis=0).A1
    nb_samples_per_user[nb_samples_per_user == 0] = 1
    print(X_train_users.shape)
    print(nb_samples_per_user.shape)
    print((X_train_users @ (1 / nb_samples_per_user)).shape)
    # sample_weights = np.ones(nb_samples)
    print(nb_samples / nb_users / nb_samples_per_user)
    sample_weights = X_train_users @ (nb_samples / nb_users / nb_samples_per_user)
    """
    
    model.fit(X_train, y_train)#nb_samples / nb_groups * sample_weights[i])

    print('[time] Training', time.time() - dt, 's')

    for dataset, X, y in [('Train', X_train, y_train),
                          ('Test', X_test, y_test)]:
        dt = time.time()
        y_pred = model.predict_proba(X)[:, 1]

        # Store predictions of the fold
        if dataset == 'Test':
            predictions.append({
                'fold': i,
                'pred': y_pred.tolist(),
                'y': y.tolist()
            })

        if len(y_pred) < 10:
            print(dataset, 'predict:', y_pred)
            print(dataset, 'was:', y)
        try:  # This may fail if there are too few classes
            nll = log_loss(y, y_pred)
            auc = roc_auc_score(y, y_pred)
        except ValueError:
            nll = auc = -1

        metrics = {'ACC': np.mean(y == np.round(y_pred)),
                   'NLL': nll,
                   'AUC': auc}
        for metric, value in metrics.items():
            results['{} {}'.format(dataset, metric)].append(value)
            print(dataset, metric, 'on fold {}:'.format(i), value)
        print('[time]', time.time() - dt, 's')

    np.save(os.path.join(folder, 'coef{}.npy'.format(i)), model.coef_)

print('# Final results')
for metric in results:
    print('{}: {}'.format(metric, avgstd(results[metric])))

iso_date = datetime.now().isoformat()
saved_results = {
    'predictions': predictions,
    'model': 'LR',
    'folds': FOLD
}
with open(os.path.join(folder, 'results-{}.json'.format(iso_date)), 'w') as f:
    json.dump(saved_results, f)

# df = pd.read_csv(os.path.join(folder, 'needed.csv'))
# indices = np.load(test_folds[0])
# test = df.iloc[indices]

# all_metrics(saved_results, test)
