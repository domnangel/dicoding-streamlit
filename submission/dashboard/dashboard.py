import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib.dates import MonthLocator

# Data
main_df = pd.read_csv("C:/Users/Sheila/Documents/SMK/PKL/DB Dicoding/submission/dashboard/main_data.csv")
tipe_datetime_kedua = ["dteday"]
for tipe in tipe_datetime_kedua:
    main_df[tipe] = pd.to_datetime(main_df[tipe])
    
data_2012 = main_df[main_df["dteday"].dt.year == 2012]

# Dashboard

st.title("Bike Sharing Dashboard :bike: :sparkles:")
st.subheader("Data-Data About Bike Sharing was Displayed Here")
st.markdown(
    """
    ## NOTE
    Go to every tab to see every displayed chart
    """
)

st.subheader("Bike Sharing Performance")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Data 1",
    "Data 2",
    "Data 3",
    "Data 4",
    "Data 5",
])

with tab1:
    # Chart 1
    st.subheader("Per Day")
    fig, ax = plt.subplots(figsize = (20, 10))
    ax.plot(
        data_2012["dteday"],
        data_2012["cnt"],
        marker = "o",
        linewidth = 2,
        color = "#3876BF")
    ax.set_title("Number of Bike Rental per Day (in 2012)",
              loc = "center",
              fontsize = "30")

    axs = plt.gca()
    axs.xaxis.set_major_locator(MonthLocator(interval=1))

    ax.tick_params(axis="x", labelsize=15)
    ax.tick_params(axis="y", labelsize=15)
    st.pyplot(fig)

    # Chart 2
    st.subheader("Per Month")
    fig, ax = plt.subplots(figsize = (20, 10))
    monthly_df = main_df.resample("M", on="dteday").sum()
    data_2012 = monthly_df[monthly_df.index.year == 2012]

    ax.plot(
        data_2012.index,
        data_2012["cnt"],
        marker = "o",
        linewidth = 2,
        color = "#3876BF")
    ax.set_title("Number of Bike Rental per Month (in 2012)",
              loc = "center",
              fontsize = "30")

    axs = plt.gca()
    axs.xaxis.set_major_locator(MonthLocator(interval=1))

    ax.tick_params(axis="x", labelsize=15)
    ax.tick_params(axis="y", labelsize=15)
    plt.ylim(ymin=0)
    st.pyplot(fig)

with tab2:
    st.subheader("From 2011 to 2012")
    fig, ax = plt.subplots(figsize = (20, 10))
    monthly_df = main_df.resample("M", on="dteday").sum()
    range_df = monthly_df[(monthly_df.index >= "2011-09") &
                          (monthly_df.index <= "2012-04")]

    ax.plot(
        range_df.index,
        range_df["cnt"],
        marker = "o",
        linewidth = 2,
        color = "#3876BF")
    ax.set_title("Number of Bike Rental from 2011 to 2012",
              loc = "center",
              fontsize = "30")

    ax.tick_params(axis="x", labelsize=15)
    ax.tick_params(axis="y", labelsize=15)
    plt.ylim(ymin=0)
    st.pyplot(fig)

with tab3:
    st.subheader("Percentage Per Day")
    fig, ax = plt.subplots(figsize = (7, 5))
    perday_df = main_df.groupby("weekday")["cnt"].sum()
    colors = ["#00B8D9", "#7649FE", "#5643FD", "#BA1E68", "#D244D9", "#9C27B0", "#E81E63"]
    
    plt.pie(
        x = perday_df,
        labels = perday_df.index,
        colors = colors,
        autopct = "%1.1f%%",
        explode = (0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03)
    )

    ax.set_title("Percentage of Bike Sharing (per day)")
    st.pyplot(fig)

with tab4:
    st.subheader("Based on Season")
    season_df = main_df.groupby('season')
    rental_in_seasons = season_df['cnt'].sum().reset_index()
    
    fig, ax = plt.subplots(figsize = (20, 10))
    color = ["#190482", "#C2D9FF", "#C2D9FF", "#C2D9FF"]
    
    sns.barplot(
        x = "season",
        y = "cnt",
        data = rental_in_seasons,
        palette = color
    )
    
    ax.set_title("Season with the Highest Number of Bike Rentals",
              fontsize = 30)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.tick_params(axis="x", labelsize=20)
    ax.tick_params(axis="y", labelsize=15)
    ax.ticklabel_format(style='plain', axis = "y")
    st.pyplot(fig)

with tab5:
    st.subheader("Based on Temperature and Wind Speed")
    fig, ax = plt.subplots(figsize = (15, 7))
    sns.scatterplot(
        data = main_df,
        x = "temp",
        y = "windspeed",
        hue = "cnt")
    ax.set_title("Number of Bike Rental (Temperature and Wind Speed)",
                 fontsize=20)
    st.pyplot(fig)

st.caption("Copyright :copyright: Sheila Alvita 2023 (Dicoding Submission)")