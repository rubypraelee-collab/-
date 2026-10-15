import calendar
import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ",
    page_icon="🚂",
    layout="wide",
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)")
st.markdown("กรอกข้อมูลกำหนดการเพื่อให้ระบบสร้างตารางรถไฟตามแบบฟอร์มทางการ")

with st.form("election_form"):
  st.subheader("📌 ข้อมูลการเลือกตั้ง")
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
    start_reg = st.date_input(
        "วันรับสมัคร (วันแรก)", value=datetime.date(2026, 10, 26)
    )
    end_reg = st.date_input(
        "วันรับสมัคร (วันสุดท้าย)", value=datetime.date(2026, 10, 30)
    )

  submitted = st.form_submit_button("🚀 สร้างตารางรถไฟรูปแบบทางการ")

if submitted:
  st.success("สร้างตารางสำเร็จ!")

  # แสดงหัวข้อรายงานตามแบบฟอร์ม
  st.markdown(
      f"### แผนการจัดการเลือกตั้ง {org_name} (กรณีสั่งให้พ้นจากตำแหน่ง)"
  )
  st.markdown(
      f"- **วันที่ตำแหน่งว่างลง:** {vacancy_date.strftime('%d %B %Y')}"
  )
  st.markdown(
      f"- **วันรับสมัคร:** {start_reg.strftime('%d %B %Y')} ถึง"
      f" {end_reg.strftime('%d %B %Y')}"
  )
  st.markdown(f"- **วันเลือกตั้ง:** {election_date.strftime('%d %B %Y')}")
  st.markdown("---")

  # ฟังก์ชันสร้างตารางรถไฟรายเดือนแบบ Excel
  def render_excel_style_table(year, month, month_name):
    st.markdown(f"#### เดือน{month_name} {year + 543}")

    num_days = calendar.monthrange(year, month)[1]

    days_thai = ["อา", "จ", "อ", "พ", "พฤ", "ศ", "ส"]
    row_day_name = ["วัน"]
    row_date_num = ["วันที่"]
    row_vac = ["นับจากวันที่ตำแหน่งว่างลง"]
    row_elec = ["นับจากวันเลือกตั้ง"]

    for d in range(1, num_days + 1):
      current_date = datetime.date(year, month, d)
      # วันในสัปดาห์ (0=Mon, 6=Sun)
      wd = current_date.weekday()
      # แปลงเป็นชื่อย่อภาษาไทย
      thai_wd_map = {
          0: "จ",
          1: "อ",
          2: "พ",
          3: "พฤ",
          4: "ศ",
          5: "ส",
          6: "อา",
      }

      row_day_name.append(thai_wd_map[wd])
      row_date_num.append(str(d))
      row_vac.append(str((current_date - vacancy_date).days + 1))
      row_elec.append(str((current_date - election_date).days))

    # เติมช่องว่างให้ครบ 31 ช่องหากเดือนมีไม่ถึง (เพื่อให้ตารางขนาดเท่ากัน)
    while len(row_date_num) < 32:
      row_day_name.append("")
      row_date_num.append("")
      row_vac.append("")
      row_elec.append("")

    columns_name = ["หัวข้อ"] + [str(i) for i in range(1, 32)]

    df_data = [
        [row_day_name[0]] + row_day_name[1:32],
        [row_date_num[0]] + row_date_num[1:32],
        [row_vac[0]] + row_vac[1:32],
        [row_elec[0]] + row_elec[1:32],
    ]

    df = pd.DataFrame(df_data, columns=columns_name)
    # ซ่อน Index ด้านซ้ายเพื่อให้เหมือนตาราง Excel
    st.dataframe(df, use_container_width=True, hide_index=True)

  # แสดงตารางเดือนตุลาคม และ พฤศจิกายน 2569
  render_excel_style_table(2026, 10, "ตุลาคม")
  render_excel_style_table(2026, 11, "พฤศจิกายน")
