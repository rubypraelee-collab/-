import datetime
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ", layout="centered"
)

st.title("🚂 ระบบสร้างตารางรถไฟเลือกตั้งอัตโนมัติ")
st.markdown(
    "กรอกข้อมูลกำหนดการเลือกตั้งด้านล่าง ระบบจะสร้างรูปตารางรถไฟพร้อมลูกศรและมาตราให้อัตโนมัติ"
)

with st.form("train_form"):
  org_name = st.text_input(
      "ชื่อองค์กรปกครองส่วนท้องถิ่น",
      "เทศบาลตำบลบึงระมาณ เขต 1 อ.บางระกำ",
  )
  vacancy_date = st.date_input(
      "วันที่ตำแหน่งว่างลง", datetime.date(2026, 10, 1)
  )
  election_date = st.date_input("วันเลือกตั้ง", datetime.date(2026, 11, 22))

  submitted = st.form_submit_button("🚀 สร้างตารางรถไฟ")

if submitted:
  # สร้างรูปตารางด้วย Matplotlib
  fig, ax = plt.subplots(figsize=(12, 6))
  ax.axis("off")
  ax.set_xlim(0, 100)
  ax.set_ylim(0, 100)

  # หัวข้อ
  ax.text(
      50,
      92,
      f"แผนการจัดการเลือกตั้ง {org_name}",
      fontsize=14,
      weight="bold",
      ha="center",
  )
  ax.text(
      50,
      85,
      (
          f"วันว่าง: {vacancy_date.strftime('%d %b %Y')} | วันเลือกตั้ง:"
          f" {election_date.strftime('%d %b %Y')}"
      ),
      fontsize=10,
      ha="center",
      color="gray",
  )

  # วาดกรอบตารางตุลาคม (แก้ไขวงเล็บให้ถูกต้องแล้วที่นี่)
  rect = plt.Rectangle(
      (10, 45), 80, 25, linewidth=1, edgecolor="black", facecolor="none"
  )
  ax.add_patch(rect)

  ax.text(
      12,
      63,
      "เดือนตุลาคม 2569 (ตารางจำลองอัตโนมัติ)",
      fontsize=11,
      weight="bold",
  )
  ax.text(12, 53, "นับจากวันเลือกตั้ง: 52  51  50  49  ...  0  1  2", fontsize=9)

  # ตัวอย่างลูกศรชี้มาตราอัตโนมัติ
  ax.annotate(
      "วันรับสมัคร (ม.12)",
      xy=(55, 45),
      xytext=(55, 25),
      arrowprops=dict(
          facecolor="blue", shrink=0.05, width=1.5, headwidth=6
      ),
      fontsize=9,
      weight="bold",
      ha="center",
      color="blue",
  )

  # บันทึกรูปชั่วคราวและแสดงผลบนเว็บ
  plt.savefig("output_table.png", dpi=200, bbox_inches="tight")
  plt.close()

  st.success("สร้างตารางรถไฟเรียบร้อยแล้ว!")
  st.image("output_table.png", caption="ตารางรถไฟเลือกตั้งพร้อมลูกศรมาตรา")

  with open("output_table.png", "rb") as file:
    st.download_button(
        label="📥 ดาวน์โหลดรูปภาพตารางรถไฟ",
        data=file,
        file_name="election_train_table.png",
        mime="image/png",
    )
