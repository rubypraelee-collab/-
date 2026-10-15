import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ",
    page_icon="🚂",
    layout="wide",
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)")
st.markdown(
    "กรอกข้อมูลด้านล่างนี้เพื่อให้ระบบสร้างตารางปฏิทิน คำนวณวัน และจัดทำตารางรถไฟให้อัตโนมัติทันทีโดยไม่ต้องจัดหน้าเอง"
)

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

  submitted = st.form_submit_button("🚀 สร้างตารางรถไฟเลือกตั้ง")

if submitted:
  st.success("สร้างตารางคำนวณเรียบร้อยแล้ว!")

  st.markdown(f"### ผลลัพธ์แผนการจัดการเลือกตั้ง: {org_name}")
  st.write(f"- **วันที่ตำแหน่งว่างลง:** {vacancy_date.strftime('%d %B %Y')}")
  st.write(
      "- **วันรับสมัคร:**"
      f" {start_reg_date.strftime('%d %B %Y')} ถึง"
      f" {end_reg_date.strftime('%d %B %Y')}"
  )
  st.write(f"- **วันเลือกตั้ง:** {election_date.strftime('%d %B %Y')}")

  # ตัวอย่างการคำนวณวันถอยหลัง / เดินหน้า
  st.markdown("---")
  st.subheader("📅 ตารางปฏิทินและห้วงเวลาการปฏิบัติงาน")

  # สร้างตารางจำลองเดือนตุลาคม 2569 เป็นตัวอย่างแสดงผล
  days_in_oct = []
  for day in range(1, 32):
    d = datetime.date(2026, 10, day)
    days_in_oct.append({
        "วันที่": day,
        "วันในสัปดาห์": d.strftime("%a"),
        "นับจากวันว่าง": (d - vacancy_date).days + 1,
        "นับจากวันเลือกตั้ง": (d - election_date).days,
    })

  df_oct = pd.DataFrame(days_in_oct)
  st.markdown("#### เดือนตุลาคม 2569")
  st.dataframe(df_oct.T, use_container_width=True)

  st.info(
      "💡 ระบบกำลังถูกพัฒนาต่อยอดให้แสดงผลเป็นตารางปฏิทินแนวนอนพร้อมลูกศรชี้"
      "ตามแบบฟอร์มทางการของสำนักงาน กกต."
  )
