import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# --- Load your dataset ---
df = pd.read_csv(r"D:\Elina\ScrapingTimeZone-Data\ScrapingTimeZone-Data\Machine-Learning\Machine-Learning\Flight_Extra_Time.csv")

# --- Function to assign season from month ---
def get_season(month):
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    else:
        return 'fall'

# --- Add season column ---
df['season'] = df['month'].apply(get_season)

# --- Filter only rows where extra_time is known ---
df_known = df[(df['extra_time'].notna()) & (df['status'] != 'Missing Value')]
df_unknown = df[df['status'] == 'Missing Value']

# --- Columns for features ---
features = [
    'year', 'month', 'day', 'dep_time', 'sched_dep_time', 'dep_delay',
    'arr_time', 'sched_arr_time', 'arr_delay', 'carrier', 'flight',
    'origin', 'dest', 'air_time', 'distance', 'hour', 'minute',
    'status', 'season'
]

# --- Encode categorical features for modeling only ---
df_model = pd.concat([df_known, df_unknown])
df_encoded = df_model.copy()
le_dict = {}

categorical_cols = ['carrier', 'origin', 'dest', 'status', 'season']
for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])
    le_dict[col] = le

# --- Split encoded data ---
df_known_encoded = df_encoded[df_model['extra_time'].notna()]
df_unknown_encoded = df_encoded[df_model['extra_time'].isna()]

# --- Prepare training data ---
X = df_known_encoded[features]
y = df_known_encoded['extra_time']
X_missing = df_unknown_encoded[features]

# --- Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# --- Train Random Forest model ---
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- Evaluate model ---
r2 = model.score(X_test, y_test)
print(f"Model R^2 score: {r2:.2f}")

# --- Predict and update original DataFrame ---
predicted = model.predict(X_missing)
df.loc[df['status'] == 'Missing Value', 'extra_time'] = predicted
df.loc[df['status'] == 'Missing Value', 'status'] = 'Safe'

# --- Save updated dataset ---
df.to_csv("filled_flight_data.csv", index=False)
print("Saved updated dataset to 'filled_flight_data.csv'.")
