import streamlit as st
from datetime import datetime, timedelta
import time

# Title of the app
st.title("A countdown app designed for you")

# Input for the target date
target_date_input = st.text_input("Make a countdown baby! (YYYY-MM-DD):")

if target_date_input:
    try:
        # Parse the target date
        target_date = datetime.strptime(target_date_input, "%Y-%m-%d")
        now = datetime.now()
        remaining_time = target_date - now

        if remaining_time.total_seconds() <= 0:
            st.subheader("Time's up!")
        else:
            # Display the countdown in real-time
            st.subheader("Time Remaining:")
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

                # Update the digital clock display
                countdown_placeholder.markdown(f"""
                ### {days} Days  
                ## {int(hours):02}:{int(minutes):02}:{int(seconds):02}
                """)

                time.sleep(1)  # Update every second

            # When time is up
            countdown_placeholder.markdown("### Time's up!")
    except ValueError:
        st.error("Invalid date format! Please enter the date in YYYY-MM-DD.")
