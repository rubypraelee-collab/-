import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# ตั้งค่าฟอนต์ภาษาไทย (ถ้าใช้งานบน Windows หรือ Google Colab ให้เลือกฟอนต์ที่รองรับภาษาไทย เช่น TH Sarabun PSK หรือ Cordia New)
# ในตัวอย่างนี้ใช้โครงสร้างการวาดตารางและลูกศรชี้
fig, ax = plt.subplots(figsize=(14, 8))

# ซ่อนแกนพิกัดรอบนอก
ax.axis("off")
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# วาดหัวข้อรายงาน
ax.text(
    50,
    95,
    "แผนการจัดการเลือกตั้งสมาชิกสภา ทต.บึงระมาณ เขตเลือกตั้งที่ 1",
    fontsize=16,
    weight="bold",
    ha="center",
)
ax.text(
    50,
    90,
    "วันที่ตำแหน่งว่างลง: 1 ต.ค. 2569 | วันเลือกตั้ง: 22 พ.ย. 2569",
    fontsize=12,
    ha="center",
    color="gray",
)

# สร้างตารางจำลองเดือนตุลาคม 2569 (แถววันที่ 1-31)
# วาดกรอบตารางหลัก
rect_oct = plt.Rectangle((5, 60), 90, 20, linewidth=1.5, edgecolor="black", facecolor="none")
ax.add_patch(rect_oct)

ax.text(7, 75, "เดือนตุลาคม 2569", fontsize=12, weight="bold")

# วาดเส้นแบ่งตารางวัน (1-31)
for i in range(32):
    x_pos = 15 + (i * 2.5)
    ax.plot([x_pos, x_pos], [60, 80], color="black", linewidth=0.5)
    if i < 31:
        ax.text(x_pos + 1.25, 76, str(i + 1), fontsize=8, ha="center")

# แถวตาราง: นับจากวันที่ตำแหน่งว่างลง
ax.text(
    6,
    68,
    "นับจากวันว่าง",
    fontsize=9,
    weight="bold",
    verticalalignment="center",
)
for i in range(31):
    x_pos = 15 + (i * 2.5) + 1.25
    ax.text(x_pos, 68, str(i + 1), fontsize=8, ha="center", verticalalignment="center")

# แถวตาราง: นับจากวันเลือกตั้ง (ถอยหลัง)
ax.text(
    6,
    63,
    "นับจากวันเลือกตั้ง",
    fontsize=9,
    weight="bold",
    verticalalignment="center",
)
count_elec = 52
for i in range(31):
    x_pos = 15 + (i * 2.5) + 1.25
    val = count_elec - i
    ax.text(
        x_pos,
        63,
        str(val),
        fontsize=8,
        ha="center",
        verticalalignment="center",
        color="red" if val == 0 else "black",
    )

# --- ส่วนของการวาดลูกศรชี้มาตราสำคัญอัตโนมัติ ---
# ตัวอย่าง: ลูกศรชี้ "วันรับสมัครเลือกตั้ง (ม.12)" ที่วันที่ 26 ตุลาคม
x_target = 15 + (25 * 2.5) + 1.25  # พิกัดวันที่ 26
ax.annotate(
    "วันรับสมัครเลือกตั้ง (ม.12)",
    xy=(x_target, 60),
    xytext=(x_target, 45),
    arrowprops=dict(facecolor="blue", shrink=0.05, width=1.5, headwidth=6),
    fontsize=9,
    weight="bold",
    ha="center",
    color="blue",
)

# ตัวอย่าง: ลูกศรชี้ "วันเลือกตั้ง" ที่วันที่ 22 พฤศจิกายน (สมมติพิกัด)
ax.annotate(
    "วันเลือกตั้ง (ม.40)",
    xy=(50, 60),
    xytext=(50, 35),
    arrowprops=dict(facecolor="orange", shrink=0.05, width=2, headwidth=8),
    fontsize=10,
    weight="bold",
    ha="center",
    color="orange",
)

# บันทึกรูปภาพออกมา
plt.savefig("election_train_table.png", dpi=300, bbox_inches="tight")
plt.show()
print("สร้างรูปภาพตารางรถไฟสำเร็จแล้ว ชื่อไฟล์: election_train_table.png")
