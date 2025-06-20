import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Page config
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="🏢",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem 3rem;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    label {
        font-weight: 600;
        color: #34495e;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🏢 Employee Attrition Prediction Dashboard")
st.markdown(
    """
    <p style="font-size:18px; color:#555;">
    Predict whether an employee is likely to leave the company based on their profile details.
    Fill the form below and click <b>Predict Attrition</b>.
    </p>
    """,
    unsafe_allow_html=True,
)

# Load and preprocess data
@st.cache_data
def load_and_preprocess():
    df = pd.read_csv('employee.csv')
    for col in df.select_dtypes(include='object').columns:
        df[col] = LabelEncoder().fit_transform(df[col])
    return df

df = load_and_preprocess()

features = [
    'Age','BusinessTravel','DailyRate','Department','DistanceFromHome','Education',
    'EducationField','EmployeeCount','EmployeeNumber','EnvironmentSatisfaction','Gender',
    'HourlyRate','JobInvolvement','JobLevel','JobRole','JobSatisfaction','MaritalStatus',
    'MonthlyIncome','MonthlyRate','NumCompaniesWorked','OverTime','PercentSalaryHike',
    'PerformanceRating','RelationshipSatisfaction','StandardHours','StockOptionLevel',
    'TotalWorkingYears','TrainingTimesLastYear','WorkLifeBalance','YearsAtCompany',
    'YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager'
]
X = df[features]
y = df['Attrition']

# Train/test split & model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(solver='liblinear', max_iter=1000)
model.fit(X_train, y_train)

# Input form layout
st.header("Enter Employee Details for Prediction")

numeric_features = [col for col in features if str(df[col].dtype) in ['int64', 'float64']]
categorical_features = [col for col in features if col not in numeric_features]

user_input = {}

with st.form("employee_form"):
    st.subheader("Numeric Features")
    cols = st.columns(3)
    for i, col in enumerate(numeric_features):
        min_val = int(df[col].min())
        max_val = int(df[col].max())
        default_val = int(df[col].median())
        user_input[col] = cols[i % 3].number_input(
            label=col.replace('_', ' '),
            min_value=min_val,
            max_value=max_val,
            value=default_val,
            step=1
        )
    
    st.subheader("Categorical Features")
    cols_cat = st.columns(2)
    for i, col in enumerate(categorical_features):
        unique_vals = list(df[col].unique())
        user_input[col] = cols_cat[i % 2].selectbox(
            label=col.replace('_', ' '),
            options=unique_vals,
            index=0
        )
    
    submitted = st.form_submit_button("Predict Attrition")

if submitted:
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.markdown(
        f"""
        <div style="background-color:#dff0d8; padding:15px; border-radius:8px; margin-top:20px; color: black;">
            <h3>Prediction: {'Will Leave' if prediction == 1 else 'Will Stay'}</h3>
            <p>Probability of Leaving: <b>{probability*100:.2f}%</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Show model performance
    st.subheader("Model Performance on Test Set")
    y_pred = model.predict(X_test)
    st.write(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    st.text(classification_report(y_test, y_pred))

# Show raw data option
if st.checkbox("Show Raw Data"):
    st.dataframe(df)
