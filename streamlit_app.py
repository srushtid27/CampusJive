import streamlit as st

# Database setup
conn = sqlite3.connect("database.db")
c = conn.cursor()

st.set_page_config(page_title="College Events Portal")

# Navigation
menu = ["Home", "Login", "Register", "Events", "My Tickets", "Media Gallery", "Admin Panel"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.title("🎉 Welcome to College Events Portal")
    st.write("Register for events, make payments, and access media here.")

elif choice == "Register":
    st.subheader("Student Registration")
    # take inputs and insert into DB

elif choice == "Login":
    st.subheader("Login")
    # authenticate user and set session_state

elif choice == "Events":
    st.subheader("Available Events")
    # fetch from DB and show register button

elif choice == "My Tickets":
    st.subheader("Your Tickets")
    # show downloadable QR tickets

elif choice == "Media Gallery":
    st.subheader("Photos & Videos")
    # fetch and display media

elif choice == "Admin Panel":
    st.subheader("Admin Dashboard")
    # add/manage events, view registrations, upload media
