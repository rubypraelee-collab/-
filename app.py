import calendar
import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ", layout="wide"
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)")
st.markdown(
    "กรอกข้อมูลกำหนดการและขั้นตอนต่างๆ ด้านล่าง ระบบจะนำไปสร้างตารางรถไฟและสรุปแผนงานให้อัตโนมัติ"
)

with st.form("election_form"):
  st.subheader("📌 ข้อมูลองค์กรและวันสำคัญหลัก")
  col_a, col_b, col_c = st.columns(3)
  with col_a:
    org_name = st.text_input(
        "ชื่อองค์กรปกครองส่วนท้องถิ่น",
        "เทศบาลตำบลบึงระมาณ เขตเลือกตั้งที่ 1 อ.บางระกำ",
    )
  with col_b:
    vacancy_date = st.date_input(
        "วันที่ถูกสั่งให้พ้นจากตำแหน่ง", datetime.date(2026, 10, 1)
    )
  with col_c:
    election_date = st.date_input("วันเลือกตั้ง", datetime.date(2026, 11, 22))

  st.markdown("---")
  st.subheader("📅 รายละเอียดขั้นตอนและห้วงเวลาตามระเบียบ กกต.")

  col1, col2 = st.columns(2)

  with col1:
    d_proposal = st.date_input(
        "ผอ.กต.ท้องถิ่นเสนอร่าง ส.ถ.1/1", datetime.date(2026, 10, 1)
    )
    d_approval = st.date_input(
        "วันที่ ผอ.กต.จว. ให้ความเห็นชอบ", datetime.date(2026, 10, 5)
    )
    d_announce_elect = st.date_input(
        "ผอ.กต.ท้องถิ่นประกาศให้มีการเลือกตั้ง / แต่งตั้ง กกต.ท้องถิ่น",
        datetime.date(2026, 10, 10),
    )

    st.markdown("---")
    st.markdown("**วันรับสมัครเลือกตั้ง (ม.12) (ห้วงเวลา 5 วัน)**")
    col_r1, col_r2 = st.columns(2)
    with col_r1:
      start_reg = st.date_input("วันแรกของการรับสมัคร", datetime.date(2026, 10, 26))
    with col_r2:
      end_reg = st.date_input("วันสุดท้ายของการรับสมัคร", datetime.date(2026, 10, 30))

    d_station_voter = st.date_input(
        "ประกาศหน่วยเลือกตั้ง (ม.23) / ประกาศบัญชีผู้มีสิทธิ (ม.43)",
        datetime.date(2026, 11, 2),
    )
    d_staff_objection = st.date_input(
        "วันสุดท้ายแต่งตั้ง จพง.ปน. (ม.28) / ยื่นคำร้องคัดค้านก่อนเลือกตั้ง 20 วัน (ม.56)",
        datetime.date(2026, 11, 2),
    )
    d_candidate_list = st.date_input(
        "ประกาศบัญชีรายชื่อผู้สมัคร (ม.52)", datetime.date(2026, 11, 9)
    )
    d_house_notice = st.date_input(
        "วันสุดท้ายส่งหนังสือแจ้งเจ้าบ้าน (ม.43)", datetime.date(2026, 11, 12)
    )
    d_reject_appeal = st.date_input(
        "วันสุดท้ายยื่นคำร้องต่อ กกต. กรณีไม่รับสมัคร (ม.55)",
        datetime.date(2026, 11, 3),
    )

  with col2:
    d_add_remove = st.date_input(
        "วันสุดท้ายเพิ่ม/ถอนชื่อ (ม.44,45) / วินิจฉัยสิทธิ (ม.56) / เปลี่ยนแปลงหน่วย (ม.23)",
        datetime.date(2026, 11, 12),
    )
    d_agent_appoint = st.date_input(
        "วันสุดท้ายแจ้งแต่งตั้งตัวแทนผู้สมัคร (ม.58)",
        datetime.date(2026, 11, 15),
    )

    st.markdown("---")
    st.markdown("**แจ้งเหตุไม่อาจไปใช้สิทธิเลือกตั้ง (ม.40)**")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
      d_vote_before = st.date_input(
          "ห้วงเวลาก่อนวันเลือกตั้ง 7 วัน", datetime.date(2026, 11, 15)
      )
    with col_e2:
      d_vote_after = st.date_input(
          "ห้วงเวลาหลังวันเลือกตั้ง 7 วัน", datetime.date(2026, 11, 29)
      )

    d_court_train = st.date_input(
        "วันสุดท้ายศาลอุทธรณ์วินิจฉัย (ม.56) / มอบวัสดุอุปกรณ์ / อบรม จพง.ปน.",
        datetime.date(2026, 11, 20),
    )
    d_voter_list_send = st.date_input(
        "วันสุดท้ายจัดส่งบัญชีรายชื่อผู้มีสิทธิเพื่อทำบัญชีถูกจำกัดสิทธิ",
        datetime.date(2026, 12, 4),
    )
    d_result_no_case = st.date_input(
        "ประกาศผลเลือกตั้ง (ไม่มีเรื่องร้องคัดค้าน) (ม.17 ว.1)",
        datetime.date(2026, 12, 22),
    )
    d_result_with_case = st.date_input(
        "ประกาศรายชื่อผู้ไม่ไปใช้สิทธิ (ม.41) / ประกาศผล (มีเรื่องร้อง) (ม.17 ว.2)",
        datetime.date(2027, 1, 21),
    )

  submitted = st.form_submit_button("🚀 บันทึกและสร้างตารางรถไฟอัตโนมัติ")

if submitted:
  st.success("บันทึกข้อมูลและสร้างตารางเรียบร้อยแล้ว!")
  st.markdown(f"### แผนการจัดการเลือกตั้ง: {org_name}")
  st.markdown(
      f"**วันที่ตำแหน่งว่างลง:** {vacancy_date.strftime('%d %B %Y')} |"
      f" **วันเลือกตั้ง:** {election_date.strftime('%d %B %Y')}"
  )
  st.markdown("---")

  # ฟังก์ชันสร้างตารางสไตล์ Excel ด้วย HTML พร้อมแสดงรายละเอียดเดือน
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
          f"<td style='border:1px solid #999;"
          f" padding:6px; text-align:center; color:{'red' if elec_count == 0 else 'black'};'>{elec_count}</td>"
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

  # แสดงตาราง 4 เดือนหลัก (ต.ค. 69 - ม.ค. 70)
  render_html_calendar(2026, 10, 'ตุลาคม')
  render_html_calendar(2026, 11, 'พฤศจิกายน')
  render_html_calendar(2026, 12, 'ธันวาคม')
  render_html_calendar(2027, 1, 'มกราคม')
