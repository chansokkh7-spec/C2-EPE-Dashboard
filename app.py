import streamlit as st
import pandas as pd

# 1. Theme Configuration
st.set_page_config(page_title="C2-EPE Master System", layout="wide")

# Custom CSS for Premium Branding (Navy Blue & Gold)
st.markdown("""
    <style>
    .stApp {
        background-color: #001f3f;
    }
    
    /* Global Gold Text */
    * {
        color: #D4AF37 !important;
        font-family: 'Arial', sans-serif;
    }

    /* Gradient Gold Titles */
    h1, h2, h3 {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
    }

    /* Premium Button Style */
    .stButton>button {
        background: linear-gradient(45deg, #BF953F, #FCF6BA, #AA771C);
        color: #001f3f !important;
        font-weight: bold;
        border: 1px solid #FCF6BA;
        border-radius: 10px;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 20px #FCF6BA;
        transform: scale(1.02);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #001a33;
        border-right: 2px solid #D4AF37;
    }

    /* Metric Cards Styling */
    div[data-testid="stMetricValue"] {
        color: #FCF6BA !important;
        font-size: 35px;
    }
    
    /* Table Styling */
    .stTable {
        background-color: #001a33;
        border: 1px solid #D4AF37;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Navigation
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>C2-EPE ACADEMY</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FCF6BA;'><i>Mastery & Excellence</i></p>", unsafe_allow_html=True)
    st.write("---")
    
    menu = st.radio("Management Menu:", [
        "📊 Dashboard",
        "📂 Student Database",
        "💰 Finance & Sales",
        "📚 GEP Content",
        "🤖 AI & Automation",
        "📈 Marketing & Strategy",
        "📜 Certification"
    ])
    
    st.write("---")
    st.markdown("<p style='text-align: center;'>Prepared by<br><b>CHAN Sokhoeurn, C2/DBA</b></p>", unsafe_allow_html=True)

# 3. Content Logic
# --- 1. Dashboard ---
if menu == "📊 Dashboard":
    st.title("🏆 Executive Master Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", "1,250", "+15%")
    col2.metric("Total Revenue", "$18,500", "+8%")
    col3.metric("GEP Volumes", "9 Vols", "Active")
    col4.metric("AI Tasks", "154", "Automated")
    
    st.write("---")
    st.write("### 🔑 Key Performance Indicators")
    st.info("System is running optimally. All AI agents are online.")
    
    # Replaced chart with a structured summary table
    kpi_df = pd.DataFrame({
        'Category': ['Enrollment Growth', 'Retention Rate', 'Mastery Completion', 'Courseware Progress'],
        'Status': ['+15% Quarterly', '92%', '85 Students', '80% Total']
    })
    st.table(kpi_df)

# --- 2. Student Database ---
elif menu == "📂 Student Database":
    st.title("📂 Student Database & Skill Passport")
    st.text_input("Search Student ID or Name...")
    df = pd.DataFrame({
        'Student ID': ['C2-001', 'C2-002', 'C2-003'],
        'Name': ['Sokha', 'Bora', 'Davy'],
        'Level': ['C2 Mastery', 'A2 Flyers', 'B1 Intermediate'],
        'Skill Passport': ['95%', '45%', '70%']
    })
    st.table(df)

# --- 3. Finance & Sales ---
elif menu == "💰 Finance & Sales":
    st.title("💰 Finance & Sales Tracking")
    st.write("### 💵 Revenue Breakdown")
    
    # Replaced Bar chart with a clean Summary Table
    finance_df = pd.DataFrame({
        'Revenue Stream': ['Tuition Fees', 'GEP Book Sales (Vol 1-9)', 'Educational Consulting'],
        'Current Month': ['$12,000', '$4,500', '$2,000'],
        'Target': ['$10,000', '$5,000', '$1,500']
    })
    st.table(finance_df)
    
    st.success("Financial Target reached for Educational Consulting.")

# --- 4. GEP Content ---
elif menu == "📚 GEP Content":
    st.title("📚 GEP Content Production")
    st.info("Focusing on Volume 2 (A2) and Volume 8-9 (Mastery)")
    st.checkbox("Content Draft: Volume 2 (Completed)")
    st.checkbox("Content Draft: Volume 8 (In-Progress)")
    st.checkbox("Content Draft: Volume 9 (Planning)")
    if st.button("Save Status"):
        st.success("Content Status Updated Successfully!")

# --- 5. AI & Automation ---
elif menu == "🤖 AI & Automation":
    st.title("🤖 AI & Automation Hub")
    st.selectbox("Select AI Agent:", ["GEP Lesson Creator", "Auto-Grader", "Customer Support Bot"])
    st.button("Execute AI Process")

# --- 6. Marketing & Strategy ---
elif menu == "📈 Marketing & Strategy":
    st.title("📈 Blue Ocean Strategy & Marketing")
    st.text_area("Strategic Notes:", value="Focus on Early Specialization & Medical English integration.")
    st.slider("Ad Campaign Reach", 0, 10000, 5000)

# --- 7. Certification ---
elif menu == "📜 Certification":
    st.title("📜 Certification & Digital ID")
    st.selectbox("Certificate Type:", ["Flyers Master Certificate", "C2 Mastery Certificate", "Digital Student ID"])
    if st.button("✨ Generate Digital Document"):
        st.balloons()
        st.success("Premium Gold Document Generated!")

# 4. Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #D4AF37;'><b>© 2026 C2-EPE ACADEMY | SYSTEM VERSION 2.2</b></p>", unsafe_allow_html=True)
