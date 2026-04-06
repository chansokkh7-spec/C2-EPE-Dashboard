import streamlit as st
import pandas as pd
import plotly.express as px

# 1. កំណត់ការរចនា (Page Configuration) - ពណ៌ Navy Blue & Gold
st.set_page_config(page_title="C2-EPE Academy | Master Dashboard", layout="wide")

# Custom CSS ដើម្បីឱ្យមើលទៅ Premium
st.markdown("""
    <style>
    .main { background-color: #001f3f; color: white; }
    .stButton>button { background-color: #D4AF37; color: #001f3f; font-weight: bold; border-radius: 10px; }
    .sidebar .sidebar-content { background-color: #001a33; }
    h1, h2, h3 { color: #D4AF37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. របារចំហៀង (Sidebar Navigation)
st.sidebar.image("https://via.placeholder.com/150x150.png?text=C2-EPE+Logo", width=150) # ដាក់ Logo របស់អ្នកនៅទីនេះ
st.sidebar.title("C2-EPE Academy")
menu = st.sidebar.radio("ផ្នែកគ្រប់គ្រងសំខាន់ៗ:", 
    ["ផ្ទាំងបញ្ជាជារួម (Dashboard)", "ទិន្នន័យសិស្ស (Student Database)", "ផ្នែកលក់ & ចំណូល (Sales)", "គ្រប់គ្រងមាតិកា (GEP Content)"])

# 3. ការបង្ហាញទិន្នន័យសិស្ស (Mock Data)
data = {
    'Student Name': ['Sokha', 'Bora', 'Davy', 'Vutha'],
    'Level': ['Flyers Master', 'A2', 'C2 Mastery', 'A2'],
    'Progress': [85, 45, 90, 30],
    'Fees Paid': [150, 150, 300, 150]
}
df = pd.DataFrame(data)

# --- ផ្នែកទី ១: Dashboard ជារួម ---
if menu == "ផ្ទាំងបញ្ជាជារួម (Dashboard)":
    st.title("🏆 C2-EPE Executive Dashboard")
    st.subheader("ស្ថានភាពអាជីវកម្ម និងការសិក្សាជារួម")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("សិស្សសរុប", "1,250 នាក់", "+5%")
    col2.metric("ចំណូលសរុប (Monthly)", "$18,500", "+12%")
    col3.metric("កម្រិត Mastery (C2)", "85 នាក់", "+2%")

    # ក្រាហ្វបង្ហាញវឌ្ឍនភាពសិស្ស
    fig = px.bar(df, x='Student Name', y='Progress', color='Level', 
                 title="វឌ្ឍនភាពសិស្សតាមកម្រិតនីមួយៗ", color_discrete_sequence=['#D4AF37', '#C0C0C0'])
    st.plotly_chart(fig, use_container_width=True)

# --- ផ្នែកទី ២: ទិន្នន័យសិស្ស & Skill Passport ---
elif menu == "ទិន្នន័យសិស្ស (Student Database)":
    st.title("📂 Student Database & Digital Passport")
    st.write("ស្វែងរក និងគ្រប់គ្រងព័ត៌មានសិស្ស")
    
    search = st.text_input("វាយឈ្មោះសិស្សដើម្បីស្វែងរក...")
    st.dataframe(df)
    
    if st.button("Generate Digital Skill Passport"):
        st.success("កំពុងបង្កើតវិញ្ញាបនបត្រឌីជីថល... រួចរាល់!")

# --- ផ្នែកទី ៣: ផ្នែកលក់ & ហិរញ្ញវត្ថុ ---
elif menu == "ផ្នែកលក់ & ចំណូល (Sales)":
    st.title("💰 Financial Management")
    st.write("របាយការណ៍ចំណូលពីការលក់សៀវភៅ GEP និងវគ្គសិក្សា")
    
    chart_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar'], 'Revenue': [5000, 7000, 18500]})
    st.line_chart(chart_data.set_index('Month'))

# --- ផ្នែកទី ៤: GEP Content Management ---
elif menu == "គ្រប់គ្រងមាតិកា (GEP Content)":
    st.title("📚 GEP Courseware Management")
    st.info("ផ្នែកនេះសម្រាប់គ្រប់គ្រងសៀវភៅ Volume 2 (A2) និង Volume 8-9 (C2)")
    
    status = st.selectbox("ស្ថានភាពផលិតសៀវភៅ:", ["កំពុងរៀបចំ", "រង់ចាំការត្រួតពិនិត្យ", "បោះពុម្ពរួចរាល់"])
    st.write(f"ស្ថានភាពបច្ចុប្បន្ន: **{status}**")

# 4. Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Prepared by CHAN Sokhoeurn, C2/DBA | Powered by AI Automation</p>", unsafe_allow_html=True)
