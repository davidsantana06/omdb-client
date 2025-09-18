from pandas import DataFrame
import streamlit as st

from .enums import ContentType
from .secrets import AUTHOR_NAME, AUTHOR_URL, IMDB_TITLE_URL, OMDB_API_KEY, OMDB_API_URL
from .services import MAX_MEDIA_PER_GET, get_media
from .types import ContentType, Media


_STYLE = """
    <style>
        a {
            color: #A78BFA !important;
            font-weight: 600;
            text-decoration: none !important;
        }
        a:hover { font-weight: 700; }

        div.stSpinner > div {
            text-align:center;
            align-items: center;
            justify-content: center;
        }

        hr { visibility: hidden !important; }

        table { width: 100%; }
        tr:first-child { border: none!important ; }
        th, td { border: none !important; }
        /* Poster */
        th:nth-child(1), td:nth-child(1) { width: 15%; text-align: center; }
        /* Title */
        th:nth-child(2), td:nth-child(2) { width: 40%; }
        /* Year */
        th:nth-child(3), td:nth-child(3) { width: 15%; text-align: center; }
        /* Type */
        th:nth-child(4), td:nth-child(4) { width: 15%; text-align: center; }
        /* IMDb */
        th:nth-child(5), td:nth-child(5) { width: 15%; text-align: center; }

        .warning {
            background-color: #FEF3C7;
            color: #CA8A04;
            border-radius: 0.25rem;
            border: 1px solid #FACC15;
            text-align: center;
            padding: 1rem;
        }
    </style>
"""


def configure_page() -> None:
    st.set_page_config(page_title="OMDb Client", page_icon="🎬", layout="centered")
    st.markdown(_STYLE, unsafe_allow_html=True)


def render_header() -> None:
    st.title("🎬 OMDb Client")
    st.caption("The Open Movie Database Client")
    st.write("Search for movies, series, and episodes using the OMDb API.")


def render_main() -> None:

    def render_table(media: list[Media]) -> None:
        df = DataFrame(media)
        df = df[Media.get_columns()]
        df["Poster"] = df["Poster"].apply(render_poster_td)
        df["Type"] = df["Type"].apply(render_type_td)
        df["imdbID"] = df["imdbID"].apply(render_imdb_td)
        df.rename(columns={"imdbID": "IMDb"}, inplace=True)
        st.write(
            df.to_html(escape=False, index=False, border=0),
            unsafe_allow_html=True,
        )

    def render_poster_td(url: str) -> str:
        if url.startswith("http"):
            return f'<img src="{url}">'
        return "N/A"

    def render_type_td(content_type: str) -> str:
        return content_type.capitalize()

    def render_imdb_td(imdb_id: str) -> str:
        return f'<a href="{IMDB_TITLE_URL}{imdb_id}" target="_blank">🔗 View</a>'

    def render_warning(message: str) -> None:
        st.markdown(
            f"<div class='warning'>☝️🤓 ~ {message}</div>",
            unsafe_allow_html=True,
        )

    content_type_options = list(ContentType)
    limit_options = [MAX_MEDIA_PER_GET * i for i in range(1, 4 + 1)]

    with st.form(key="search_form"):
        title = st.text_input("Title", placeholder="e.g., Blade Runner", max_chars=100)

        left_col, right_col = st.columns(2)
        with left_col:
            content_type = st.selectbox("Type", content_type_options)
        with right_col:
            limit = st.selectbox("Limit", limit_options)

        submitted = st.form_submit_button("🔍 Search", use_container_width=True)

    if not submitted:
        return

    if submitted and not title:
        render_warning("Title is required.")
        return

    with st.spinner("Fetching data..."):
        media = get_media(OMDB_API_URL, OMDB_API_KEY, title, content_type, limit)
        render_table(media) if media != [] else render_warning("No results found.")


def render_footer() -> None:
    st.markdown(
        f"""
        <div style="text-align: center;">
            Made with 💪 by <a href="{AUTHOR_URL}">{AUTHOR_NAME}</a> • 
            Powered by <a href="{OMDB_API_URL}">OMDb API</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_divider() -> None:
    st.divider()
