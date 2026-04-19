import tkinter as tk
import random
import math
import sys

h, a = [], []
t = ['多喝水哦~', '好好爱自己', '好好吃饭', '保持好心情', '我想你了', '顺顺利利', '别熬夜', '天冷了多穿衣服', '要开心哦', '注意休息']
c = ['pink', 'lightblue', 'lightgreen', 'lemonchiffon', 'hotpink', 'skyblue', 'lightcoral', 'paleturquoise', 'mistyrose', 'khaki']

def g(n, w, h):
    """生成爱心形状的点"""
    p = []
    for i in range(n):
        th = i / n * 2 * math.pi
        x = 16 * math.sin(th) ** 3
        y = 13 * math.cos(th) - 5 * math.cos(2 * th) - 2 * math.cos(3 * th) - math.cos(4 * th)
        sx = int(w / 2 + x * 20 - 50)
        sy = int(h / 2 - y * 20 - 80)
        p.append((max(0, min(sx, w - 150)), max(0, min(sy, h - 40))))
    return p

def cw(x, y, tip=None, is_h=True):
    """创建窗口"""
    w = tk.Toplevel()
    w.geometry(f"150x40+{x}+{y}")
    w.title('提示')
    w.attributes('-topmost', 1)
    w.overrideredirect(1)  # 无边框窗口
    
    color = random.choice(c)
    text = tip if tip else random.choice(t)
    
    label = tk.Label(w, text=text, bg=color, font=('微软雅黑', 14), width=15, height=2)
    label.pack(fill='both', expand=True)
    
    # 点击关闭单个窗口
    label.bind('<Button-1>', lambda e: w.destroy())
    
    return w

def m():
    """主函数"""
    r = tk.Tk()
    r.withdraw()
    sw, sh = r.winfo_screenwidth(), r.winfo_screenheight()
    n = 100  # 窗口数量
    
    # 生成爱心形状的窗口
    points = g(n, sw, sh)
    for i, (x, y) in enumerate(points):
        is_last = i == n - 1
        tip = "王乐君 ❤️ 我爱你" if is_last else None
        w = cw(x, y, tip)
        h.append(w)
    
    # 空格键关闭所有窗口
    def close_all(event):
        for win in h:
            try:
                win.destroy()
            except:
                pass
        r.quit()
        sys.exit()
    
    r.bind('<space>', close_all)
    for win in h:
        win.bind('<space>', close_all)
    
    # 提示窗口
    tip_win = tk.Toplevel()
    tip_win.geometry(f"200x30+{sw//2-100}+{sh-60}")
    tip_win.attributes('-topmost', 1)
    tip_win.overrideredirect(1)
    tk.Label(tip_win, text="按空格键关闭所有窗口", bg='white', fg='gray', font=('微软雅黑', 10)).pack(fill='both')
    tip_win.bind('<space>', close_all)
    
    r.mainloop()

if __name__ == '__main__':
    m()
