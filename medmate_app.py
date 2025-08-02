import streamlit as st
from datetime import datetime, time

# App title
st.title("💊 MedMate - Personal Medicine Reminder App")

# Session state to store reminders
if 'reminders' not in st.session_state:
    st.session_state.reminders = []

# 📸 Upload Medicine Photo
st.subheader("📷 Upload Medicine Photo (Optional)")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Medicine Preview", width=150)

# Reminder input
st.subheader("🔔 Set a Reminder")
reminder_time = st.time_input("Select time:", value=datetime.now().time())
reminder_message = st.text_input("Enter medicine name or reminder message")

# Add reminder
if st.button("Add Reminder"):
    if reminder_message:
        st.session_state.reminders.append({
            "time": reminder_time.strftime("%I:%M %p"),
            "message": reminder_message
        })
        st.success("Reminder added!")
    else:
        st.warning("Please enter a reminder message.")

# Display current reminders
if st.session_state.reminders:
    st.subheader("⏰ Your Reminders")
    for i, rem in enumerate(st.session_state.reminders):
        st.write(f"🕒 **{rem['time']}** - {rem['message']}")
        if st.button(f"Delete Reminder {i+1}", key=f"delete_{i}"):
            st.session_state.reminders.pop(i)
            st.success("Reminder deleted.")
            st.experimental_rerun()
else:
    st.info("No reminders added yet.")
