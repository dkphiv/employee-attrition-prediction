def preprocess_data(df):
    # Zielvariable
    y = df["Attrition"].map({"Yes": 1, "No": 0})
    
    # Features
    X = df.drop("Attrition", axis=1)
    
    # Encoding
    X = pd.get_dummies(X)
    
    return X, y
