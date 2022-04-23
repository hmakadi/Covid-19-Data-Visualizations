# Group 1

import pandas as pd
import streamlit as st
import plotly.express as px

df1 = pd.read_csv("https://covid19.who.int/WHO-COVID-19-global-table-data.csv",
                  names=['Name', 'WHO Region', 'Cases - cumulative total',
                         'Cases - cumulative total per 100000 population', 'Cases - newly reported in last 7 days',
                         'Cases - newly reported in last 7 days per 100000 population',
                         'Cases - newly reported in last 24 hours', 'Deaths - cumulative total',
                         'Deaths - cumulative total per 100000 population', 'Deaths - newly reported in last 7 days',
                         'Deaths - newly reported in last 7 days per 100000 population',
                         'Deaths - newly reported in last 24 hours'], header=None)
df1 = df1.iloc[2:, :]

df2 = pd.read_csv("https://covid19.who.int/who-data/vaccination-data.csv")

st.title('Covid-19 Data Visualizations')

if st.sidebar.checkbox('Show dataframe of latest reported counts of cases and deaths'):
    st.write(df1)

if st.sidebar.checkbox('Show dataframe of vaccination data'):
    st.write(df2)

page_names = ['Comparison dashboard', 'Vaccinations dashboard', 'Cases dashboard', 'Deaths dashboard']
page = st.sidebar.radio('Select the page to view', page_names)

if page == 'Comparison dashboard':

    comparison_pages = ['View the bar chart']
    comparison = st.radio('Select an option', comparison_pages)

    if comparison == 'View the bar chart':
        country_select = st.selectbox('Select a country', df1['Name'].unique())
        selected_country = df1[df1['Name'] == country_select]
        st.markdown("## State level analysis")


        def cases_and_deaths_dataframe(df1):
            cases_and_deaths_dataframe = pd.DataFrame({
                'Status': ['Number of Cases', 'Number of deaths'],
                'Number of cases and deaths': (df1.iloc[0]['Cases - cumulative total'],
                                               df1.iloc[0]['Deaths - cumulative total'])})
            return cases_and_deaths_dataframe


        state_total = cases_and_deaths_dataframe(selected_country)
        state_total_graph = px.bar(state_total, x='Status', y='Number of cases and deaths',
                                   labels={'Number of cases and deaths': 'Cases and deaths status in %s' % (
                                       country_select)}, color='Status')
        st.plotly_chart(state_total_graph)

elif page == 'Vaccinations dashboard':

    country_select = st.selectbox('Select a country', df2['COUNTRY'].unique())
    selected_country = df2[df2['COUNTRY'] == country_select]
    st.markdown("## State level analysis")


    def persons_vaccinated_dataframe(df2):
        vaccination_dataframe = pd.DataFrame({
            'Vaccination Status': ['Number of persons vaccinated with atleast one dose',
                                   'Number of persons fully vaccinated'],
            'Number of persons vaccinated': (df2.iloc[0]['PERSONS_FULLY_VACCINATED'],
                                             df2.iloc[0]['PERSONS_VACCINATED_1PLUS_DOSE'])})
        return vaccination_dataframe


    state_total = persons_vaccinated_dataframe(selected_country)
    state_total_graph = px.bar(state_total, x='Vaccination Status', y='Number of persons vaccinated',
                               labels={'Number of persons vaccinated': 'Number of persons vaccinated in %s' % (
                                   country_select)}, color='Vaccination Status')
    st.plotly_chart(state_total_graph)

elif page == 'Cases dashboard':

    comparison_pages = ['View the bar chart', 'View the sun burst chart']
    comparison = st.radio('Select an option', comparison_pages)

    if comparison == 'View the sun burst chart':
        fig = px.sunburst(df1, path=['WHO Region', 'Name'], values='Cases - cumulative total')
        fig.show()

elif page == 'Deaths dashboard':

    comparison_pages = ['View the bar chart', 'View the sun burst chart']
    comparison = st.radio('Select an option', comparison_pages)

    if comparison == 'View the sun burst chart':
        fig = px.sunburst(df1, path=['WHO Region', 'Name'], values='Deaths - cumulative total')
        fig.show()

