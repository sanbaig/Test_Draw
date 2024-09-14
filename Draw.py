import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def draw_text(ax, text, x, y):
    bbox_props = dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue")
    ax.text(x, y, text, ha="center", va="center", size=12, bbox=bbox_props)

def draw_arrow(ax, start, end):
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color="black"))

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Hide axes
ax.axis('off')

# Draw nodes (boxes)
draw_text(ax, "传感器输入\n- 按压位置 x\n- 按压时间 t", 5, 8)
draw_text(ax, "处理输入数据\n- 计算位置和时间\n- 确定电机和时长", 5, 5)
draw_text(ax, "输出控制信号\n- 发送信号给电机", 5, 2)

# Draw arrows
draw_arrow(ax, (5, 7.5), (5, 6.5))
draw_arrow(ax, (5, 4.5), (5, 3.5))

plt.show()

##测试上传github
