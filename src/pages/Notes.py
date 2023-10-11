"""Notes page."""
import os
import streamlit as st

def str_to_page_name(text: str) -> str:
    """Converts a string to a page name."""
    return text.replace("_", " ").title()

def main():
    """Notes page."""
    data_dir = "data"
    if os.path.exists(data_dir):
        pages = []
        if "index.md" in os.listdir(data_dir):
            pages.append("index.md")
        for filename in os.listdir(data_dir):
            if not filename.startswith(".") and filename != "index.md":
                pages.append(filename)
        if not pages:
            st.warning("No pages found in the Data folder.")
        else:
            st.set_page_config(page_title="Notes", page_icon=":coffee:", layout="wide")
            selected_page = st.sidebar.selectbox("Select a file", pages)
            filepath = os.path.join(
                data_dir,
                selected_page,
            )
            with open(filepath, "r", encoding="utf-8") as open_file:
                content = open_file.read()
            if filepath.endswith(".md"):
                st.markdown(content, unsafe_allow_html=True)
            else:
                st.text(content)

    else:
        st.error(f"Data folder not found! (looking for {data_dir})")


if __name__ == "__main__":
    main()
