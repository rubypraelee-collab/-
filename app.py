import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ",
    page_icon="🚂",
    layout="wide",
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)")
st.markdown("กรอกข้อมูลกำหนดการเลือกตั้งเพื่อให้ระบบสร้างตารางรถไฟอัตโนมัติ")

with st.form("election_form"):
  st.subheader("📌 กำหนดการเลือกตั้ง")
  col1, col2 = st.columns(2)

  with col1:
    org_name = st.text_input(
        "ชื่อองค์กรปกครองส่วนท้องถิ่น",
        value="เทศบาลตำบลบึงระมาณ เขตเลือกตั้งที่ 1 อ.บางระกำ",
    )
    vacancy_date = st.date_input(
        "วันที่ตำแหน่งว่างลง", value=datetime.date(2026, 10, 1)
    )
    election_date = st.date_input(
        "วันเลือกตั้ง", value=datetime.date(2026, 11, 22)
    )

  with col2:
    start_reg_date = st.date_input(
        "วันเริ่มต้นรับสมัคร", value=datetime.date(2026, 10, 26)
    )
    end_reg_date = st.date_input(
        "วันสิ้นสุดรับสมัคร", value=datetime.date(2026, 10, 30)
    )

  submitted = st.form_submit_button("🚀 สร้างตารางรถไฟ")

if submitted:
  st.success("สร้างตารางเรียบร้อยแล้ว!")
  st.markdown(f"### แผนการจัดการเลือกตั้ง: {org_name}")

  # ฟังก์ชันช่วยสร้างตารางปฏิทินรายเดือน
  def render_calendar_table(year, month, month_name, vacancy_date, election_date):
    st.markdown(f"#### เดือน{month_name} {year + 543}")
    
    # หาวันทั้งหมดในเดือนนั้น
    import calendar
    cal = calendar.monthcalendar(year, month)
    days_header = ["วัน", "พฤ", "ศ", "ส", "อา", "จ", "อ", "พ", "พฤ", "ศ", "ส", "อา", "จ", "อ", "พ", "พฤ", "ศ", "ส", "อา", "จ", "อ", "พ", "พฤ", "ศ", "ส", "อา", "จ", "อ", "พ", "พฤ", "ศ", "ส"]
    
    # สร้างตารางจำลองรายวัน
    data_days = []
    data_vacancy = []
    data_election = []
    
    # หาจำนวนวันในเดือน
    num_days = calendar.monthrange(year, month)[1]
    
    row_days = ["วันที่"]
    row_vac = ["นับจากวันที่ตำแหน่งว่างลง"]
    row_elec = ["นับจากวันเลือกตั้ง"]
    
    for d in range(1, num_days + 1):
      current_date = datetime.date(year, month, d)
      row_days.append(str(d))
      row_vac.append(str((current_date - vacancy_date).days + 1))
      row_elec.append(str((current_date - election_date).days))
      
    df_display = pd.DataFrame([row_days[1:], row_vac[1:], row_elec[1:]], 
                              columns=[str(i) for i in range(1, num_days + 1)],
                              index=["วันที่", "นับจากวันที่ตำแหน่งว่างลง", "นับจากวันเลือกตั้ง"])
    
    st.dataframe(df_display, use_container_width=True)

  # แสดงตารางเดือนตุลาคม และ พฤศจิกายน
  render_calendar_table(2026, 10, "ตุลาคม", vacancy_date, election_date)
  render_calendar_table(2026, 11, "พฤศจิกายน", vacancy_date, election_date)
