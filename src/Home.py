"""Home page."""
import streamlit as st
import streamlit.components.v1 as components
import feedparser

def parse_feed(feed):
    """Parse RSS feed."""
    with st.spinner(f"Loading {feed} ..."):
        feed = feedparser.parse(feed)
        for i in range(3):
            st.write(f"{i+1}. [{feed.entries[i].title}]({feed.entries[i].link})")

def main():
    """Home page."""
    st.set_page_config(page_title="Home", page_icon=":coffee:", layout="wide")

    # Sidebar links
    with st.sidebar:
        st.markdown("""
        ## Quick Links

        - [GitHub](https://github.com/)
        - [YouTube](https://www.youtube.com/)""")

        # Clock widget
        components.html("""<div style="text-align:center;padding:1em 0;">
            <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=en&size=small&timezone=Europe%2FBerlin" width="100%" height="90" frameborder="0" seamless></iframe>
            </div>""")

        st.markdown("## Google Search")
        # Google search widget
        components.html("""<script async src="https://cse.google.com/cse.js?cx=03208d414f651405c"></script>
            <div class="gcse-searchbox-only"></div>""")

    # Main page title
    st.markdown("# MyDash")
    st.markdown("---")

    # RSS tickers
    st.markdown("### Python Library RSS:")
    parse_feed("https://www.blog.pythonlibrary.org/feed/")
    st.markdown("### Real Python RSS:")
    parse_feed("https://realpython.com/atom.xml?format=xml")
    st.markdown("### Planet Python RSS:")
    parse_feed("https://planetpython.org/rss20.xml")

if __name__ == "__main__":
    main()
