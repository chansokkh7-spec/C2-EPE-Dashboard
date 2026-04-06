import streamlit as st
import pandas as pd
import plotly.express as px

# 1. កំណត់ការរចនា (Page Configuration)
st.set_page_config(page_title="C2-EPE Academy | Master Dashboard", layout="wide")

# Custom CSS សម្រាប់អក្សរពណ៌មាសទាំងស្រុង (All Gold Text)
st.markdown("""
    <style>
    /* ផ្ទៃខាងក្រោយមេ */
    .stApp {
        background-color: #001f3f;
    }
    
    /* កំណត់ឱ្យរាល់អក្សរទាំងអស់ចេញពណ៌មាស */
    html, body, [class*="st-"] {
        color: #D4AF37 !important;
        font-family: 'Kantumruy Pro', sans-serif;
    }

    /* ចំណងជើងធំៗឱ្យមានពន្លឺមាស Gradient */
    h1, h2, h3 {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
    }

    /* ការរចនាប៊ូតុងពណ៌មាស */
    .stButton>button {
        background: linear-gradient(45deg, #BF953F, #FCF6BA, #AA771C);
        color: #001f3f !important;
        font-weight: bold;
        border: 2px solid #FCF6BA;
        border-radius: 8px;
    }
    
    /* ការរចនា Sidebar */
    [data-testid="stSidebar"] {
        background-color: #001a33;
        border-right: 2px solid #D4AF37;
    }

    /* ការរចនាតារាង (Dataframe) ឱ្យមានអក្សរពណ៌មាស */
    .stDataFrame, [data-testid="stTable"] {
        color: #D4AF37 !important;
        background-color: #001f3f;
    }

    /* Metric Label (អក្សរតូចលើលេខ) */
    [data-testid="stMetricLabel"] {
        color: #FCF6BA !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. របារចំហៀង (Sidebar Navigation)
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>C2-EPE Academy</h2>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("មឺនុយគ្រប់គ្រង:", 
        ["📊 Dashboard", "📂 Student Database", "💰 Finance", "📚 GEP Content"])
    st.write("---")
    st.markdown("<p style='text-align: center;'>Prepared by<br><b>CHAN Sokhoeurn, C2/DBA</b></p>", unsafe_allow_html=True)

# 3. ទិន្នន័យគំរូ
df = pd.DataFrame({
    'Student Name': ['Sokha', 'Bora', 'Davy'],
    'Level': ['Flyers Master', 'A2', 'C2 Mastery'],
    'Status': ['Paid', 'Pending', 'Paid']
})

# --- ការបង្ហាញតាមមឺនុយ ---
if menu == "📊 Dashboard":
    st.title("🏆 C2-EPE Master Dashboard")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", "1,250", "+12%")
    col2.metric("Revenue", "$18,500", "+5%")
    col3.metric("Course Volumes", "9 Vols", "Active")

    st.write("### 📈 Student Growth")
    chart_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar'], 'Students': [800, 1000, 1250]})
    st.line_chart(chart_data.set_index('Month'))

elif menu == "📂 Student Database":
    st.title("📂 Student Information")
    st.dataframe(df)
    if st.button("Generate Passport"):
        st.success("Digital Passport Created!")

elif menu == "💰 Finance":
    st.title("💰 Financial Overview")
    st.write("គ្រប់គ្រងចំណូលពី GEP Volumes និង Tuition Fees")
    st.bar_chart(pd.DataFrame({'Revenue': [5000, 7000, 18500]}))

elif menu == "📚 GEP Content":
    st.title("📚 GEP Courseware")
    st.write("ស្ថានភាពផលិតសៀវភៅ Volume 2 (A2) និង Volume 8-9 (C2)")
    st.checkbox("Volume 2: Completed")
    st.checkbox("Volume 8: In Progress")
    st.checkbox("Volume 9: Planning")

# 4. Footer
st.markdown("<br><hr><p style='text-align: center;'>© 2026 C2-EPE Academy | Excellence in Education</p>", unsafe_allow_html=True)
