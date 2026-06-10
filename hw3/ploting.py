import matplotlib.pyplot as plt
import os
import numpy as np

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 拼接文件路径
file_path = os.path.join(script_dir, 'hubble29.csv')

data = np.genfromtxt(file_path, delimiter=',', names=True, dtype=None, encoding='utf-8')


d = data['distance']   # 距离 (Mpc)
v = data['velocity']   # 速度 (km/s)

# === 2. 线性回归（Hubble 1929）===
# v = H0 * d + b
H0_fit, b_fit = np.polyfit(d, v, 1)

# === 3. 现代值直线 ===
H0_modern = 70  # km/s/Mpc

# === 4. 生成拟合线数据 ===
d_line = np.linspace(0, max(d)*1.1, 100)

v_fit = H0_fit * d_line + b_fit
v_modern = H0_modern * d_line

# === 5. 作图 ===
plt.figure(figsize=(8,6))

# 数据点
plt.scatter(d, v, label='Hubble (1929) Data')

# 拟合直线
plt.plot(d_line, v_fit, linestyle='--',
         label=f'Hubble Fit: v = {H0_fit:.1f} d + {b_fit:.1f}')

# 现代值直线
plt.plot(d_line, v_modern, linestyle='-',
         label=f'Modern Value: v = {H0_modern} d')

# === 6. 标注与美化 ===
plt.xlabel('Distance (Mpc)')
plt.ylabel('Velocity (km/s)')
plt.title('Hubble (1929) Data and Modern Comparison')

plt.legend()
plt.grid()

# === 7. 保存图像（用于交作业）===
plt.savefig('hubble_plot.png', dpi=300)

# 显示图像
plt.show()

# === 8. 输出Hubble常数 ===
print(f"Hubble (1929) fitted H0 = {H0_fit:.2f} km/s/Mpc")