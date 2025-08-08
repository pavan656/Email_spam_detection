import streamlit as st
import pickle

# Load the model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

# Page Config
st.set_page_config(page_title="Spam or Not?", page_icon="✉️", layout="centered")

# Main Title Section
st.title("✉️ Spam Detector")
st.subheader("Is that email real or a scam? Let's find out!")
st.caption("An ML-based tool to help you classify emails as **Spam** or **Not Spam**")

# Sidebar Info
with st.sidebar:
    st.header("ℹ️ About This App")
    st.write("This app uses a machine learning model trained on labeled email data to classify email content.")
    st.markdown("""
    **Steps to use:**
    1. Paste the email content in the input box.
    2. Click on 'Analyze'.
    3. View the prediction and safety advice.
    """)
    st.write("---")
    st.markdown("🛡️ Stay cautious and secure your inbox!")

# Email Input Section
with st.container():
    st.markdown("### 📝 Paste Your Email Below")
    user_input = st.text_area(
        "Email Content:",
        height=180,
        placeholder="e.g., Congratulations! You've been selected for a cash reward. Click to claim now..."
    )

# Analyze Button and Prediction
if st.button("🔍 Analyze Email"):
    if user_input.strip():
        st.markdown("### 📢 Prediction")

        # Process and Predict
        data = [user_input]
        vectorized_data = cv.transform(data).toarray()
        prediction = model.predict(vectorized_data)

        if prediction[0] == 0:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.success("✅ Legitimate Email")
            with col2:
                st.markdown("""
                - You may proceed to read or respond.  
                - Always double-check the sender's details.  
                """)
        else:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.error("🚫 Spam Email Detected")
            with col2:
                st.markdown("""
                - Avoid clicking links or downloading attachments.  
                - Report this email if you're unsure of the sender.  
                """)

    else:
        st.warning("⚠️ Please provide some email content before analyzing.")

# Footer
st.divider()
st.markdown("### 📌 Email Security Tips")
st.markdown("""
- Never share personal info via email.  
- Look for suspicious domain names or strange formatting.  
- Use a reliable spam filter and keep your antivirus updated.  
""")
st.markdown("Developed with ❤️ by **Soppa Sruthi**")
