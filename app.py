import streamlit as st
from auth import login_user, signup_user
from profile_setup import profile_setup_page
from dashboard import dashboard_page


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Personal Skill Gap Analyzer Returns",
    layout="wide"
)


# -----------------------------
# CUSTOM THEME STYLING
# -----------------------------
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE INITIALIZATION
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "profile_completed" not in st.session_state:
    st.session_state.profile_completed = False

if "username" not in st.session_state:
    st.session_state.username = ""


# -----------------------------
# MAIN APP FUNCTION
# -----------------------------
def main():
    st.title("AI Personal Skill Gap Analyzer")
    st.markdown("### Discover careers, identify skill gaps, and grow beautifully.")


    # -----------------------------
    # LOGIN / SIGNUP
    # -----------------------------
    if not st.session_state.logged_in:

        menu = st.sidebar.radio(
            "Choose Option",
            ["Login", "Signup"]
        )

        if menu == "Login":
            st.subheader("Login to Your Account")

            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                success = login_user(username, password)

                if success:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

        elif menu == "Signup":
            st.subheader("Create New Account")

            new_username = st.text_input("Create Username")
            new_email = st.text_input("Email")
            new_password = st.text_input("Create Password", type="password")

            if st.button("Signup"):
                success = signup_user(
                    new_username,
                    new_email,
                    new_password
                )

                if success:
                    st.success("Signup successful! Please login.")
                else:
                    st.error("Username already exists.")


    # -----------------------------
    # PROFILE SETUP
    # -----------------------------
    elif not st.session_state.profile_completed:
        profile_setup_page()


    # -----------------------------
    # MAIN DASHBOARD
    # -----------------------------
    else:
        dashboard_page(st.session_state.username)


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    main()