import cudf
import numpy as np

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

print(y)
