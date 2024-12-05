import streamlit as st
from datetime import datetime, timedelta
import time

# Title with romantic emojis
st.markdown(
    "<h1 style='text-align: center; color: pink;'>💖 Countdown to Our Special Day 💖</h1>",
    unsafe_allow_html=True,
)

# Input for the target date
st.markdown("### 🥰 Enter the date you're looking forward to, my love! (YYYY-MM-DD):")
target_date_input = st.text_input("")

# Background color customization
page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ffe4e1;
    background-image: url("https://i.pinimg.com/originals/1e/4d/c3/1e4dc343bdf379b776fef360bf5b5f01.jpg");
    background-size: cover;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

if target_date_input:
    try:
        # Parse the target date
        target_date = datetime.strptime(target_date_input, "%Y-%m-%d")
        now = datetime.now()
        remaining_time = target_date - now

        if remaining_time.total_seconds() <= 0:
            st.markdown(
                "<h2 style='text-align: center; color: red;'>💘 It's time! Make it unforgettable! 💘</h2>",
                unsafe_allow_html=True,
            )
        else:
            # Display the countdown in real-time
            st.markdown("<h2 style='text-align: center;'>⏳ Time Remaining:</h2>", unsafe_allow_html=True)
            countdown_placeholder = st.empty()

            while remaining_time.total_seconds() > 0:
                now = datetime.now()
                remaining_time = target_date - now

                # Calculate days, hours, minutes, and seconds
                total_seconds = remaining_time.total_seconds()
                days = remaining_time.days
                hours = (total_seconds // 3600) % 24
                minutes = (total_seconds // 60) % 60
                seconds = total_seconds % 60

                # Update the countdown with romantic formatting
                countdown_placeholder.markdown(f"""
                <div style='text-align: center; font-size: 24px;'>
                    <p style='font-size: 40px; color: #ff69b4;'>💝 {days} Days 💝</p>
                    <p style='font-size: 36px; color: #ff1493;'>💓 {int(hours):02}:{int(minutes):02}:{int(seconds):02} 💓</p>
                </div>
                """, unsafe_allow_html=True)

                time.sleep(1)  # Update every second

            # When time is up
            countdown_placeholder.markdown(
                "<h2 style='text-align: center; color: red;'>🎉 The wait is over! Celebrate your love! 🎉</h2>",
                unsafe_allow_html=True,
            )
    except ValueError:
        st.error("Invalid date format! Please enter the date in YYYY-MM-DD.")

