import streamlit as st
import plotly.express as px

df = px.data.gapminder()
st.title("Gapminder Dataset Animated Visualization")
st.write('Loading In progress.......... Please wait!')
st.write(df)

st.subheader('Population change per Continent Colored by life expectancy')
fig = px.bar(df,
             x ="continent",
             y ="pop",
             color ='lifeExp',
             animation_frame ='year',
             hover_name ='country',
             range_y =[0, 4000000000])
fig.show()
st.plotly_chart(fig)

st.subheader('GDP % chaange over time Colored by life expectancy ')
fig2 = px.treemap(df, path=[px.Constant('world'), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'])
fig2.show()
st.plotly_chart(fig2)

st.subheader('Countries per Continent - Colored by life expectancy and Sized by Population')
fig3 = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
fig3.show()
st.plotly_chart(fig3)

st.markdown('Made by **Mohamad bouzi** :sunglasses:')