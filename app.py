# Group 1

import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
from vega_datasets import data

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

page_names = ['Global overview', 'Cases dashboard', 'Deaths dashboard', 'Vaccinations dashboard']
page = st.sidebar.radio('Select the page to view', page_names)

if page == 'Global overview':

    select_option = ['Cases', 'Deaths', 'Vaccinations']
    option = st.radio('Select an option', select_option)

    if option == 'Cases':

        option = st.selectbox('What would you like to be visualized?',
                              ('Cumulative confirmed cases reported to WHO to date',
                               'New confirmed cases reported in the last 7 days',
                               'New confirmed cases reported in the last 24 hours'))

        if option == 'Cumulative confirmed cases reported to WHO to date':

            country_df = df1.groupby('Name').last().reset_index()
            df_by_country = country_df.sort_values(by='Cases - cumulative total', ascending=True)
            fig = px.choropleth(df_by_country, locations="Name",
                                locationmode='country names',
                                hover_name="Cases - cumulative total",
                                color="Name",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

        elif option == 'New confirmed cases reported in the last 7 days':

            country_df = df1.groupby('Name').last().reset_index()
            df_by_country = country_df.sort_values(by='Cases - newly reported in last 7 days', ascending=True)
            fig = px.choropleth(df_by_country, locations="Name",
                                locationmode='country names',
                                hover_name="Cases - newly reported in last 7 days",
                                color="Name",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

        elif option == 'New confirmed cases reported in the last 24 hours':

            country_df = df1.groupby('Name').last().reset_index()
            df_by_country = country_df.sort_values(by='Cases - newly reported in last 24 hours', ascending=True)
            fig = px.choropleth(df_by_country, locations="Name",
                                locationmode='country names',
                                hover_name="Cases - newly reported in last 24 hours",
                                color="Name",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

    elif option == 'Deaths':

        option = st.selectbox('What would you like to be visualized?',
                              ('Cumulative confirmed deaths reported to WHO to date',
                               'New confirmed deaths reported in the last 7 days',
                               'New confirmed deaths reported in the last 24 hours'))

        if option == 'Cumulative confirmed deaths reported to WHO to date':

            country_df = df1.groupby('Name').last().reset_index()
            df_by_country = country_df.sort_values(by='Deaths - cumulative total', ascending=True)
            fig = px.choropleth(df_by_country, locations="Name",
                                locationmode='country names',
                                hover_name="Deaths - cumulative total",
                                color="Name",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

        elif option == 'New confirmed deaths reported in the last 7 days':

            country_df = df1.groupby('Name').last().reset_index()
            df_by_country = country_df.sort_values(by='Deaths - newly reported in last 7 days', ascending=True)
            fig = px.choropleth(df_by_country, locations="Name",
                                locationmode='country names',
                                hover_name="Deaths - newly reported in last 7 days",
                                color="Name",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

        elif option == 'New confirmed deaths reported in the last 24 hours':

            country_df = df1.groupby('Name').last().reset_index()
            df_by_country = country_df.sort_values(by='Deaths - newly reported in last 24 hours', ascending=True)
            fig = px.choropleth(df_by_country, locations="Name",
                                locationmode='country names',
                                hover_name="Deaths - newly reported in last 24 hours",
                                color="Name",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

    elif option == 'Vaccinations':

        option = st.selectbox('What would you like to be visualized?',
                              ('Cumulative total vaccine doses administered',
                               'Cumulative number of persons vaccinated with at least one dose',
                               'Cumulative number of persons fully vaccinated',
                               'Persons received booster or additional dose'))

        if option == 'Cumulative total vaccine doses administered':

            country_df = df2.groupby('COUNTRY').last().reset_index()
            df_by_country = country_df.sort_values(by='TOTAL_VACCINATIONS', ascending=True)
            fig = px.choropleth(df_by_country, locations="COUNTRY",
                                locationmode='country names',
                                color="TOTAL_VACCINATIONS",
                                hover_name="COUNTRY",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

        elif option == 'Cumulative number of persons vaccinated with at least one dose':

            country_df = df2.groupby('COUNTRY').last().reset_index()
            df_by_country = country_df.sort_values(by='PERSONS_VACCINATED_1PLUS_DOSE', ascending=True)
            fig = px.choropleth(df_by_country, locations="COUNTRY",
                                locationmode='country names',
                                color="PERSONS_VACCINATED_1PLUS_DOSE",
                                hover_name="COUNTRY",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

        elif option == 'Cumulative number of persons fully vaccinated':

            country_df = df2.groupby('COUNTRY').last().reset_index()
            df_by_country = country_df.sort_values(by='PERSONS_FULLY_VACCINATED', ascending=True)
            fig = px.choropleth(df_by_country, locations="COUNTRY",
                                locationmode='country names',
                                color="PERSONS_FULLY_VACCINATED",
                                hover_name="COUNTRY",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

        elif option == 'Persons received booster or additional dose':

            country_df = df2.groupby('COUNTRY').last().reset_index()
            df_by_country = country_df.sort_values(by='PERSONS_BOOSTER_ADD_DOSE', ascending=True)
            fig = px.choropleth(df_by_country, locations="COUNTRY",
                                locationmode='country names',
                                color="PERSONS_BOOSTER_ADD_DOSE",
                                hover_name="COUNTRY",
                                color_continuous_scale=px.colors.sequential.Plasma)
            fig.update_layout(title_text="title", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=400)
            st.plotly_chart(fig, use_container_width=True)

elif page == 'Cases dashboard':

    select_option = ['View the sun burst chart']
    option = st.radio('Select an option', select_option)

    if option == 'View the sun burst chart':

        option = st.selectbox('What would you like to be visualized?',
                              ('Cumulative confirmed cases reported to WHO to date',
                               'Cumulative confirmed cases reported to WHO to date per 100,000 population',
                               'New confirmed cases reported in the last 7 days',
                               'New confirmed cases reported in the last 7 days per 100,000 population',
                               'New confirmed cases reported in the last 24 hours'))

        if option == 'Cumulative confirmed cases reported to WHO to date':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Cases - cumulative total',
                              title="Cumulative confirmed cases reported to WHO to date")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'Cumulative confirmed cases reported to WHO to date per 100,000 population':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Cases - cumulative total per 100000 population',
                              title="Cumulative confirmed cases reported to WHO to date per 100,000 population")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'New confirmed cases reported in the last 7 days':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Cases - newly reported in last 7 days',
                              title="New confirmed cases reported in the last 7 days")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'New confirmed cases reported in the last 7 days per 100,000 population':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Cases - newly reported in last 7 days per 100000 population',
                              title="New confirmed cases reported in the last 7 days per 100,000 population")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'New confirmed cases reported in the last 24 hours':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Cases - newly reported in last 24 hours',
                              title="New confirmed cases reported in the last 24 hours")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

elif page == 'Deaths dashboard':

    select_option = ['View the sun burst chart']
    option = st.radio('Select an option', select_option)

    if option == 'View the sun burst chart':

        option = st.selectbox('What would you like to be visualized?',
                              ('Cumulative confirmed deaths reported to WHO to date',
                               'Cumulative confirmed deaths reported to WHO to date per 100,000 population',
                               'New confirmed deaths reported in the last 7 days',
                               'New confirmed deaths reported in the last 7 days per 100,000 population',
                               'New confirmed deaths reported in the last 24 hours'))

        if option == 'Cumulative confirmed deaths reported to WHO to date':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Deaths - cumulative total',
                              title="Cumulative confirmed deaths reported to WHO to date")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'Cumulative confirmed deaths reported to WHO to date per 100,000 population':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Deaths - cumulative total per 100000 population',
                              title="Cumulative confirmed deaths reported to WHO to date per 100,000 population")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'New confirmed deaths reported in the last 7 days':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Deaths - newly reported in last 7 days',
                              title="New confirmed deaths reported in the last 7 days")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'New confirmed deaths reported in the last 7 days per 100,000 population':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Deaths - newly reported in last 7 days per 100000 population',
                              title="New confirmed deaths reported in the last 7 days per 100,000 population")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'New confirmed deaths reported in the last 24 hours':

            fig = px.sunburst(df1,
                              path=['WHO Region', 'Name'],
                              values='Deaths - newly reported in last 24 hours',
                              title="New confirmed deaths reported in the last 24 hours")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

elif page == 'Vaccinations dashboard':

    select_option = ['View the sun burst chart', 'View the bar chart']
    option = st.radio('Select an option', select_option)

    if option == 'View the sun burst chart':

        option = st.selectbox('What would you like to be visualized?',
                              ('Cumulative total vaccine doses administered',
                               'Cumulative number of persons vaccinated with at least one dose',
                               'Cumulative total vaccine doses administered per 100 population',
                               'Cumulative persons vaccinated with at least one dose per 100 population',
                               'Cumulative number of persons fully vaccinated',
                               'Cumulative number of persons fully vaccinated per 100 population',
                               'Persons received booster or additional dose',
                               'Persons received booster or additional dose per 100 population'))

        if option == 'Cumulative total vaccine doses administered':

            fig = px.sunburst(df2,
                              path=['WHO_REGION', 'COUNTRY'],
                              values='TOTAL_VACCINATIONS',
                              title="Cumulative total vaccine doses administered")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'Cumulative number of persons vaccinated with at least one dose':

            fig = px.sunburst(df2,
                              path=['WHO_REGION', 'COUNTRY'],
                              values='PERSONS_VACCINATED_1PLUS_DOSE',
                              title="Cumulative number of persons vaccinated with at least one dose")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'Cumulative total vaccine doses administered per 100 population':

            fig = px.sunburst(df2,
                              path=['WHO_REGION', 'COUNTRY'],
                              values='TOTAL_VACCINATIONS_PER100',
                              title="Cumulative total vaccine doses administered per 100 population")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'Cumulative persons vaccinated with at least one dose per 100 population':

            fig = px.sunburst(df2,
                              path=['WHO_REGION', 'COUNTRY'],
                              values='PERSONS_VACCINATED_1PLUS_DOSE_PER100',
                              title="Cumulative persons vaccinated with at least one dose per 100 population")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'Cumulative number of persons fully vaccinated':

            fig = px.sunburst(df2,
                              path=['WHO_REGION', 'COUNTRY'],
                              values='PERSONS_FULLY_VACCINATED',
                              title="Cumulative number of persons fully vaccinated")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'Cumulative number of persons fully vaccinated per 100 population':

            fig = px.sunburst(df2,
                              path=['WHO_REGION', 'COUNTRY'],
                              values='PERSONS_FULLY_VACCINATED_PER100',
                              title="Cumulative number of persons fully vaccinated per 100 population")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'Persons received booster or additional dose':

            fig = px.sunburst(df2,
                              path=['WHO_REGION', 'COUNTRY'],
                              values='PERSONS_BOOSTER_ADD_DOSE',
                              title="Persons received booster or additional dose")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        elif option == 'Persons received booster or additional dose per 100 population':

            fig = px.sunburst(df2,
                              path=['WHO_REGION', 'COUNTRY'],
                              values='PERSONS_BOOSTER_ADD_DOSE_PER100',
                              title="Persons received booster or additional dose per 100 population")
            fig.update_layout(height=800)
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

    elif option == 'View the bar chart':

        country_select = st.selectbox('Select a country', df2['COUNTRY'].unique())
        selected_country = df2[df2['COUNTRY'] == country_select]
        st.markdown("## State level analysis")


        def persons_vaccinated_dataframe(df2):
            vaccination_dataframe = pd.DataFrame({
                'Vaccination Status': ['Number of persons vaccinated with atleast one dose',
                                       'Number of persons fully vaccinated',
                                       'Persons received booster or additional dose'],
                'Number of persons vaccinated': (df2.iloc[0]['PERSONS_VACCINATED_1PLUS_DOSE'],
                                                 df2.iloc[0]['PERSONS_FULLY_VACCINATED'],
                                                 df2.iloc[0]['PERSONS_BOOSTER_ADD_DOSE'])})
            return vaccination_dataframe


        state_total = persons_vaccinated_dataframe(selected_country)
        state_total_graph = px.bar(state_total, x='Vaccination Status', y='Number of persons vaccinated',
                                   labels={'Number of persons vaccinated': 'Number of persons vaccinated in %s' % (
                                       country_select)},
                                   color='Vaccination Status')
        st.plotly_chart(state_total_graph)