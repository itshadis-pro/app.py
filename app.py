import streamlit as st
from datetime import datetime

# Title of the app
st.title("Countdown Timer")

# Input for the target date
target_date_input = st.text_input("Enter the target date (YYYY-MM-DD):")

if target_date_input:
    try:
        # Parse the target date
        target_date = datetime.strptime(target_date_input, "%Y-%m-%d")
        now = datetime.now()
        remaining_time = target_date - now

        if remaining_time.total_seconds() <= 0:
            st.subheader("Time's up!")
        else:
            # Calculate days, hours, minutes, and seconds
            days = remaining_time.days
            hours, remainder = divmod(remaining_time.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)

            # Display the countdown
            st.subheader("Time Remaining:")
            st.write(f"**Days:** {days}")
            st.write(f"**Hours:** {int(hours) % 24}")
            st.write(f"**Minutes:** {int(minutes)}")
            st.write(f"**Seconds:** {int(seconds)}")
    except ValueError:
        st.error("Invalid date format! Please enter the date in YYYY-MM-DD.")
