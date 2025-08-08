from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

# Encode the target
le = LabelEncoder()
df['RiskLevelEncoded'] = le.fit_transform(df['RiskLevel'])

# Define features and target
X = df.drop(columns=['RiskLevel', 'RiskLevelEncoded'])
y = df['RiskLevelEncoded']

# Impute missing values using mean strategy
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = LogisticRegression(multi_class='multinomial', max_iter=1000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
