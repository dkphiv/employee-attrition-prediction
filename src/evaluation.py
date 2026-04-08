from sklearn.metrics import classification_report

def evaluate_model(y_test, y_pred):
    print(classification_report(y_test, y_pred))