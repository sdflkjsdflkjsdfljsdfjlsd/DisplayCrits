import streamlit as st
import os


def load_mech_data(mech_name):
    """
    Attempts to find and read a .txt file matching the mech name.
    """
    # Sanitize input to match file naming conventions
    filename = f"{mech_name.strip()}.txt"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    else:
        return None


# --- Streamlit UI Configuration ---
st.set_page_config(page_title="Mech Critical Table Lookup")

st.title("🛡️ Mech Critical Table Lookup")
st.markdown("Enter the name of a Mech to retrieve its custom Alpha Strike critical hits table.")

# User Input
mech_input = st.text_input("Mech Name", placeholder="Type name here...")

if mech_input:
    content = load_mech_data(mech_input)

    if content:
        st.success(f"Found entry for: {mech_input}")

        # Display the content in a code block or clean text area
        st.subheader("Critical Table Data")
        st.code(content, language="text")

        # Optional: Parse the data into a table if it follows a strict format
        lines = content.split('\n')
        table_data = []
        for line in lines:
            if '\t' in line:
                table_data.append(line.split('\t'))

        if table_data:
            st.table(table_data)

    else:
        st.error(f"No file found for '{mech_input}'. Please ensure '{mech_input}.txt' exists in the repository.")

# Footer
st.sidebar.info("Upload your .txt files to the same GitHub folder as this script.")
