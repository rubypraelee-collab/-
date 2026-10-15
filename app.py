import calendar
import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)",
    page_icon="🚂",
    layout="wide",
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (รูปแบบทางการ กกต.)")
st.markdown(
    "กรอกข้อมูลด้านล่างเพื่อสร้างตารางรถไฟพร้อมคำนวณวันและแสดงเหตุการณ์ตามมาตราต่างๆ"
)

with st.form("election_form"):
  st.subheader("📌 กำหนดการเลือกตั้งหลัก")
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
        "วันเริ่มต้นรับสมัคร", value=datetime.date(2026, 10, 26)
    )
    end_reg = st.date_input(
        "วันสิ้นสุดรับสมัคร", value=datetime.date(2026, 10, 30)
    )

  submitted = st.form_submit_button("🚀 สร้างตารางรถไฟและกำหนดการอัตโนมัติ")

if submitted:
  st.success("สร้างตารางและคำนวณวันสำคัญเรียบร้อยแล้ว!")

  # แสดงหัวข้อสรุปแผน
  st.markdown(f"### แผนการจัดการเลือกตั้ง: {org_name}")
  st.markdown(
      f"- **วันที่ตำแหน่งว่างลง:** {vacancy_date.strftime('%d %B %Y')}"
  )
  st.markdown(
      f"- **วันรับสมัคร:** {start_reg.strftime('%d %B %Y')} ถึง"
      f" {end_reg.strftime('%d %B %Y')}"
  )
  st.markdown(f"- **วันเลือกตั้ง:** {election_date.strftime('%d %B %Y')}")

  # คำนวณวันสำคัญตามกฎหมายอัตโนมัติ
  notice_date = vacancy_date  # วันที่ถูกสั่งให้พ้นจากตำแหน่ง
  res_decl = start_reg - datetime.timedelta(
      days=3
  )  # ผอ.กต.ท้องถิ่นประกาศให้มีการเลือกตั้ง / แต่งตั้ง กกต.ท้องถิ่น
  polling_station_notice = election_date - datetime.timedelta(
      days=20
  )  # ประกาศกำหนดหน่วย/ที่เลือกตั้ง (ม.23)
  voter_list_notice = election_date - datetime.timedelta(
      days=20
  )  # ประกาศบัญชีรายชื่อผู้มีสิทธิ (ม.43)
  candidate_list_notice = start_reg + datetime.timedelta(
      days=5
  )  # ประกาศบัญชีรายชื่อผู้สมัคร (ม.52)
  house_notice = election_date - datetime.timedelta(
      days=10
  )  # วันสุดท้ายส่งหนังสือแจ้งเจ้าบ้าน (ม.43)
  setab_notice = election_date - datetime.timedelta(
      days=15
  )  # วันสุดท้ายแต่งตั้ง จพง.ปน. (ม.28)

  st.markdown("---")
  st.subheader("📋 สรุปกำหนดเวลาและมาตราสำคัญ (Auto-Calculated)")

  milestones = [
      {
          "วันที่": vacancy_date.strftime("%d %B %Y"),
          "เหตุการณ์ / ขั้นตอน": (
              "วันที่ถูกสั่งให้พ้นจากตำแหน่ง / วันที่ตำแหน่งว่างลง"
          ),
          "อ้างอิง": "-",
      },
      {
          "วันที่": res_decl.strftime("%d %B %Y"),
          "เหตุการณ์ / ขั้นตอน": (
              "ผอ.กต.ท้องถิ่นประกาศให้มีการเลือกตั้ง และแต่งตั้ง กกต.ท้องถิ่น"
          ),
          "อ้างอิง": "มาตรา 12",
      },
      {
          "วันที่": (
              f"{start_reg.strftime('%d %B %Y')} ถึง"
              f" {end_reg.strftime('%d %B %Y')}"
          ),
          "เหตุการณ์ / ขั้นตอน": "วันรับสมัครเลือกตั้งสมาชิกสภาท้องถิ่น",
          "อ้างอิง": "มาตรา 12",
      },
      {
          "วันที่": candidate_list_notice.strftime("%d %B %Y"),
          "เหตุการณ์ / ขั้นตอน": "วันประกาศบัญชีรายชื่อผู้สมัคร",
          "อ้างอิง": "มาตรา 52",
      },
      {
          "วันที่": polling_station_notice.strftime("%d %B %Y"),
          "เหตุการณ์ / ขั้นตอน": (
              "วันประกาศกำหนดหน่วยเลือกตั้ง / ที่เลือกตั้ง และเปลี่ยนแปลงหน่วย"
          ),
          "อ้างอิง": "มาตรา 23",
      },
      {
          "วันที่": voter_list_notice.strftime("%d %B %Y"),
          "เหตุการณ์ / ขั้นตอน": "วันประกาศบัญชีรายชื่อผู้มีสิทธิเลือกตั้ง",
          "อ้างอิง": "มาตรา 43",
      },
      {
          "วันที่": house_notice.strftime("%d %B %Y"),
          "เหตุการณ์ / ขั้นตอน": "วันสุดท้ายส่งหนังสือแจ้งเจ้าบ้านไปยังผู้มีสิทธิ",
          "อ้างอิง": "มาตรา 43",
      },
      {
          "วันที่": election_date.strftime("%d %B %Y"),
          "เหตุการณ์ / ขั้นตอน": (
              "🎉 **วันเลือกตั้ง** และวันแจ้งเหตุที่ไม่อาจไปใช้สิทธิ"
          ),
          "อ้างอิง": "มาตรา 40",
      },
      {
          "วันที่": (election_date + datetime.timedelta(days=30)).strftime(
              "%d %B %Y"
          ),
          "เหตุการณ์ / ขั้นตอน": (
              "วันประกาศผลการเลือกตั้ง (กรณีไม่มีเรื่องร้องคัดค้าน)"
          ),
          "อ้างอิง": "มาตรา 17 ว.1",
      },
  ]

  df_milestones = pd.DataFrame(milestones)
  st.table(df_milestones)

  st.markdown("---")
  st.subheader("📅 ตารางปฏิทินรถไฟ 4 เดือน (ต.ค. 2569 - ม.ค. 2570)")

  # ฟังก์ชันสร้างตารางปฏิทิน
  def render_calendar_table(year, month, month_name):
    st.markdown(f"#### เดือน{month_name} {year + 543}")
    num_days = calendar.monthrange(year, month)[1]

    thai_wd_map = {0: "จ", 1: "อ", 2: "พ", 3: "พฤ", 4: "ศ", 5: "ส", 6: "อา"}
    row_day_name = ["วัน"]
    row_date_num = ["วันที่"]
    row_vac = ["นับจากวันที่ตำแหน่งว่างลง"]
    row_elec = ["นับจากวันเลือกตั้ง"]

    for d in range(1, num_days + 1):
      current_date = datetime.date(year, month, d)
      wd = current_date.weekday()
      row_day_name.append(thai_wd_map[wd])
      row_date_num.append(str(d))
      row_vac.append(str((current_date - vacancy_date).days + 1))
      row_elec.append(str((current_date - election_date).days))

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
    st.dataframe(df, use_container_width=True, hide_index=True)

  # แสดงตารางทั้ง 4 เดือน
  render_calendar_table(2026, 10, "ตุลาคม")
  render_calendar_table(2026, 11, "พฤศจิกายน")
  render_calendar_table(2026, 12, "ธันวาคม")
  render_calendar_table(2027
