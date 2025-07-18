
from streamlit_extras.streaming_write import write
import streamlit as st
import pandas as pd
import numpy as np
import time
import mongo_client


def example():
    _LOREM_IPSUM = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

    def stream_example():
        for word in _LOREM_IPSUM.split():
            yield word + " "
            time.sleep(0.1)

        # Also supports any other object supported by `st.write`
        yield pd.DataFrame(
            np.random.randn(5, 10),
            columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        )

        for word in _LOREM_IPSUM.split():
            yield word + " "
            time.sleep(0.05)

    if st.button("Stream data"):
        write(stream_example)

example()