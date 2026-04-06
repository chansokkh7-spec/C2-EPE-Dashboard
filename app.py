import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Theme Configuration
st.set_page_config(page_title="C2-EPE Master System", layout="wide")

# Custom CSS for Premium Rounded Metric Boxes
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

    /* Custom Round Metric Box Design */
    [data-testid="stMetric"] {
        background: rgba(0, 26, 51, 0.8);
        border: 2px solid #D4AF37;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.3);
        text-align: center;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #001a33;
        border-right: 2px solid #D4AF37;
    }

    /* Premium Button Style */
    .stButton>button {
        background: linear-gradient(45deg, #BF953F, #FCF6BA, #AA771C);
        color: #001f3f !important;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Navigation
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>C2-EPE ACADEMY</h2>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("Management Menu:", ["📊 Dashboard", "📂 Student Database", "💰 Finance & Sales", "📚 GEP Content", "🤖 AI & Automation", "📈 Marketing & Strategy", "📜 Certification"])
    st.write("---")
    st.markdown("<p style='text-align: center;'>Prepared by<br><b>CHAN Sokhoeurn, C2/DBA</b></p>", unsafe_allow_html=True)

# 3. Content Logic
if menu == "📊 Dashboard":
    st.title("🏆 Executive Master Dashboard")
    
    # Rounded Metric Boxes
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="👥 Total Students", value="1,250", delta="+15%")
    col2.metric(label="💰 Total Revenue", value="$18,500", delta="+8%")
    col3.metric(label="📚 GEP Volumes", value="9 Vols", delta="Active")
    col4.metric(label="🤖 AI Tasks", value="154", delta="Automated")
    
    st.write("---")
    
    # Pie Chart
    st.write("### 🍕 Student Levels Distribution")
    pie_df = pd.DataFrame({
        'Level': ['C2 Mastery', 'A2 Flyers', 'B1 Intermediate', 'Other'],
        'Count': [85, 450, 315, 400]
    })
    fig_pie = px.pie(pie_df, values='Count', names='Level', 
                     color_discrete_sequence=['#BF953F', '#D4AF37', '#8A6E2F', '#5C4033'])
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#D4AF37")
    st.plotly_chart(fig_pie, use_container_width=True)

elif menu == "📂 Student Database":
    st.title("📂 Student Database")
    df = pd.DataFrame({
        'Student ID': ['C2-001', 'C2-002', 'C2-003'],
        'Name': ['Sokha', 'Bora', 'Davy'],
        'Level': ['C2 Mastery', 'A2 Flyers', 'B1 Intermediate'],
        'Skill Passport': ['95%', '45%', '70%']
    })
    st.table(df)

else:
    st.title(menu)
    st.info("Section under development with Premium Gold Theme.")

# 4. Footer
st.markdown("<br><hr><p style='text-align: center; color: #D4AF37;'><b>© 2026 C2-EPE ACADEMY | SYSTEM VERSION 2.3</b></p>", unsafe_allow_html=True)
