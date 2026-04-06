import streamlit as st
import pandas as pd
import plotly.express as px

# 1. កំណត់ការរចនា (Page Configuration) - Navy Blue & Gold Theme
st.set_page_config(page_title="C2-EPE Academy | Master Dashboard", layout="wide")

# Custom CSS សម្រាប់ Premium Branding (Navy Blue #001f3f & Metallic Gold #D4AF37)
st.markdown("""
    <style>
    /* ផ្ទៃខាងក្រោយមេ */
    .stApp {
        background-color: #001f3f;
    }
    
    /* ការរចនាអត្ថបទពណ៌មាស Gradient */
    h1, h2, h3 {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
    }

    /* ការរចនាប៊ូតុងឱ្យមានពន្លឺពណ៌មាស */
    .stButton>button {
        background: linear-gradient(45deg, #BF953F, #FCF6BA, #AA771C);
        color: #001f3f !important;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 15px #FCF6BA;
    }

    /* ការរចនា Sidebar */
    [data-testid="stSidebar"] {
        background-color: #001a33;
        border-right: 2px solid #D4AF37;
    }
    .st-emotion-cache-10trblm { color: #D4AF37 !important; } /* Sidebar text */

    /* ការរចនា Metrics Card */
    div[data-testid="stMetricValue"] {
        color: #FCF6BA !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. របារចំហៀង (Sidebar Navigation)
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>C2-EPE Academy</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #D4AF37; text-align: center;'><i>Mastery in English</i></p>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("ជ្រើសរើសផ្នែកគ្រប់គ្រង:", 
        ["📊 ផ្ទាំងបញ្ជាជារួម", "📂 ទិន្នន័យសិស្ស (Skill Passport)", "💰 ចំណូល និងការលក់", "📚 គ្រប់គ្រងមាតិកា (GEP)"])
    st.write("---")
    st.markdown("<p style='font-size: 12px; color: gray;'>Prepared by CHAN Sokhoeurn, C2/DBA</p>", unsafe_allow_html=True)

# 3. ការបង្កើតទិន្នន័យគំរូ (Mock Data)
data = {
    'ឈ្មោះសិស្ស': ['សុក្ខា', 'បូរ៉ា', 'ដាវី', 'វុឌ្ឍា'],
    'កម្រិត': ['Flyers Master', 'A2', 'C2 Mastery', 'Flyers Master'],
    'វឌ្ឍនភាព': [85, 45, 95, 30],
    'ស្ថានភាពបង់ប្រាក់': ['បង់រួច', 'ជំពាក់', 'បង់រួច', 'បង់រួច']
}
df = pd.DataFrame(data)

# --- ផ្នែកទី ១: Dashboard ជារួម ---
if menu == "📊 ផ្ទាំងបញ្ជាជារួម":
    st.title("🏆 Executive Master Dashboard")
    
    # បង្ហាញលេខសង្ខេប (Metrics)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("សិស្សសរុប", "1,250", "+12%")
    c2.metric("ចំណូលខែនេះ", "$18,500", "+5%")
    c3.metric("កម្រិត Mastery (C2)", "85", "Active")
    c4.metric("សៀវភៅបោះពុម្ព", "9 Volumes", "Volume 8 In-Progress")

    # ក្រាហ្វវឌ្ឍនភាពសិស្ស
    st.write("### 📈 ក្រាហ្វវឌ្ឍនភាពសិស្សតាមកម្រិត")
    fig = px.bar(df, x='ឈ្មោះសិស្ស', y='វឌ្ឍនភាព', color='កម្រិត',
                 color_discrete_sequence=['#D4AF37', '#C0C0C0', '#8A6E2F'])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#D4AF37")
    st.plotly_chart(fig, use_container_width=True)

# --- ផ្នែកទី ២: ទិន្នន័យសិស្ស ---
elif menu == "📂 ទិន្នន័យសិស្ស (Skill Passport)":
    st.title("📂 Student Database & Skill Passport")
    st.write("ស្វែងរកព័ត៌មានសិស្ស និងតាមដានជំនាញ (Skill Tracking)")
    
    search = st.text_input("ស្វែងរកតាមឈ្មោះសិស្ស...")
    st.dataframe(df.style.highlight_max(axis=0, color='#D4AF37'))
    
    if st.button("✨ បង្កើត Digital Skill Passport"):
        st.balloons()
        st.success("វិញ្ញាបនបត្រឌីជីថលកម្រិត Premium ត្រូវបានបង្កើតរួចរាល់!")

# --- ផ្នែកទី ៣: ផ្នែកលក់ & ហិរញ្ញវត្ថុ ---
elif menu == "💰 ចំណូល និងការលក់":
    st.title("💰 Financial & Sales Management")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### របាយការណ៍ចំណូលប្រចាំឆ្នាំ")
        st.area_chart(pd.DataFrame({'ចំណូល': [5000, 7500, 12000, 18500]}))
    with col_b:
        st.write("### ការលក់សៀវភៅ GEP")
        st.bar_chart(pd.DataFrame({'Volume': ['V1', 'V2', 'V8'], 'ចំនួនលក់': [120, 85, 45]}))

# --- ផ្នែកទី ៤: GEP Content ---
elif menu == "📚 គ្រប់គ្រងមាតិកា (GEP)":
    st.title("📚 GEP Courseware Production")
    st.info("ផ្តោតលើការផលិតសៀវភៅ Volume 2 (A2) និង Volume 8-9 (Advanced)")
    
    task = st.radio("ជ្រើសរើសស្ថានភាពផលិត:", ["រៀបចំមាតិកា (Drafting)", "រចនា Layout", "បោះពុម្ព (Printing)"])
    if st.button("Update Status"):
        st.write(f"ស្ថានភាពបច្ចុប្បន្នត្រូវបានកែប្រែទៅជា: **{task}**")

# 4. Footer ដ៏ថ្លៃថ្នូរ
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #D4AF37;'><b>Prepared by CHAN Sokhoeurn, C2/DBA</b><br><i>C2-EPE Academy & Junior Medical Institute (JMI) Eco-System</i></p>", unsafe_allow_html=True)
