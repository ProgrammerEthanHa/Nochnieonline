import streamlit as st
import pandas as pd
import altair as alt

st.header("Noch nie online 2022")
st.subheader("Anteil der 16 bis 74 Jährigen in %, ausgewählte EU-Staaaten")

source = pd.DataFrame({
        'Anteil (%)': [14, 14, 10, 9, 6, 6, 3, 2, 1],
        'Land': ['Griechenland', 'Portugal', 'Italien', 'Polen', 'Frankreich', 'Deutschland', 'Niederlande', 'Finnland', 'Schweden']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Land:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    2023
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Eurostat")