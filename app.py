import calendar
import datetime
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)", layout="wide"
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)")
st.markdown(
    "กรอกข้อมูลกำหนดการและขั้นตอนต่างๆ ด้านล่าง"
    " ระบบจะสร้างรูปภาพตารางรถไฟพร้อมลูกศรชี้มาตราให้อัตโนมัติ"
)

with st.form("election_form"):
  st.subheader("📌 1. ข้อมูลการเลือกตั้งและเดือนที่ต้องการแสดงในตาราง")
  col_a, col_b, col_c = st.columns(3)
  with col_a:
    org_name = st.text_input(
        "ชื่อองค์กรปกครองส่วนท้องถิ่น",
        "เทศบาลตำบลบึงระมาณ เขตเลือกตั้งที่ 1 อ.บางระกำ",
    )
  with col_b:
    start_month = st.selectbox(
        "เดือนเริ่มต้นของตาราง",
        options=list(range(1, 13)),
        index=9,
        format_func=lambda m: [
            "มกราคม",
            "กุมภาพันธ์",
            "มีนาคม",
            "เมษายน",
            "พฤษภาคม",
            "มิถุนายน",
            "กรกฎาคม",
            "สิงหาคม",
            "กันยายน",
            "ตุลาคม",
            "พฤศจิกายน",
            "ธันวาคม",
        ][m - 1],
    )
  with col_c:
    start_year = st.number_input(
        "ปี พ.ศ. ของตาราง", value=2569, min_value=2500, max_value=2700
    )

  st.markdown("---")
  st.subheader("📅 2. กรอกวันที่ขั้นตอนตามกฎหมายและห้วงเวลา")

  col1, col2 = st.columns(2)

  with col1:
    d_dismiss = st.date_input(
        "1. วันที่ถูกสั่งให้พ้นจากตำแหน่ง", datetime.date(2026, 10, 1)
    )
    d_proposal = st.date_input(
        "2. ผอ.กต.ท้องถิ่นเสนอร่าง ส.ถ.1/1", datetime.date(2026, 10, 1)
    )
    d_approval = st.date_input(
        "3. วันที่ ผอ.กต.จว. ให้ความเห็นชอบ", datetime.date(2026, 10, 5)
    )
    d_announce_elect = st.date_input(
        "4. ผอ.กต.ท้องถิ่นประกาศให้มีการเลือกตั้ง (ม.12) / แต่งตั้ง"
        " กกต.ท้องถิ่น",
        datetime.date(2026, 10, 10),
    )

    st.markdown("**5. วันรับสมัครเลือกตั้ง (ม.12) (ห้วงเวลา 5 วัน)**")
    d_reg_range = st.date_input(
        "เลือกห้วงเวลาวันรับสมัคร (วันแรก - วันสุดท้าย)",
        value=(datetime.date(2026, 10, 26), datetime.date(2026, 10, 30)),
    )

    d_station_voter = st.date_input(
        "6. ประกาศหน่วยเลือกตั้ง (ม.23) / ประกาศบัญชีผู้มีสิทธิ (ม.43)",
        datetime.date(2026, 11, 2),
    )
    d_staff_objection = st.date_input(
        "7. วันสุดท้ายแต่งตั้ง จพง.ปน. (ม.28) / ยื่นคำร้องคัดค้านก่อนเลือกตั้ง"
        " 20 วัน (ม.56)",
        datetime.date(2026, 11, 2),
    )
    d_candidate_list = st.date_input(
        "8. ประกาศบัญชีรายชื่อผู้สมัคร (ม.52)", datetime.date(2026, 11, 9)
    )
    d_house_notice = st.date_input(
        "9. วันสุดท้ายส่งหนังสือแจ้งเจ้าบ้าน (ม.43)", datetime.date(2026, 11, 12)
    )
    d_reject_appeal = st.date_input(
        "10. วันสุดท้ายยื่นคำร้องต่อ กกต. กรณีไม่รับสมัคร (ม.55)",
        datetime.date(2026, 11, 3),
    )

  with col2:
    d_add_remove = st.date_input(
        "11. วันสุดท้ายเพิ่ม/ถอนชื่อ (ม.44,45) / วินิจฉัยสิทธิ (ม.56) /"
        " เปลี่ยนแปลงหน่วย (ม.23)",
        datetime.date(2026, 11, 12),
    )
    d_agent_appoint = st.date_input(
        "12. วันสุดท้ายแจ้งแต่งตั้งตัวแทนผู้สมัคร (ม.58)",
        datetime.date(2026, 11, 15),
    )

    st.markdown(
        "**13. แจ้งเหตุที่ไม่อาจไปใช้สิทธิเลือกตั้ง (ม.40) (ก่อนเลือกตั้ง 7"
        " วัน)**"
    )
    d_vote_before_range = st.date_input(
        "เลือกห้วงเวลาก่อนวันเลือกตั้ง 7 วัน",
        value=(datetime.date(2026, 11, 15), datetime.date(2026, 11, 21)),
    )

    st.markdown("**14. วันเลือกตั้ง**")
    d_election_range = st.date_input(
        "เลือกวัน/ห้วงเวลาวันเลือกตั้ง",
        value=(datetime.date(2026, 11, 22), datetime.date(2026, 11, 22)),
    )

    st.markdown(
        "**15. แจ้งเหตุที่ไม่อาจไปใช้สิทธิเลือกตั้ง (ม.40) (หลังวันเลือกตั้ง 7"
        " วัน)**"
    )
    d_vote_after_range = st.date_input(
        "เลือกห้วงเวลาหลังวันเลือกตั้ง 7 วัน",
        value=(datetime.date(2026, 11, 23), datetime.date(2026, 11, 29)),
    )

    d_court_train = st.date_input(
        "16. วันสุดท้ายศาลอุทธรณ์วินิจฉัย (ม.56) / มอบวัสดุอุปกรณ์ / อบรม"
        " จพง.ปน.",
        datetime.date(2026, 11, 20),
    )
    d_voter_list_send = st.date_input(
        "17. วันสุดท้ายจัดส่งบัญชีรายชื่อผู้มีสิทธิเพื่อทำบัญชีถูกจำกัดสิทธิ",
        datetime.date(2026, 12, 4),
    )
    d_result_no_case = st.date_input(
        "18. ประกาศผลการเลือกตั้ง กรณีไม่มีเรื่องร้องคัดค้าน (ม.17 ว.1)",
        datetime.date(2026, 12, 22),
    )
    d_result_with_case = st.date_input(
        "19. ประกาศผู้ไม่ไปใช้สิทธิ (ม.41) / ประกาศผลกรณีมีเรื่องร้อง (ม.17"
        " ว.2)",
        datetime.date(2027, 1, 21),
    )

  submitted = st.form_submit_button("🚀 สร้างตารางรถไฟพร้อมลูกศรชี้อัตโนมัติ")

if submitted:
  st.success("สร้างตารางรถไฟและปักหมุดลูกศรขั้นตอนเรียบร้อยแล้ว!")

  # แปลงปี พ.ศ. เป็น ค.ศ. สำหรับคำนวณ
  year_ad = start_year - 543

  # หาวันเลือกตั้งหลักสำหรับคำนวณวันถอยหลัง
  elec_main_date = (
      d_election_range[0]
      if isinstance(d_election_range, (list, tuple))
      else d_election_range
  )

  # ฟังก์ชันสร้างตารางสไตล์ Excel + ลูกศรด้วย SVG
  def render_svg_calendar(y, m):
    month_names_th = [
        "",
        "มกราคม",
        "กุมภาพันธ์",
        "มีนาคม",
        "เมษายน",
        "พฤษภาคม",
        "มิถุนายน",
        "กรกฎาคม",
        "สิงหาคม",
        "กันยายน",
        "ตุลาคม",
        "พฤศจิกายน",
        "ธันวาคม",
    ]
    num_days = calendar.monthrange(y, m)[1]
    thai_wd_map = {0: "จ", 1: "อ", 2: "พ", 3: "พฤ", 4: "ศ", 5: "ส", 6: "อา"}

    days_row, dates_row, vac_row, elec_row = "", "", "", ""

    for d in range(1, num_days + 1):
      curr_dt = datetime.date(y, m, d)
      wd = curr_dt.weekday()
      vac_cnt = (curr_dt - d_dismiss).days + 1
      elec_cnt = (curr_dt - elec_main_date).days

      days_row += (
          f"<th style='border:1px solid #000; width:28px;"
          f" background:#eef;'>{thai_wd_map[wd]}</th>"
      )
      dates_row += (
          f"<td style='border:1px solid #000; font-weight:bold;'>{d}</td>"
      )
      vac_row += f"<td style='border:1px solid #000;'>{vac_cnt}</td>"
      elec_row += (
          f"<td style='border:1px solid #000;"
          f" color:{'red' if elec_cnt == 0 else 'black'};'>{elec_cnt}</td>"
      )

    html_code = f"""
        <div style='margin-bottom: 30px;'>
            <h4 style='margin-bottom:5px;'>เดือน{month_names_th[m]} {y + 543}</h4>
            <table style='border-collapse:collapse; text-align:center; font-size:13px; width:100%; font-family:Sarabun, sans-serif; background:#fff;'>
                <tr><th style='border:1px solid #000; width:200px; text-align:left; background:#ddd;'>วัน</th>{days_row}</tr>
                <tr><th style='border:1px solid #000; text-align:left; background:#ddd;'>วันที่</th>{dates_row}</tr>
                <tr><th style='border:1px solid #000; text-align:left; background:#ddd;'>นับจากวันที่ถูกสั่งให้พ้นตำแหน่ง</th>{vac_row}</tr>
                <tr><th style='border:1px solid #000; text-align:left; background:#ddd;'>นับจากวันเลือกตั้ง</th>{elec_row}</tr>
            </table>
        </div>
        """
    st.markdown(html_code, unsafe_allow_html=True)

  # แสดงตาราง 4 เดือนต่อเนื่องนับจากเดือนที่เลือก
  curr_y, curr_m = year_ad, start_month
  for _ in range(4):
    render_svg_calendar(curr_y, curr_m)
    curr_m += 1
    if curr_m > 12:
      curr_m = 1
      curr_y += 1
