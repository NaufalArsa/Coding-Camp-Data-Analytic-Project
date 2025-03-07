import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("..\data\day.csv")
hour_df = pd.read_csv("..\data\hour.csv")

# Mapping untuk season dan weathersit
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
weather_map = {1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'}

day_df['season'] = day_df['season'].map(season_map)
day_df['weathersit'] = day_df['weathersit'].map(weather_map)

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Streamlit UI setup
st.set_page_config(page_title="Bike Rental Dashboard", layout="wide")

st.title('🚴‍♂️ Bike Rental Dashboard')

# Sidebar untuk filter
st.sidebar.header("📊 Filter Data")
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", 
                                   [day_df["dteday"].min(), day_df["dteday"].max()],
                                   min_value=day_df["dteday"].min(), 
                                   max_value=day_df["dteday"].max())

selected_season = st.sidebar.multiselect("Pilih Musim", 
                                         options=day_df["season"].unique(), 
                                         default=day_df["season"].unique())

selected_weather = st.sidebar.multiselect("Pilih Kondisi Cuaca", 
                                          options=day_df["weathersit"].unique(), 
                                          default=day_df["weathersit"].unique())

# Filter dataset
filtered_df = day_df[
    (day_df["dteday"] >= pd.to_datetime(date_range[0])) & 
    (day_df["dteday"] <= pd.to_datetime(date_range[1])) & 
    (day_df["season"].isin(selected_season)) & 
    (day_df["weathersit"].isin(selected_weather))
]

# Menampilkan Metrics
col1, col2, col3 = st.columns(3)
col1.metric("📅 Total Penyewaan", f"{filtered_df['cnt'].sum():,}")
col2.metric("🔄 Rata-rata Penyewaan Harian", f"{filtered_df['cnt'].mean():,.2f}")
col3.metric("📊 Hari Tertinggi", filtered_df.loc[filtered_df['cnt'].idxmax(), 'dteday'].strftime('%Y-%m-%d'))

# Menggunakan Tabs
tab1, tab2, tab3 = st.tabs(["📈 Tren Penyewaan", "📊 Distribusi Data", "📌 Analisis Tambahan"])

with tab1:
    st.subheader("📅 Rata-rata Penyewaan Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(8,5)) 
    sns.barplot(x="season", y="cnt", data=filtered_df, palette="Blues", ax=ax)
    ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    st.caption("Insight: Jumlah penyewa paling banyak terjadi pada musim Fall dengan total 1.061.129 penyewa dengan rata-rata setiap harinya 5644 penyewa.")

    st.subheader('🧮 Total Penyewaan Sepeda: Hari Kerja vs Hari Libur')
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x='workingday', y='cnt', data=day_df, estimator=sum, color="blue")  # Total sebagai background
    sns.barplot(x='workingday', y='casual', data=day_df, estimator=sum, color="blue", label="Casual")
    sns.barplot(x='workingday', y='registered', data=day_df, estimator=sum, color="red", label="Registered")
    ax.set_title("Total Penyewaan Sepeda: Hari Kerja vs Hari Libur")
    ax.set_xticks([0,1], ['Hari Libur', 'Hari Kerja'])
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Jumlah Penyewa")
    st.pyplot(fig)
    st.caption("Insight: Jumlah penyewa paling banyak terjadi pada hari kerja yaitu sebanyak 2.292.410 penyewa. Selain itu, jenis penyewa dengan jumlah paling banyak adalah registered")

with tab2:
    st.subheader("⛅ Distribusi Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x="weathersit", y="cnt", data=filtered_df, palette="coolwarm", ax=ax)
    ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Cuaca")
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    st.caption("Insight: Jumlah penyewa paling banyak terjadi pada cuaca Clear, Few clouds, Partly cloudy, Partly cloudy dengan total 2.257.952 penyewa dengan rata-rata setiap harinya 4876 penyewa.")

    st.subheader('📊 Distribusi Jumlah Penyewaan Sepeda Harian')
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(day_df['cnt'], bins=30, kde=True, color="blue", ax=ax)
    ax.set_title("Distribusi Jumlah Penyewaan Sepeda Harian")
    ax.set_xlabel("Jumlah Penyewaan")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)
    st.caption("Insight: Data jumlah penyewaan sepeda harian cenderung berdistribusi normal.")
    
    st.subheader("📊 Penyewaan Sepeda Berdasarkan Jam")
    fig, ax = plt.subplots(figsize=(12,6))
    sns.boxplot(x="hr", y="cnt", data=hour_df, palette="viridis", ax=ax)
    ax.set_title("Boxplot Penyewaan Sepeda Berdasarkan Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    st.caption("Insight: Terdapat data outlier yang disebabkan banyaknya penyewa pada jam sibuk, yaitu mulai dari siang-sore.")
    
with tab3:
    st.subheader("⚙️ Kategori Penyewaan Sepeda")
    bins = [0, 2000, 4000, 7000]  
    labels = ['Low', 'Medium', 'High']
    day_df['rental_category'] = pd.cut(day_df['cnt'], bins=bins, labels=labels)
    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(x="rental_category", data=day_df, ax=ax)
    ax.set_xlabel("Kategori Penyewaan")
    ax.set_ylabel("Jumlah")
    ax.set_title("Kategori Penyewaan Sepeda")
    st.pyplot(fig)
    st.caption("Insight: Sebagai analisis tambahan, menggunakan teknik clustering (binning), kita bisa mengelompokkan hari dengan penyewaan rendah, sedang, atau tinggi untuk optimasi layanan.")

    st.subheader("📑 Recency, Frequency, Monetary (RFM) Analysis")
    max_date = day_df['dteday'].max()
    day_df['Recency'] = (max_date - day_df['dteday']).dt.days
    day_df['Frequency'] = 1 
    day_df['Monetary'] = day_df['cnt']
    rfm_df = day_df[['dteday', 'Recency', 'Frequency', 'Monetary']]
    st.write(rfm_df.head())
    st.caption("Insight: Sebagai analisis tambahan, RFM Analysis berfungsi untuk digunakan dalam analisa customer segmentation.")
