import streamlit as st
import time
from agents.decision_analyzer import analyze_decision
from agents.eulogy_writer import write_eulogy
from agents.graveyard_tour import show_cemetery

# --- Page Config ---
st.set_page_config(page_title="RegretGPT", page_icon="⚰️", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚰️ RegretGPT")
st.write("### The Cemetery of Your Life Choices")
st.info("The AI Agent that roasts your logic and buries your regrets.")

# --- Sidebar for the Graveyard Tour ---
with st.sidebar:
    st.header("🕯️ The Cemetery Gates")
    if st.button("Visit the Cemetery"):
        st.session_state.view_graveyard = True
    if st.button("Bury a New Decision"):
        st.session_state.view_graveyard = False

# --- Main Logic ---
if 'view_graveyard' not in st.session_state or not st.session_state.view_graveyard:
    decision = st.text_area("Tell me a decision you made:",
                            placeholder="e.g., I bought crypto because a lizard told me to.")

    if st.button("Submit to Judgment"):
        if decision:
            with st.status("Performing Autopsy...", expanded=True) as status:
                st.write("🧠 Reviewing the damage...")
                analysis = analyze_decision(decision)

                st.write("📜 Preparing the funeral service...")
                eulogy = write_eulogy(decision, analysis)

                time.sleep(1)
                status.update(label="Burial Complete!", state="complete", expanded=False)

            # --- Display Results ---
            st.subheader("🧠 The Autopsy")
            st.write(analysis)

            st.divider()

            st.subheader("⚰️ The Eulogy")
            st.markdown(f"*{eulogy}*")

            # Note: On a live server, local file writing (graveyard.json)
            # works but resets when the app redeploys.
        else:
            st.warning("You must provide a sacrifice (a decision).")

else:
    st.subheader("🕯️ Tour of the Cemetery")
    # We call your existing logic (you might need to tweak show_cemetery to return text instead of printing)
    # For now, let's keep it simple:
    st.write("Checking the graves...")
    # [Note: For a better UI, we'd loop through graveyard.json here and use st.expander]