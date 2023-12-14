import cudf
import cuml
import numpy as np
from cuml import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load your time series data using cudf
# Replace this with your actual data loading method
# Assume 'data' contains your time series data
data = np.random.randn(1000, 1)  # Example random data
gdf = cudf.DataFrame({'value': data.flatten()})

# Prepare features and target columns for prediction
look_back = 10  # Number of past values to use as features for prediction
gdf['target'] = gdf['value'].shift(-1)  # Shift target column by one time step
for i in range(1, look_back + 1):
    gdf[f'feature_{i}'] = gdf['value'].shift(i)

# Drop rows with NaN due to shifting for target column
gdf.dropna(inplace=True)

# Split the data into features and target variable
X = gdf.drop(['value', 'target'], axis=1)
y = gdf['target']

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the SVR model from cuml
model = SVR()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate and print the Root Mean Squared Error (RMSE)
rmse = np.sqrt(mean_squared_error(y_test.to_array(), predictions))
print(f"Root Mean Squared Error (RMSE): {rmse}")
