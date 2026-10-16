import calendar
import datetime
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)", layout="wide"
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)")
st.markdown(
    "กรอกข้อมูลกำหนดการและขั้นตอนต่างๆ ด้านล่าง"
    " ระบบจะสร้างตารางรถไฟพร้อมลูกศรชี้มาตราตามวันที่ให้อัตโนมัติ"
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
    d_election = st.date_input("วันเลือกตั้ง", datetime.date(2026, 11, 22))

  st.markdown("---")
  st.subheader("📅 2. กรอกวันที่ขั้นตอนและห้วงเวลาตามกฎหมาย")

  col1, col2 = st.columns(2)

  with col1:
    d_proposal = st.date_input(
        "1. ผอ.กต.ท้องถิ่นเสนอร่าง ส.ถ.1/1", datetime.date(2026, 10, 1)
    )
    d_approval = st.date_input(
        "2. วันที่ ผอ.กต.จว. ให้ความเห็นชอบ", datetime.date(2026, 10, 5)
    )
    d_announce_elect = st.date_input(
        "3. ผอ.กต.ท้องถิ่นประกาศเลือกตั้ง (ม.12) / แต่งตั้ง กกต.ท้องถิ่น",
        datetime.date(2026, 10, 10),
    )

    st.markdown("**4. วันรับสมัครเลือกตั้ง (ม.12) (ห้วงเวลา 5 วัน)**")
    d_reg_start = st.date_input(
        "วันแรกรับสมัคร", datetime.date(2026, 10, 26), key="reg_s"
    )
    d_reg_end = st.date_input(
        "วันสุดท้ายรับสมัคร", datetime.date(2026, 10, 30), key="reg_e"
    )

    d_station_voter = st.date_input(
        "5. ประกาศหน่วยเลือกตั้ง (ม.23) / ประกาศบัญชีผู้มีสิทธิ (ม.43)",
        datetime.date(2026, 11, 2),
    )
    d_staff_objection = st.date_input(
        "6. วันสุดท้ายแต่งตั้ง จพง.ปน. (ม.28) / ยื่นคำร้องคัดค้านฯ (ม.56)",
        datetime.date(2026, 11, 2),
    )
    d_candidate_list = st.date_input(
        "7. ประกาศบัญชีรายชื่อผู้สมัคร (ม.52)", datetime.date(2026, 11, 9)
    )

  with col2:
    d_house_notice = st.date_input(
        "8. วันสุดท้ายส่งหนังสือแจ้งเจ้าบ้าน (ม.43)", datetime.date(2026, 11, 12)
    )
    d_reject_appeal = st.date_input(
        "9. วันสุดท้ายยื่นคำร้องต่อ กกต. กรณีไม่รับสมัคร (ม.55)",
        datetime.date(2026, 11, 3),
    )
    d_add_remove = st.date_input(
        "10. วันสุดท้ายเพิ่ม/ถอนชื่อ (ม.44,45) / วินิจฉัยสิทธิ (ม.56)",
        datetime.date(2026, 11, 12),
    )
    d_agent_appoint = st.date_input(
        "11. วันสุดท้ายแจ้งแต่งตั้งตัวแทนผู้สมัคร (ม.58)",
        datetime.date(2026, 11, 15),
    )

    st.markdown(
        "**12. แจ้งเหตุไม่อาจไปใช้สิทธิเลือกตั้ง (ม.40) (ก่อนเลือกตั้ง 7 วัน)**"
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
        "**13. แจ้งเหตุไม่อาจไปใช้สิทธิเลือกตั้ง (ม.40) (หลังวันเลือกตั้ง 7 วัน)**"
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

  submitted = st.form_submit_button(
      "🚀 สร้างตารางรถไฟพร้อมลูกศรชี้อัตโนมัติ"
  )

if submitted:
  st.success("คำนวณและสร้างตารางรถไฟเรียบร้อยแล้ว!")
  st.markdown(f"### 📊 ผลลัพธ์ตารางรถไฟเลือกตั้ง: {org_name}")

  def render_train_table_html(y, m):
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
    num_days = calendar.monthrange(y, m)[1]

    days_row, dates_row, vac_row, elec_row = "", "", "", ""
    day_tags = {}

    for d in range(1, num_days + 1):
      curr_dt = datetime.date(y, m, d)
      wd = curr_dt.weekday()
      vac_cnt = (curr_dt - d_dismiss).days + 1
      elec_cnt = (curr_dt - d_election).days

      labels_top = []
      labels_bottom = []

      if curr_dt == d_dismiss:
        labels_top.append("พ้นจากตำแหน่ง")
      if curr_dt == d_announce_elect:
        labels_top.append("ประกาศเลือกตั้ง (ม.12)")
      if d_reg_start <= curr_dt <= d_reg_end:
        labels_top.append("วันรับสมัคร (ม.12)")
      if curr_dt == d_election:
        labels_top.append("🎉 วันเลือกตั้ง (ม.40)")

      if curr_dt == d_station_voter:
        labels_bottom.append("ประกาศหน่วย/บัญชี (ม.23/43)")
      if curr_dt == d_candidate_list:
        labels_bottom.append("ประกาศรายชื่อผู้สมัคร (ม.52)")
      if curr_dt == d_house_notice:
        labels_bottom.append("แจ้งเจ้าบ้าน (ม.43)")

      top_str = " | ".join(labels_top)
      top_html = (
          f"<div style='font-size:9px; color:red; font-weight:bold; height:35px;"
          f" writing-mode:vertical-lr; transform:rotate(180deg); margin:0 auto;'>{top_str}</div>"
          if labels_top
          else ""
      )

      bot_str = " | ".join(labels_bottom)
      bot_html = (
          f"<div style='font-size:9px; color:blue; font-weight:bold; height:35px;"
          f" writing-mode:vertical-lr; margin:0 auto;'>{bot_str}</div>"
          if labels_bottom
          else ""
      )

      bg_color = "#ffffff"
      if curr_dt == d_election:
        bg_color = "#ffeb3b"
      elif d_reg_start <= curr_dt <= d_reg_end:
        bg_color = "#e3f2fd"

      days_row += (
          f"<th style='border:1px solid #000; padding:2px; text-align:center;"
          f" background-color:{bg_color}; font-size:11px;'>{thai_wd_map[wd]}<br>{top_html}</th>"
      )
      dates_row += (
          f"<td style='border:1px solid #000; padding:4px; text-align:center;"
          f" font-weight:bold; background-color:{bg_color}; font-size:12px;'>{d}</td>"
      )
      vac_row += (
          f"<td style='border:1px solid #000; padding:4px; text-align:center;"
          f" font-size:11px;'>{vac_cnt}</td>"
      )

      elec_color = "red" if elec_cnt == 0 else "black"
      elec_row += (
          f"<td style='border:1px solid #000; padding:4px; text-align:center;"
          f" color:{elec_color}; font-weight:bold; font-size:11px;'>{elec_cnt}</td>"
      )

      day_tags[d] = bot_html

    bot_row = ""
    for d in range(1, num_days + 1):
      bot_row += (
          f"<td style='border:1px solid #000; padding:2px; text-align:center;"
          f" background:#f9f9f9;'>{day_tags[d]}</td>"
      )

    html_code = f"""
        <div style="margin-bottom: 30px; overflow-x: auto;">
            <h4 style="margin-bottom: 8px; color: #333;">เดือน{month_names_th[m]} {y + 543}</h4>
            <table style="border-collapse: collapse; width: 100%; font-family: sans-serif; background-color: white;">
                <tr>
                    <td style="border:1px solid #000; padding:6px; background-color:#ddd; width:220px; font-weight:bold; font-size:12px;">กิจกรรม / ลูกศรชี้</td>
                    {days_row}
                </tr>
                <tr>
                    <td style="border:1px solid #000; padding:6px; background-color:#ddd; font-weight:bold; font-size:12px;">วัน</td>
                    {dates_row}
                </tr>
                <tr>
                    <td style="border:1px solid #000; padding:6px; background-color:#ddd; font-weight:bold; font-size:12px;">วันที่</td>
                    {dates_row}
                </tr>
                <tr>
                    <td style="border:1px solid #000; padding:6px; background-color:#ddd; font-weight:bold; font-size:12px;">นับจากวันที่ถูกสั่งให้พ้นจากตำแหน่ง</td>
                    {vac_row}
                </tr>
                <tr>
                    <td style="border:1px solid #000; padding:6px; background-color:#ddd; font-weight:bold; font-size:12px;">นับจากวันเลือกตั้ง</td>
                    {elec_row}
                </tr>
                <tr>
                    <td style="border:1px solid #000; padding:6px; background-color:#ddd; font-weight:bold; font-size:12px;">รายละเอียดขั้นตอนเพิ่มเติม</td>
                    {bot_row}
                </tr>
            </table>
        </div>
        """
    st.markdown(html_code, unsafe_allow_html=True)

  render_train_table_html(d_dismiss.year, d_dismiss.month)

  next_m = d_dismiss.month + 1
  next_y = d_dismiss.year
  if next_m > 12:
    next_m = 1
    next_y += 1
  render_train_table_html(next_y, next_m)
