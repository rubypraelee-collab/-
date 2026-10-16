import calendar
import datetime
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)", layout="wide"
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ (กกต.)")
st.markdown(
    "กรอกข้อมูลกำหนดการและขั้นตอนต่างๆ ด้านล่าง"
    " ระบบจะสร้างรูปภาพตารางรถไฟพร้อมลูกศรชี้มาตราตามวันที่ให้อัตโนมัติ"
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
      "🚀 สร้างรูปภาพตารางรถไฟพร้อมลูกศรชี้อัตโนมัติ"
  )

if submitted:
  st.success("คำนวณและวาดเส้นลูกศรลงในภาพตารางรถไฟเรียบร้อยแล้ว!")

  # ฟังก์ชันวาดรูปภาพ SVG ตารางพร้อมลูกศร
  def generate_train_table_svg(y, m):
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

    cell_w = 32
    cell_h = 24
    start_x = 220
    start_y = 120

    svg_items = []

    # หัวข้อเดือน
    svg_items.append(
        f"<text x='20' y='40' font-size='18' font-weight='bold'"
        f" font-family='Sarabun, sans-serif'>เดือน{month_names_th[m]}"
        f" {y + 543}</text>"
    )

    # วาดโครงสร้างตารางหลัก (หัวข้อแถว)
    headers = [
        "วัน",
        "วันที่",
        "นับจากวันที่ถูกสั่งให้พ้นตำแหน่ง",
        "นับจากวันเลือกตั้ง",
    ]
    for idx, h in enumerate(headers):
      svg_items.append(
          f"<rect x='20' y='{start_y + idx * cell_h}' width='{start_x - 20}'"
          f" height='{cell_h}' fill='#e0e0e0' stroke='#000' stroke-width='1'/>"
      )
      svg_items.append(
          f"<text x='25' y='{start_y + idx * cell_h + 16}' font-size='11'"
          " font-weight='bold'"
          f" font-family='Sarabun, sans-serif'>{h}</text>"
      )

    # วาดช่องวันที่และตัวเลขคำนวณวัน
    day_x_map = {}
    for d in range(1, num_days + 1):
      curr_dt = datetime.date(y, m, d)
      wd = curr_dt.weekday()
      vac_cnt = (curr_dt - d_dismiss).days + 1
      elec_cnt = (curr_dt - d_election).days
      cx = start_x + (d - 1) * cell_w
      day_x_map[curr_dt] = cx + cell_w / 2

      # สีพื้นหลังช่องวันเลือกตั้ง / รับสมัคร
      fill_bg = "#ffffff"
      if curr_dt == d_election:
        fill_bg = "#ffeb3b"
      elif d_reg_start <= curr_dt <= d_reg_end:
        fill_bg = "#e3f2fd"

      # แถว 1: วัน
      svg_items.append(
          f"<rect x='{cx}' y='{start_y}' width='{cell_w}' height='{cell_h}'"
          f" fill='{fill_bg}' stroke='#000'/>"
      )
      svg_items.append(
          f"<text x='{cx + cell_w / 2}' y='{start_y + 16}' font-size='11'"
          f" text-anchor='middle'>{thai_wd_map[wd]}</text>"
      )

      # แถว 2: วันที่
      svg_items.append(
          f"<rect x='{cx}' y='{start_y + cell_h}' width='{cell_w}'"
          f" height='{cell_h}' fill='{fill_bg}' stroke='#000'/>"
      )
      svg_items.append(
          f"<text x='{cx + cell_w / 2}' y='{start_y + cell_h + 16}'"
          f" font-size='11' font-weight='bold'"
          f" text-anchor='middle'>{d}</text>"
      )

      # แถว 3: นับวันว่าง
      svg_items.append(
          f"<rect x='{cx}' y='{start_y + cell_h * 2}' width='{cell_w}'"
          f" height='{cell_h}' fill='#ffffff' stroke='#000'/>"
      )
      svg_items.append(
          f"<text x='{cx + cell_w / 2}' y='{start_y + cell_h * 2 + 16}'"
          f" font-size='10' text-anchor='middle'>{vac_cnt}</text>"
      )

      # แถว 4: นับวันเลือกตั้ง
      svg_items.append(
          f"<rect x='{cx}' y='{start_y + cell_h * 3}' width='{cell_w}'"
          f" height='{cell_h}' fill='#ffffff' stroke='#000'/>"
      )
      txt_color = "red" if elec_cnt == 0 else "black"
      svg_items.append(
          f"<text x='{cx + cell_w / 2}' y='{start_y + cell_h * 3 + 16}'"
          f" font-size='10' fill='{txt_color}' font-weight='bold'"
          f" text-anchor='middle'>{elec_cnt}</text>"
      )

    # วาดลูกศรชี้ขึ้น-ลง และกล่องข้อความมาตราขั้นตอน
    table_top = start_y
    table_bottom = start_y + cell_h * 4

    def add_arrow_label(target_dt, label_text, direction='down'):
      if target_dt in day_x_map:
        tx = day_x_map[target_dt]
        if direction == 'down':  # ลูกศรชี้ลงมาจากด้านบน
          ty = table_top
          svg_items.append(
              f"<line x1='{tx}' y1='{ty - 35}' x2='{tx}' y2='{ty - 5}'"
              " stroke='red' stroke-width='2' marker-end='url(#arrow)'/>"
          )
          svg_items.append(
              f"<text x='{tx}' y='{ty - 42}' font-size='10' fill='red'"
              " font-weight='bold' text-anchor='middle'"
              f" font-family='Sarabun, sans-serif'>{label_text}</text>"
          )
        else:  # ลูกศรชี้ขึ้นมาจากด้านล่าง
          ty = table_bottom
          svg_items.append(
              f"<line x1='{tx}' y1='{ty + 35}' x2='{tx}' y2='{ty + 5}'"
              " stroke='blue' stroke-width='2' marker-end='url(#arrow_blue)'/>"
          )
          svg_items.append(
              f"<text x='{tx}' y='{ty + 48}' font-size='10' fill='blue'"
              " font-weight='bold' text-anchor='middle'"
              f" font-family='Sarabun, sans-serif'>{label_text}</text>"
          )

    # วาดลูกศรจุดสำคัญ
    add_arrow_label(
        d_dismiss, "วันที่ถูกสั่งให้พ้นจากตำแหน่ง", direction="down"
    )
    add_arrow_label(
        d_announce_elect,
        "ผอ.กต.ท้องถิ่นประกาศเลือกตั้ง (ม.12)",
        direction="down",
    )
    add_arrow_label(
        d_reg_start, "วันรับสมัครเลือกตั้ง (ม.12)", direction="down"
    )
    add_arrow_label(d_election, "🎉 วันเลือกตั้ง (ม.40)", direction="down")

    add_arrow_label(
        d_station_voter,
        "ประกาศหน่วยเลือกตั้ง (ม.23) / บัญชีรายชื่อ (ม.43)",
        direction="up",
    )
    add_arrow_label(
        d_candidate_list, "ประกาศรายชื่อผู้สมัคร (ม.52)", direction="up"
    )
    add_arrow_label(
        d_house_notice, "วันสุดท้ายแจ้งเจ้าบ้าน (ม.43)", direction="up"
    )

    svg_content = f"""
        <svg width='1220' height='320' xmlns='http://www.w3.org/2000/svg'>
            <defs>
                <marker id='arrow' viewBox='0 0 10 10' refX='5' refY='5' markerWidth='6' markerHeight='6' orient='auto-start-reverse'>
                    <path d='M 0 0 L 10 5 L 0 10 z' fill='red'/>
                </marker>
                <marker id='arrow_blue' viewBox='0 0 10 10' refX='5' refY='5' markerWidth='6' markerHeight='6' orient='auto-start-reverse'>
                    <path d='M 0 0 L 10 5 L 0 10 z' fill='blue'/>
                </marker>
            </defs>
            {''.join(svg_items)}
        </svg>
        """
    st.image(svg_content, use_column_width=True)

  # แสดงตารางปฏิทิน 2 เดือนหลัก (ตุลาคม และ พฤศจิกายน)
  st.subheader(f"📊 ผลลัพธ์รูปภาพตารางรถไฟเลือกตั้ง: {org_name}")
  generate_train_table_svg(d_dismiss.year, d_dismiss.month)

  # แสดงเดือนถัดไป
  next_m = d_dismiss.month + 1
  next_y = d_dismiss.year
  if next_m > 12:
    next_m = 1
    next_y += 1
  generate_train_table_svg(next_y, next_m)
