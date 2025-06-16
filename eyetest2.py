import streamlit as st

# Chart data
eye_chart_rows = [
    {"text": "E", "size": 100, "distance": "60 meters"},
    {"text": "FP", "size": 80, "distance": "36 meters"},
    {"text": "TOZ", "size": 60, "distance": "24 meters"},
    {"text": "LPED", "size": 45, "distance": "18 meters"},
    {"text": "PECFD", "size": 35, "distance": "12 meters"},
    {"text": "EDFCZP", "size": 25, "distance": "9 meters"},
    {"text": "FELOPZD", "size": 20, "distance": "6 meters"},
    {"text": "DEFPOTEC", "size": 15, "distance": "5 meters"},
    {"text": "LEFODPEC", "size": 12, "distance": "4 meters"},
]

# Page setup
st.set_page_config(page_title="👓 Eye Test App", layout="centered")
st.markdown("<h1 style='text-align:center;'>👓 Online Vision Check</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>A fun and simple way to check your visual clarity from your screen.</p>", unsafe_allow_html=True)
st.divider()

st.info("📏 Ideal screen distance: about 50 cm (arm's length) for accurate testing.")

# Input fields for each row
user_answers = []
with st.form("eye_test_form"):
    for i, row in enumerate(eye_chart_rows):
        st.markdown(
            f"<div style='font-size:{row['size']}px; text-align:center; margin: 20px 0;'>{row['text']}</div>",
            unsafe_allow_html=True
        )
        answer = st.text_input(f"🔎 Line {i+1} (Should be readable at {row['distance']}):", key=f"line_{i}")
        user_answers.append(answer)

    submitted = st.form_submit_button("🚀 Submit Test")

# After submission: evaluate answers
if submitted:
    correct_lines = 0
    for i, row in enumerate(eye_chart_rows):
        if user_answers[i].strip().upper() == row["text"]:
            correct_lines += 1

    st.divider()
    st.subheader("🧠 Your Vision Result")
    st.info(f"✅ You correctly identified *{correct_lines}* out of *{len(eye_chart_rows)}* lines.")

    # Suggestion-based feedback
    if correct_lines == 0:
        st.error("⚠ You couldn't read any lines.")
        st.warning("👁 This may indicate serious vision problems. Please consult an eye specialist.")
    elif correct_lines <= 2:
        st.warning("👓 Your vision seems poor. It is strongly recommended to visit an optometrist.")
    elif correct_lines <= 5:
        st.info("🧐 Your vision may be below average. Consider reducing screen time and checking lighting.")
    elif correct_lines <= 7:
        st.success("👍 Your vision appears normal, but test regularly to ensure consistency.")
    else:
        st.balloons()
        st.success("🎯 Excellent! You have strong visual clarity. Keep caring for your eyes!")

    st.caption("🧪 This is a simple visual simulation.")  