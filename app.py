# --- 2. Student Database ---
elif menu == "📂 Student Database":
    st.title("📂 Student Database & Skill Passport")
    st.write("Real-time tracking of student achievements and mastery levels.")
    
    # បង្កើតទិន្នន័យជា DataFrame
    df = pd.DataFrame({
        'Student ID': ['C2-001', 'C2-002', 'C2-003'],
        'Name': ['Sokha', 'Bora', 'Davy'],
        'Level': ['C2 Mastery', 'A2 Flyers', 'B1 Intermediate'],
        'Skill Passport': ['95%', '45%', '70%']
    })

    # ការរចនាតារាងឱ្យមានស្ទីលពណ៌មាស Premium
    st.markdown("""
        <style>
        table {
            border: 2px solid #D4AF37 !important;
            border-collapse: collapse;
            width: 100%;
            border-radius: 15px;
            overflow: hidden;
        }
        th {
            background-color: #D4AF37 !important;
            color: #001f3f !important;
            text-align: left;
            padding: 15px;
            font-size: 18px;
        }
        td {
            border: 1px solid #D4AF37 !important;
            padding: 12px;
            color: #FCF6BA !important;
            background-color: rgba(0, 31, 63, 0.5);
        }
        tr:hover {
            background-color: rgba(212, 175, 55, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # បង្ហាញតារាងជា HTML ដើម្បីឱ្យស៊ីជាមួយ CSS ខាងលើ
    st.write(df.to_html(index=False, escape=False), unsafe_allow_html=True)
    
    st.write("")
    if st.button("✨ Export to PDF"):
        st.success("Preparing Student Skill Passports...")
