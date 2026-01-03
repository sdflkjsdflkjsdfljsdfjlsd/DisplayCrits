import streamlit as st
import os

def get_all_mech_files():
    """Returns a list of all .txt files in the directory."""
    return [f for f in os.listdir('.') if f.endswith('.txt')]

def display_mech_content(filename):
    """Reads and displays the content of the selected Mech file."""
    with open(filename, "r") as f:
        content = f.read()
    
    st.success(f"Displaying data for: **{filename}**")
    st.subheader("Critical hits")
    
    # Simple code block display for the raw MTF format
    st.code(content, language="text")

# --- Streamlit UI ---
st.set_page_config(page_title="Mech Database", page_icon="🤖")

st.title("Alpha Strike Custom Crit Tables")
st.write("Enter a name or model (e.g., 'Crab' or 'KGC').")

# 1. User Input
user_query = st.text_input("Search Mechs:", key="search_input").strip().lower()

if user_query:
    # 2. Find all matches
    all_files = get_all_mech_files()
    matches = [f for f in all_files if user_query in f.lower()]

    if not matches:
        st.error(f"No results found for '{user_query}'.")
    
    elif len(matches) == 1:
        # If only one match, show it immediately
        display_mech_content(matches[0])
        
    else:
        # 3. If multiple matches, show a selection dropdown
        st.info(f"Found {len(matches)} matches. Please select one:")
        selected_file = st.selectbox("Select the correct Mech:", matches)
        
        if selected_file:
            display_mech_content(selected_file)

# Footer info
st.sidebar.markdown("### How to use\nUpload your `.txt` files to the main GitHub folder. The app scans them automatically.")
