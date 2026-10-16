import calendar
import datetime
import io
from PIL import Image, ImageDraw, ImageFont
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)", layout="wide"
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)")
st.markdown(
    "กรอกข้อมูลกำหนดการและขั้นตอนต่างๆ ด้านล่าง"
    " ระบบจะสร้างตารางรถไฟพร้อมลูกศรชี้มาตราตามพิกัดวันที่จริงให้อัตโนมัติ"
)

with st.form("election_form"):
  st.subheader("📌 1. ข้อมูลการเลือกตั้งและตั้งต้นปฏิทิน")
  col_a, col_b, col_c = st.columns(3)
  with col_a:
    org_name = st.text_input(
        "ชื่อองค์กรปกครองส่วนท้องถิ่น",
        "เทศบาลตำบลบึงระมาณ เขตเลือกตั้งที่ 1 อ.บางระกำ",
    )
  with col_b:
    d_dismiss = st.date_input(
        "วันที่ถูกสั่งให้พ้นจากตำแหน่ง (วันเริ่มนับ)",
        datetime.date(2026, 10, 1),
    )
  with col_c:
    # คำนวณวันเลือกตั้งตั้งต้น
    d_election = st.date_input("วันเลือกตั้ง", datetime.date(2026, 11, 22))

  st.markdown("---")
  st.subheader("📅 2. กรอกวันที่ขั้นตอนและห้วงเวลาตามกฎหมาย")

  col1, col2 = st.columns(2)

  with col1:
    d_proposal = st.date_input(
        "ผอ.กต.ท้องถิ่นเสนอร่าง ส.ถ.1/1", datetime.date(2026, 10, 1)
    )
    d_approval = st.date_input(
        "วันที่ ผอ.กต.จว. ให้ความเห็นชอบ", datetime.date(2026, 10, 5)
    )
    d_announce_elect = st.date_input(
        "ผอ.กต.ท้องถิ่นประกาศเลือกตั้ง (ม.12) / แต่งตั้ง กกต.ท้องถิ่น",
        datetime.date(2026, 10, 10),
    )

    st.markdown("**วันรับสมัครเลือกตั้ง (ม.12) (ห้วงเวลา 5 วัน)**")
    d_reg_start = st.date_input(
        "วันแรกรับสมัคร", datetime.date(2026, 10, 26), key="reg_s"
    )
    d_reg_end = st.date_input(
        "วันสุดท้ายรับสมัคร", datetime.date(2026, 10, 30), key="reg_e"
    )

    d_station_voter = st.date_input(
        "ประกาศหน่วยเลือกตั้ง (ม.23) / ประกาศบัญชีผู้มีสิทธิ (ม.43)",
        datetime.date(2026, 11, 2),
    )
    d_staff_objection = st.date_input(
        "วันสุดท้ายแต่งตั้ง จพง.ปน. (ม.28) / ยื่นคำร้องคัดค้านฯ (ม.56)",
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
        "วันสุดท้ายเพิ่ม/ถอนชื่อ (ม.44,45) / วินิจฉัยสิทธิ (ม.56) /"
        " เปลี่ยนแปลงหน่วย (ม.23)",
        datetime.date(2026, 11, 12),
    )
    d_agent_appoint = st.date_input(
        "วันสุดท้ายแจ้งแต่งตั้งตัวแทนผู้สมัคร (ม.58)",
        datetime.date(2026, 11, 15),
    )

    st.markdown(
        "**แจ้งเหตุไม่อาจไปใช้สิทธิเลือกตั้ง (ม.40) (ก่อนเลือกตั้ง 7 วัน)**"
    )
    d_vote_before_s = st.date_input(
        "วันเริ่มแจ้งเหตุ (ก่อนเลือกตั้ง)",
        datetime.date(2026, 11, 15),
        key="vb_s",
    )
    d_vote_before_e = st.date_input(
        "วันสิ้นสุดแจ้งเหตุ (ก่อนเลือกตั้ง)",
        datetime.date(2026, 11, 21),
        key="vb_e",
    )

    st.markdown(
        "**แจ้งเหตุไม่อาจไปใช้สิทธิเลือกตั้ง (ม.40) (หลังวันเลือกตั้ง 7 วัน)**"
    )
    d_vote_after_s = st.date_input(
        "วันเริ่มแจ้งเหตุ (หลังเลือกตั้ง)",
        datetime.date(2026, 11, 23),
        key="va_s",
    )
    d_vote_after_e = st.date_input(
        "วันสิ้นสุดแจ้งเหตุ (หลังเลือกตั้ง)",
        datetime.date(2026, 11, 29),
        key="va_e",
    )

    d_court_train = st.date_input(
        "วันสุดท้ายศาลอุทธรณ์วินิจฉัย (ม.56) / มอบอุปกรณ์ / อบรม จพง.ปน.",
        datetime.date(2026, 11, 20),
    )
    d_voter_list_send = st.date_input(
        "วันสุดท้ายจัดส่งบัญชีรายชื่อผู้มีสิทธิฯ (ถูกจำกัดสิทธิ)",
        datetime.date(2026, 12, 4),
    )
    d_result_no_case = st.date_input(
        "ประกาศผลเลือกตั้ง (ไม่มีเรื่องร้องคัดค้าน) (ม.17 ว.1)",
        datetime.date(2026, 12, 22),
    )
    d_result_with_case = st.date_input(
        "ประกาศผู้ไม่ไปใช้สิทธิ (ม.41) / ประกาศผล (มีเรื่องร้อง) (ม.17 ว.2)",
        datetime.date(2027, 1, 21),
    )

  submitted = st.form_submit_button("🚀 สร้างตารางรถไฟพร้อมลูกศรอัตโนมัติ")

if submitted:
  st.success("คำนวณวันและสร้างตารางรถไฟเรียบร้อยแล้ว!")

  # แสดงปฏิทินแบบ HTML คำนวณวันอ้างอิงจากปี/เดือน ที่กรอกจริง
  start_year = d_dismiss.year
  start_month = d_dismiss.month

  def render_html_calendar(y, m):
    num_days = calendar.monthrange(y, m)[1]
    thai_wd_map = {0: "จ", 1: "อ", 2: "พ", 3: "พฤ", 4: "ศ", 5: "ส", 6: "อา"}
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

    days_row, dates_row, vac_row, elec_row = "", "", "", ""

    for d in range(1, num_days + 1):
      curr_dt = datetime.date(y, m, d)
      wd = curr_dt.weekday()
      vac_cnt = (curr_dt - d_dismiss).days + 1
      elec_cnt = (curr_dt - d_election).days

      # ไฮไลต์วันเลือกตั้ง และ วันรับสมัคร
      bg_color = "#f8f9fa"
      if curr_dt == d_election:
        bg_color = "#ffeb3b"
      elif d_reg_start <= curr_dt <= d_reg_end:
        bg_color = "#e3f2fd"

      days_row += (
          f"<th style='border:1px solid #000; padding:4px;"
          f" text-align:center; background-color:{bg_color};'>{thai_wd_map[wd]}</th>"
      )
      dates_row += (
          f"<td style='border:1px solid #000; padding:4px; text-align:center;"
          f" font-weight:bold; background-color:{bg_color};'>{d}</td>"
      )
      vac_row += (
          f"<td style='border:1px solid #000; padding:4px;"
          f" text-align:center;'>{vac_cnt}</td>"
      )
      elec_row += (
          f"<td style='border:1px solid #000; padding:4px; text-align:center;"
          f" color:{'red' if elec_cnt == 0 else 'black'};'>{elec_cnt}</td>"
      )

    html_table = f"""
        <div style="margin-bottom: 20px; overflow-x: auto;">
            <h4 style="margin-bottom: 5px;">เดือน{month_names_th[m]} {y + 543}</h4>
            <table style="border-collapse: collapse; width: 100%; font-size: 12px; font-family: sans-serif; background-color: white;">
                <tr><th style="border:1px solid #000; padding:6px; background-color:#ddd; width:220px; text-align:left;">วัน</th>{days_row}</tr>
                <tr><th style="border:1px solid #000; padding:6px; background-color:#ddd; text-align:left;">วันที่</th>{dates_row}</tr>
                <tr><th style="border:1px solid #000; padding:6px; background-color:#ddd; text-align:left;">นับจากวันที่ถูกสั่งให้พ้นจากตำแหน่ง</th>{vac_row}</tr>
                <tr><th style="border:1px solid #000; padding:6px; background-color:#ddd; text-align:left;">นับจากวันเลือกตั้ง</th>{elec_row}</tr>
            </table>
        </div>
        """
    st.markdown(html_table, unsafe_allow_html=True)

  # แสดงตารางต่อเนื่อง 4 เดือนนับจากเดือนของวันว่าง
  cy, cm = start_year, start_month
  for _ in range(4):
    render_html_calendar(cy, cm)
    cm += 1
    if cm > 12:
      cm = 1
      cy += 1

  # สรุปขั้นตอนและมาตราตามวันที่กรอกจริง
  st.markdown("---")
  st.subheader("📌 สรุปกำหนดการและเส้นทางรถไฟเลือกตั้ง (เรียงตามลำดับวัน)")

  events = [
      (d_dismiss, "วันที่ถูกสั่งให้พ้นจากตำแหน่ง", "-"),
      (d_proposal, "ผอ.กต.ท้องถิ่นเสนอร่าง ส.ถ.1/1", "-"),
      (d_approval, "วันที่ ผอ.กต.จว. ให้ความเห็นชอบ", "-"),
      (
          d_announce_elect,
          "ผอ.กต.ท้องถิ่นประกาศให้มีการเลือกตั้ง / แต่งตั้ง กกต.ท้องถิ่น",
          "มาตรา 12",
      ),
      (
          f"{d_reg_start.strftime('%d/%m/%Y')} - {d_reg_end.strftime('%d/%m/%Y')}",
          "วันรับสมัครเลือกตั้ง (ห้วงเวลา 5 วัน)",
          "มาตรา 12",
      ),
      (
          d_station_voter,
          (
              "ประกาศกำหนดหน่วยเลือกตั้ง/ที่เลือกตั้ง และ"
              " ประกาศบัญชีรายชื่อผู้มีสิทธิเลือกตั้ง"
          ),
          "มาตรา 23 / 43",
      ),
      (
          d_staff_objection,
          (
              "วันสุดท้ายแต่งตั้ง จพง.ปน. และ"
              " วันสุดท้ายยื่นคำร้องคัดค้านการรับสมัคร (ก่อนวันเลือกตั้ง >= 20"
              " วัน)"
          ),
          "มาตรา 28 / 56",
      ),
      (d_candidate_list, "ประกาศบัญชีรายชื่อผู้สมัคร", "มาตรา 52"),
      (
          d_house_notice,
          "วันสุดท้ายส่งหนังสือแจ้งเจ้าบ้าน (ก่อนวันเลือกตั้ง >= 10 วัน)",
          "มาตรา 43",
      ),
      (
          d_reject_appeal,
          "วันสุดท้ายยื่นคำร้องต่อ กกต. กรณีไม่รับสมัคร",
          "มาตรา 55",
      ),
      (
          d_add_remove,
          (
              "วันสุดท้ายเพิ่มชื่อ/ถอนชื่อ, วันสุดท้าย กกต. วินิจฉัยสิทธิสมัคร,"
              " วันสุดท้ายเปลี่ยนแปลงหน่วยเลือกตั้ง"
          ),
          "มาตรา 44, 45 / 56 / 23",
      ),
      (
          d_agent_appoint,
          "วันสุดท้ายแจ้งการแต่งตั้งตัวแทนผู้สมัคร",
          "มาตรา 58",
      ),
      (
          f"{d_vote_before_s.strftime('%d/%m/%Y')} - {d_vote_before_e.strftime('%d/%m/%Y')}",
          "แจ้งเหตุที่ไม่อาจไปใช้สิทธิเลือกตั้ง (ก่อนวันเลือกตั้ง 7 วัน)",
          "มาตรา 40",
      ),
      (d_election, "🎉 วันเลือกตั้ง", "มาตรา 40"),
      (
          f"{d_vote_after_s.strftime('%d/%m/%Y')} - {d_vote_after_e.strftime('%d/%m/%Y')}",
          "แจ้งเหตุที่ไม่อาจไปใช้สิทธิเลือกตั้ง (หลังวันเลือกตั้ง 7 วัน)",
          "มาตรา 40",
      ),
      (
          d_court_train,
          (
              "วันสุดท้ายศาลอุทธรณ์วินิจฉัยสิทธิสมัคร, มอบวัสดุอุปกรณ์,"
              " อบรม จพง.ปน."
          ),
          "มาตรา 56",
      ),
      (
          d_voter_list_send,
          "วันสุดท้ายจัดส่งบัญชีรายชื่อผู้มีสิทธิเพื่อทำบัญชีผู้ถูกจำกัดสิทธิ",
          "-",
      ),
      (
          d_result_no_case,
          "ประกาศผลการเลือกตั้ง (กรณีไม่มีเรื่องร้องคัดค้าน)",
          "มาตรา 17 วรรคหนึ่ง",
      ),
      (
          d_result_with_case,
          (
              "ประกาศบัญชีรายชื่อผู้ไม่ไปใช้สิทธิ (ม.41) / ประกาศผล"
              " (กรณีมีเรื่องร้องคัดค้าน)"
          ),
          "มาตรา 41 / มาตรา 17 วรรคสอง",
      ),
  ]

  import pandas as pd

  df_events = pd.DataFrame(events, columns=["วันที่ / ห้วงเวลา", "ขั้นตอน / กิจกรรม", "อ้างอิงกฎหมาย"])
  st.table(df_events)
