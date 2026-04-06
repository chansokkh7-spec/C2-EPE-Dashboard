import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="C2-EPE Master System", layout="wide")

# 2. Premium CSS (Navy Blue & Gold)
st.markdown("""
    <style>
    .stApp { background-color: #001f3f; }
    * { color: #D4AF37 !important; font-family: 'Arial', sans-serif; }
    
    /* Metrics Style (Rounded Boxes) */
    [data-testid="stMetric"] {
        background: rgba(0, 26, 51, 0.8);
        border: 2px solid #D4AF37;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.3);
    }

    /* Sidebar Style */
    [data-testid="stSidebar"] { background-color: #001a33; border-right: 2px solid #D4AF37; }

    /* Premium Table Styling */
    .gold-table {
        width: 100%;
        border-collapse: collapse;
        border: 2px solid #D4AF37;
        border-radius: 15px;
        overflow: hidden;
        margin-top: 20px;
    }
    .gold-table th {
        background-color: #D4AF37;
        color: #001f3f !important;
        padding: 15px;
        text-align: left;
    }
    .gold-table td {
        border: 1px solid #D4AF37;
        padding: 12px;
        background-color: rgba(0, 31, 63, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Menu
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>C2-EPE ACADEMY</h2>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("Management Menu:", ["📊 Dashboard", "📂 Student Database", "💰 Finance & Sales", "📚 GEP Content", "🤖 AI & Automation", "📈 Marketing & Strategy", "📜 Certification"])
    st.write("---")
    st.markdown("<p style='text-align: center;'>Prepared by<br><b>CHAN Sokhoeurn, C2/DBA</b></p>", unsafe_allow_html=True)

# 4. Main Content Logic
if menu == "📊 Dashboard":
    st.title("🏆 Executive Master Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", "1,250", "+15%")
    col2.metric("Total Revenue", "$18,500", "+8%")
    col3.metric("GEP Volumes", "9 Vols", "Active")
    col4.metric("AI Tasks", "154", "Automated")
    
    st.write("---")
    st.write("### 🍕 Student Levels Distribution")
    pie_df = pd.DataFrame({'Level': ['C2 Mastery', 'A2 Flyers', 'B1 Intermediate', 'Other'], 'Count': [85, 450, 315, 400]})
    fig = px.pie(pie_df, values='Count', names='Level', color_discrete_sequence=['#BF953F', '#D4AF37', '#8A6E2F', '#5C4033'])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#D4AF37")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "📂 Student Database":
    st.title("📂 Student Database & Skill Passport")
    st.write("Professional tracking system for C2-EPE students.")
    
    # Student Data
    students = [
        {"ID": "C2-001", "Name": "Sokha", "Level": "C2 Mastery", "Passport": "95%"},
        {"ID": "C2-002", "Name": "Bora", "Level": "A2 Flyers", "Passport": "45%"},
        {"ID": "C2-003", "Name": "Davy", "Level": "B1 Intermediate", "Passport": "70%"}
    ]
    
    # Manual HTML Table for Premium Look
    table_html = f"""
    <table class="gold-table">
        <tr>
            <th>Student ID</th>
            <th>Name</th>
            <th>Level</th>
            <th>Skill Passport</th>
        </tr>
        {"".join([f"<tr><td>{s['ID']}</td><td>{s['Name']}</td><td>{s['Level']}</td><td>{s['Passport']}</td></tr>" for s in students])}
    </table>
    """
    st.markdown(table_html, unsafe_allow_html=True)
    
    st.write("")
    st.button("✨ Generate New Skill Passport")

else:
    st.title(menu)
    st.info("This section is ready for content integration.")

# 5. Footer
st.markdown("<br><hr><p style='text-align: center;'>© 2026 C2-EPE ACADEMY | SYSTEM VERSION 2.4</p>", unsafe_allow_html=True)
