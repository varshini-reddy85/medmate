import streamlit as st
from datetime import datetime
import json
import os
from PIL import Image

# Load existing reminders
def load_reminders():
    if os.path.exists("reminders.json"):
        with open("reminders.json", "r") as file:
            return json.load(file)
    return []

# Save reminders to JSON
def save_reminders(reminders):
    with open("reminders.json", "w") as file:
        json.dump(reminders, file, indent=4)

# Create images folder if not exists
if not os.path.exists("images"):
    os.makedirs("images")

# UI
st.title("💊 MedMate: Personal Medicine Reminder")

# Reminder form
with st.form("reminder_form"):
    name = st.text_input("Medicine Name")
    dosage = st.text_input("Dosage (e.g:2 pills)")
    time = st.time_input("Reminder Time")
    image = st.file_uploader("Upload Medicine Photo", type=["jpg", "jpeg", "png"])
    submitted = st.form_submit_button("Set Reminder")

    if submitted:
        image_filename = None
        if image is not None:
            image_filename = f"images/{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            with open(image_filename, "wb") as f:
                f.write(image.read())

        reminders = load_reminders()
        reminders.append({
            "name": name,
            "dosage": dosage,
            "time": time.strftime("%H:%M"),
            "image": image_filename
        })
        save_reminders(reminders)
        st.success("✅ Reminder set successfully!")

# Display reminders
st.subheader("📅 Your Reminders:")
reminders = load_reminders()
if reminders:
    for r in reminders:
        st.markdown(f"**🕒 {r['time']}**")
        st.markdown(f"- **Medicine:** {r['name']}")
        st.markdown(f"- **Dosage:** {r['dosage']}")
        if r["image"]:
            st.image(r["image"], width=150)
        st.markdown("---")
else:
    st.info("No reminders yet.")
