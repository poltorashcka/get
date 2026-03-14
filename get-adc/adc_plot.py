from matplotlib import pyplot as plt

def plt_vol_vs_time(time, vol, max_vol):
    plt.figure(figsize=(10,6))
    plt.plot(time, vol)
    plt.title("voltage vs time")
    plt.xlabel("time")
    plt.ylabel("voltage")
    plt.grid()
    plt.show()

def plot_samp_per_h(time):
    t = []
    for i in range(1, len(time)):
        t.append(time[i] - time[i-1])
    plt.figure(figsize=(10,6))
    plt.hist(t)
    plt.title("hist num of measures vs samp rate")
    plt.xlabel("num of measures")
    plt.ylabel("samp rate")
    plt.xlim(0, 2)
    plt.grid()
    plt.show()

