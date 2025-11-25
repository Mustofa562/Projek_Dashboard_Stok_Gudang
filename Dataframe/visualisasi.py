import matplotlib.pyplot as plt

def show_bar(df):
    plt.bar(df["Produk"], df["Stok"], color='orange')
    plt.title("Grafik Stok Barang")
    plt.show()


def show_pie(df):
    plt.pie(df["Total Nilai (Rp)"], labels=df["Produk"], autopct="%1.1f%%")
    plt.title("Persentase Nilai Barang")
    plt.show()
