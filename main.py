import streamlit as st
view = [300,200,100,500]
show_raw = st.checkbox('show raw data')
if show_raw == True:
    st.write('# raw data')
    view
st.write('# table')
st.table(view)
st.write('# bar graph')
st.bar_chart(view)

topics = [
    {"id":1, "title":"html", "body":"html is ...", 'view':100},
    {"id":1, "title":"css", "body":"css is ...", 'view':200}
]

st.table(topics)

import padnas as pd
topics['view']