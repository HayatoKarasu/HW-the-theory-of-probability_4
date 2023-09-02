from matplotlib import pyplot as plt

def show():
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()


plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "1) У нас есть колода из 36 карт (4 масти и 9 номенал), Вытянули", fontsize=15)
plt.text(0.01, 0.8, "одну карту (вероятности вытягивания отдельной карты равны).", fontsize=15)
plt.text(0.01, 0.7, "Определить следующие случайные величины:", fontsize=15)
plt.text(0.01, 0.6, "ξ - масть: 0 - червы, 1 - пики, 2 - крести, 3 - бубны.", fontsize=15)
plt.text(0.01, 0.5, "η: принимает значение 0 если выпала 6, 7, 8, 9, 10 или 1 если", fontsize=15)
plt.text(0.01, 0.4, "валет, дама, король, туз.", fontsize=15)
plt.text(0.01, 0.3, "Для доказательства, что ξ и η независимы требуется рассмотреть", fontsize=15)
plt.text(0.01, 0.2, "все α и β и проверить выполнение равенства:", fontsize=15)
form = r"$P((\xi \leq \alpha) \bigcap (\eta \leq \beta)) = P(\xi \leq \alpha) * P(\eta \leq \beta)$"
plt.text(0.01, 0.1, form, fontsize=15)

show()

plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "Для примера рассмотрим α = 0, β = 0. Остальное аналогично.", fontsize=15)
form = r"$P((\xi \leq 0) \bigcap (\eta \leq 0)) = 5/36; P(\xi \leq 0) * P(\eta \leq 0) = 5/36$"
plt.text(0.01, 0.8, form, fontsize=15)
plt.text(0.01, 0.7, "2) Вероятность брака = 0,2. Определить вероятность в партии из", fontsize=15)
plt.text(0.01, 0.6, "10 деталей ровно k будут без брака. Решить для k = 0, 1, 3, 10", fontsize=15)
plt.text(0.01, 0.5, "Для решения используем схему Бернулли. p = 1 - 0,2 = 0,8", fontsize=15)
form = r"$P_10(0) = C_{10}^0 p^0 (1-p)^{10-0} = \frac{10!}{0! 10!} 0,8^0 0,2^10 \approx 10^{-7}$"
plt.text(0.01, 0.4, form, fontsize=15)
form = r"$P_10(1) = C_{10}^1 p^1 (1-p)^{10-1} = \frac{10!}{1! 9!} 0,8^1 0,2^9 \approx 4*10^{-6}$"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$P_10(3) = C_{10}^3 p^3 (1-p)^{10-3} = \frac{10!}{3! 7!} 0,8^3 0,2^7 \approx 8*10^{-4}$"
plt.text(0.01, 0.2, form, fontsize=15)
form = r"$P_10(10) = C_{10}^{10} p^{10} (1-p)^0 = \frac{10!}{10! 0!} 0,8^{10} 0,2^0 \approx 0,1$"
plt.text(0.01, 0.1, form, fontsize=15)

show()