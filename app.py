import streamlit as st
import pandas as pd
import plotly.express as px

# 1. កំណត់ការរចនាទូទៅ (Theme Settings)
st.set_page_config(page_title="C2-EPE Master System", layout="wide")

# Custom CSS សម្រាប់អក្សរពណ៌មាស និង Branding របស់ C2-EPE
st.markdown("""
    <style>
    /* ផ្ទៃខាងក្រោយមេ Navy Blue */
    .stApp {
        background-color: #001f3f;
    }
    
    /* កំណត់ឱ្យរាល់អក្សរទាំងអស់ចេញពណ៌មាស */
    * {
        color: #D4AF37 !important;
        font-family: 'Kantumruy Pro', sans-serif;
    }

    /* ចំណងជើងធំៗឱ្យមានពន្លឺមាស Gradient */
    h1, h2, h3 {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
    }

    /* ការរចនាប៊ូតុងពណ៌មាស Premium */
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
    
    /* ការរចនា Sidebar */
    [data-testid="stSidebar"] {
        background-color: #001a33;
        border-right: 2px solid #D4AF37;
    }

    /* ការរចនា Card Metric */
    div[data-testid="stMetricValue"] {
        color: #FCF6BA !important;
        font-size: 35px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. របារចំហៀង និងមឺនុយទាំង ៧ ផ្នែក
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>C2-EPE ACADEMY</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FCF6BA;'><i>Mastery & Excellence</i></p>", unsafe_allow_html=True)
    st.write("---")
    
    menu = st.radio("មឺនុយគ្រប់គ្រងសំខាន់ៗ:", [
        "📊 Dashboard (ផ្ទាំងបញ្ជាជារួម)",
        "📂 Student Database (ទិន្នន័យសិស្ស)",
        "💰 Finance & Sales (ចំណូល/ការលក់)",
        "📚 GEP Content (ផលិតកម្មមេរៀន)",
        "🤖 AI & Automation (ប្រព័ន្ធឆ្លាតវៃ)",
        "📈 Marketing & Strategy (យុទ្ធសាស្ត្រ)",
        "📜 Certification (សញ្ញាបត្រ/កាត)"
    ])
    
    st.write("---")
    st.markdown("<p style='text-align: center;'>Prepared by<br><b>CHAN Sokhoeurn, C2/DBA</b></p>", unsafe_allow_html=True)

# 3. ការបង្ហាញតាមផ្នែកនីមួយៗ
# --- ១. Dashboard ---
if menu == "📊 Dashboard (ផ្ទាំងបញ្ជាជារួម)":
    st.title("🏆 C2-EPE Executive Master Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("សិស្សសរុប", "1,250", "+15%")
    col2.metric("ចំណូលសរុប", "$18,500", "+8%")
    col3.metric("GEP Volumes", "9 Vols", "Active")
    col4.metric("AI Tasks", "154", "Automated")
    
    st.write("### 📈 វឌ្ឍនភាពនៃការរីកចម្រើន")
    chart_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 'Growth': [400, 600, 950, 1250]})
    st.area_chart(chart_data.set_index('Month'))

# --- ២. Student Database ---
elif menu == "📂 Student Database (ទិន្នន័យសិស្ស)":
    st.title("📂 Student Database & Skill Passport")
    st.write("ស្វែងរក និងគ្រប់គ្រងព័ត៌មានសិស្សតាមប្រព័ន្ធឌីជីថល")
    st.text_input("ស្វែងរកតាមឈ្មោះ ឬលេខសម្គាល់សិស្ស...")
    # Mock Database
    df = pd.DataFrame({
        'Student ID': ['C2-001', 'C2-002', 'C2-003'],
        'Name': ['Sokha', 'Bora', 'Davy'],
        'Level': ['C2 Mastery', 'A2 Flyers', 'B1 Intermediate'],
        'Skill Passport': ['95%', '45%', '70%']
    })
    st.table(df)

# --- ៣. Finance & Sales ---
elif menu == "💰 Finance & Sales (ចំណូល/ការលក់)":
    st.title("💰 Finance & Sales Tracking")
    c1, c2 = st.columns(2)
    with c1:
        st.write("#### ការលក់សៀវភៅ GEP (Volumes)")
        st.bar_chart(pd.DataFrame({'Sales': [150, 230, 85]}))
    with c2:
        st.write("#### ចំណូលតាមប្រភេទសេវាកម្ម")
        st.write("- ថ្លៃសិក្សា: $12,000")
        st.write("- លក់សៀវភៅ: $4,500")
        st.write("- ប្រឹក្សាយោបល់: $2,000")

# --- ៤. GEP Content ---
elif menu == "📚 GEP Content (ផលិតកម្មមេរៀន)":
    st.title("📚 GEP Content Management")
    st.info("ផ្តោតលើការផលិតសៀវភៅ Volume 2 (A2) និង Volume 8-9 (Mastery)")
    st.checkbox("រៀបចំមាតិកា Volume 2 (Completed)")
    st.checkbox("រៀបចំមាតិកា Volume 8 (In-Progress)")
    st.checkbox("រៀបចំមាតិកា Volume 9 (Planning)")
    if st.button("Update Content Status"):
        st.success("ស្ថានភាពមាតិកាត្រូវបានកត់ត្រា!")

# --- ៥. AI & Automation ---
elif menu == "🤖 AI & Automation (ប្រព័ន្ធឆ្លាតវៃ)":
    st.title("🤖 AI & Automation Hub")
    st.write("គ្រប់គ្រង Prompt និងប្រព័ន្ធឆ្លើយតបស្វ័យប្រវត្តិ")
    st.selectbox("ជ្រើសរើស AI Agent:", ["GEP Lesson Creator", "Auto-Grader", "Customer Support Bot"])
    st.button("Run AI Automation Process")

# --- ៦. Marketing & Strategy ---
elif menu == "📈 Marketing & Strategy (យុទ្ធសាស្ត្រ)":
    st.title("📈 Marketing & Blue Ocean Strategy")
    st.write("យុទ្ធសាស្ត្របង្កើតទីផ្សារថ្មី និងការផ្សព្វផ្សាយ")
    st.text_area("Blue Ocean Strategy Notes:", value="ផ្តោតលើ Early Specialization និង Medical English...")
    st.slider("Campaign Reach", 0, 10000, 5000)

# --- ៧. Certification ---
elif menu == "📜 Certification (សញ្ញាបត្រ/កាត)":
    st.title("📜 Certification & Digital ID")
    st.write("ចេញសញ្ញាបត្រឌីជីថលពណ៌មាស Premium")
    st.selectbox("ជ្រើសរើសប្រភេទសញ្ញាបត្រ:", ["Flyers Master Certificate", "C2 Mastery Certificate", "Digital Student ID"])
    if st.button("✨ បង្កើតសញ្ញាបត្រ (Generate)"):
        st.balloons()
        st.success("សញ្ញាបត្រត្រូវបានបង្កើតដោយជោគជ័យ!")

# 4. Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #D4AF37;'><b>© 2026 C2-EPE ACADEMY | SYSTEM VERSION 2.0</b></p>", unsafe_allow_html=True)
