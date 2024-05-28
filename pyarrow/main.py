import pandas as pd
import pyarrow as pa

# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'score': [85.5, 90.0, 95.5]
}
df = pd.DataFrame(data)

# Convert to Arrow Table
table = pa.Table.from_pandas(df)
print(table)