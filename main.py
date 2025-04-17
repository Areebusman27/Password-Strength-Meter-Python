import streamlit as st
import string

# Title with style
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔒 PASSWORD STRENGTH METER</h1>", unsafe_allow_html=True)

# Input field
input_password = st.text_input("🔑 Enter your password")

# Special characters set
special_characters = set(string.punctuation)

# Initialize score
score = 0

# Check Score button
if st.button('✅ Check Score'):
    if len(input_password) >= 8:
        score += 1
    else:
        st.error('❌ Password must have at least 8 characters')

    if any(char.isupper() for char in input_password):
        score += 1
    else:
        st.error("❌ Password must have uppercase letters")

    if any(char.islower() for char in input_password):
        score += 1
    else:
        st.error("❌ Password must have lowercase letters")

    if any(char.isdigit() for char in input_password):
        score += 1
    else:
        st.error("❌ Password must have digits")

    if any(char in special_characters for char in input_password):
        score += 1
    else:
        st.error("❌ Password must have special characters")

    # Results
    st.markdown("---")
    if score == 5:
        st.success('✅ Your password is **strong** 🔥')
    elif score == 4:
        st.success("✅ Your password is **moderately strong** 👍")
    elif score == 3:
        st.warning('⚠️ Your password is **weak**')
    else:
        st.error("🚫 Reset your password. It is **very weak**")

# Footer
st.markdown("<small style='color:gray;'>Made with ❤️ using Streamlit</small>", unsafe_allow_html=True)
