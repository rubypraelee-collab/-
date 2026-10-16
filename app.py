import calendar
import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ", layout="wide"
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)")
st.markdown(
    "กรอกข้อมูลกำหนดการเลือกตั้งด้านล่าง ระบบจะสร้างตารางรถไฟตามแบบฟอร์มทางการ"
    " ให้อัตโนมัติ"
)

with st.form("train_form"):
  col1, col2 = st.columns(2)
  with col1:
    org_name = st.text_input(
        "ชื่อองค์กรปกครองส่วนท้องถิ่น",
        "เทศบาลตำบลบึงระมาณ เขตเลือกตั้งที่ 1 อ.บางระกำ",
    )
    vacancy_date = st.date_input(
        "วันที่ตำแหน่งว่างลง", datetime.date(2026, 10, 1)
    )
  with col2:
    election_date = st.date_input("วันเลือกตั้ง", datetime.date(2026, 11, 22))

  submitted = st.form_submit_button("🚀 สร้างตารางรถไฟ")

if submitted:
  st.success("สร้างตารางเรียบร้อยแล้ว!")
  st.markdown(f"### แผนการจัดการเลือกตั้ง: {org_name}")
  st.markdown(
      f"**วันที่ตำแหน่งว่างลง:** {vacancy_date.strftime('%d %B %Y')} |"
      f" **วันเลือกตั้ง:** {election_date.strftime('%d %B %Y')}"
  )
  st.markdown("---")

  # ฟังก์ชันสร้างตารางสไตล์ Excel ด้วย HTML
  def render_html_calendar(year, month, month_name):
    num_days = calendar.monthrange(year, month)[1]
    thai_wd_map = {0: 'จ', 1: 'อ', 2: 'พ', 3: 'พฤ', 4: 'ศ', 5: 'ส', 6: 'อา'}

    days_row = ''
    dates_row = ''
    vac_row = ''
    elec_row = ''

    for d in range(1, num_days + 1):
      current_date = datetime.date(year, month, d)
      wd = current_date.weekday()
      days_row += (
          f"<th style='border:1px solid #999; padding:6px;"
          f" text-align:center; background-color:#f8f9fa;'>{thai_wd_map[wd]}</th>"
      )
      dates_row += (
          f"<td style='border:1px solid #999; padding:6px;"
          f" text-align:center; font-weight:bold;'>{d}</td>"
      )

      vac_count = (current_date - vacancy_date).days + 1
      elec_count = (current_date - election_date).days

      vac_row += (
          f"<td style='border:1px solid #999; padding:6px;"
          f" text-align:center;'>{vac_count}</td>"
      )
      elec_row += (
          f"<td style='border:1px solid #999; "
          f"padding:6px; text-align:center; color:{'red' if elec_count == 0 else 'black'};'>{elec_count}</td>"
      )

    html_table = f"""
        <div style="margin-bottom: 25px; overflow-x: auto;">
            <h4 style="margin-bottom: 8px; color: #333;">เดือน{month_name} {year + 543}</h4>
            <table style="border-collapse: collapse; width: 100%; font-size: 14px; font-family: sans-serif; background-color: white;">
                <tr>
                    <th style="border:1px solid #999; padding:8px; background-color:#e9ecef; width:220px; text-align:left;">วัน</th>
                    {days_row}
                </tr>
                <tr>
                    <th style="border:1px solid #999; padding:8px; background-color:#e9ecef; text-align:left;">วันที่</th>
                    {dates_row}
                </tr>
                <tr>
                    <th style="border:1px solid #999; padding:8px; background-color:#e9ecef; text-align:left;">นับจากวันที่ตำแหน่งว่างลง</th>
                    {vac_row}
                </tr>
                <tr>
                    <th style="border:1px solid #999; padding:8px; background-color:#e9ecef; text-align:left;">นับจากวันเลือกตั้ง</th>
                    {elec_row}
                </tr>
            </table>
        </div>
        """
    st.markdown(html_table, unsafe_allow_html=True)

  # แสดงตารางเดือนตุลาคม และ พฤศจิกายน
  render_html_calendar(2026, 10, 'ตุลาคม')
  render_html_calendar(2026, 11, 'พฤศจิกายน')

  st.info(
      '💡 ตารางด้านบนถูกสร้างขึ้นในรูปแบบตาราง Excel ทางเว็บ รองรับภาษาไทยสมบูรณ์'
      ' 100% สามารถแคปหน้าจอหรือนำไปใช้งานต่อได้ทันทีครับ'
  )
