# importing libraries
import streamlit as st
import pandas as pd
import helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.figure_factory as ff

# st.title("Business Care Dashboard")
st.markdown("<h1 style='text-align: center;'>Business Care Dashboard</h1>", unsafe_allow_html=True)

st.sidebar.title("Business Care")

df = pd.read_excel('scripts/preprocessed_data.xlsx')

month = df['EMonth'].unique().tolist()
# month.sort()
month.insert(0, 'Overall')
year = df['EYear'].unique().tolist()
year.sort()
year.insert(0, 'Overall')

def segment_list(df):
    segment_list = df['Segment'].unique().tolist()
    segment_list.sort()
    segment_list.insert(0, 'Overall')
    
    return segment_list

def site_list(df):
    site_list = df['SITE'].unique().tolist()
    site_list.sort()
    site_list.insert(0, 'Overall')
    
    return site_list
def group_list(df):
    group_list = df['Group_Name'].unique().tolist()
    group_list.sort()
    group_list.insert(0, 'Overall')
    
    return group_list

# st.sidebar.image("https://logowik.com/content/uploads/images/etisalat-new-20229928.logowik.com.webp")
user_menu = st.sidebar.selectbox(
    'Select Analyze Option',
    ('Overall','Segment-Wise Analysis','Group-wise Analysis')
)


if user_menu == 'Overall':
    # month, year = month_year_list(df)
    st.markdown("<h3 style='text-align: center;'>Overall Analyze</h3>", unsafe_allow_html=True)
    # st.subheader("Overall Analyze")
    selected_year = st.sidebar.selectbox("Select Year",year)
    # Select Month
    disabled = selected_year == "Overall"
    selected_month = st.sidebar.selectbox("Select Month",month,disabled=disabled)
    st.markdown(
                    """
                    <div style="text-align: center; color: yellow; font-size: 16px;">
                        Note: If you want to see Specific Year Analyzation, select a year first and Month respectively. 
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    # Select Site
    selected_site = st.sidebar.selectbox("Select Site",site_list(df))
    
    # selected_month == 'Overall' and
    if selected_year == 'Overall' and selected_site == 'Overall':
        # st.dataframe(df)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Total Complaints: ",df.shape[0])
        with col2:
            st.write("Total Agents: ",df['Agent_Name'].nunique())
        with col3:
            st.write("Total Sites: ",df['SITE'].nunique())

        col23, col24, col25 = st.columns(3)
        with col23:
            st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
        with col24:
            st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
        with col25:
            st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
        
        col4, col5, col6 = st.columns(3)
        with col4:
            st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
        with col5:
            st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
        with col6:
            st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

        # Plotting bar chart of Over all Status
        df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
        fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status', title='Overall Action Taken by Date', labels={'EDate': 'Date', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plotting bar chart of Over all Action Status Count
        df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
        fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
             labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plotting bar chart of Over all Segment wise count
        df_Se_grouped = df.groupby(['Segment']).size().reset_index(name='Count')
        fig = px.bar(df_Se_grouped, x='Segment', y='Count', color='Segment', title='Segment Wise Counts',
             labels={'Segment': 'Segment', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Segment Wise Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plotting bar chart of Over all Product wise count
        df_suseg_grouped = df.groupby(['Sub_Segment']).size().reset_index(name='Count')
        fig = px.bar(df_suseg_grouped, x='Sub_Segment', y='Count', color='Sub_Segment', title='Sub_Segment Wise Counts',
             labels={'Sub_Segment': 'Sub_Segment', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Sub_Segment Wise Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plotting bar chart of Over all Site wise count
        df_Site_grouped = df.groupby(['SITE']).size().reset_index(name='Count')
        fig = px.bar(df_Site_grouped, x='SITE', y='Count', color='SITE', title='Site Wise Counts',
             labels={'SITE': 'Site', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Site Wise Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plot for Cast Score 1
        df['ACPT_Category'] = df['ACPT_Category'].str.lower()
        df_CS_grouped_c = df[df['Csat_Score'] == 1]
        df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
        fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count',  title='Count of ACPT Category for Csat_Score == 1',
             labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Customer Satisfaction Score = 1", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plot for Cast Score 2
        df_CS_grouped_c = df[df['Csat_Score'] == 2]
        df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
        fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count', title='Count of ACPT Category for Csat_Score == 2',
             labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Customer Satisfaction Score = 2", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plot for Cast Score 3
        df_CS_grouped_c = df[df['Csat_Score'] == -100]
        df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
        fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count', title='Count of ACPT Category for Csat_Score == -100',
             labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Customer Satisfaction Score = -100", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)
    if selected_year != 'Overall' and selected_site == 'Overall':
        if selected_month == 'Overall':
            df = df[df['EYear'] == selected_year]

            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='Action_Status', y='Count',  color='Action_Status',
                 title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Overall Action Taken by Year {selected_year}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            df_grouped = df.groupby(['Segment']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='Segment', y='Count',  color='Segment',
                title='Segment Counts',
                labels={'Segment': 'Segment', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Segment Counts by Year {selected_year}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            df_grouped = df.groupby(['SITE']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='SITE', y='Count', color='SITE',
                title='Site Counts',
                labels={'SITE': 'Site', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Site Counts by Year {selected_year}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
        if selected_month != 'Overall':
            df = df[(df['EYear'] == selected_year) & (df['EMonth'] == selected_month)]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='Action_Status', y='Count', color='Action_Status',
                 title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Overall Action Taken by Year {selected_year}, Month {selected_month}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            df_grouped = df.groupby(['Segment']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='Segment', y='Count', color='Segment',
                title='Segment Counts',
                labels={'Segment': 'Segment', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Segment Counts by Year {selected_year}, Month {selected_month}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            df_grouped = df.groupby(['SITE']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='SITE', y='Count', color='SITE',
                title='Site Counts',
                labels={'SITE': 'Site', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Site Counts by Year {selected_year}, Month {selected_month}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
    if selected_year != 'Overall' and selected_site != 'Overall':
        if selected_month == 'Overall':
            df = df[(df['EYear'] == selected_year) & (df['SITE'] == selected_site)]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='Action_Status', y='Count', color='Action_Status',
                 title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Overall Action Taken by Year {selected_year}, Site {selected_site}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            df_grouped = df.groupby(['Segment']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='Segment', y='Count', color='Segment',
                title='Segment Counts',
                labels={'Segment': 'Segment', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Segment Counts by Year {selected_year}, Site {selected_site}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            df_grouped = df.groupby(['SITE']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='SITE', y='Count', color='SITE',
                title='Site Counts',
                labels={'SITE': 'Site', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Site Counts by Year {selected_year}, Site {selected_site}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
        if selected_month != 'Overall':
            df = df[(df['EYear'] == selected_year) & (df['EMonth'] == selected_month) & (df['SITE'] == selected_site)]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='Action_Status', y='Count', color='Action_Status',
                 title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Overall Action Taken by Year {selected_year}, Month {selected_month}, Site {selected_site}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            df_grouped = df.groupby(['Segment']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='Segment', y='Count', color='Segment',
                title='Segment Counts', 
                labels={'Segment': 'Segment', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Segment Counts by Year {selected_year}, Month {selected_month}, Site {selected_site}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            df_grouped = df.groupby(['SITE']).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='SITE', y='Count', color='SITE',
                title='Site Counts',
                labels={'SITE': 'Site', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': f"Site Counts by Year {selected_year}, Month {selected_month}, Site {selected_site}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
    if selected_year == 'Overall' and selected_site != 'Overall':
        df = df[(df['SITE'] == selected_site)]
        
        col1, col2, col3 = st.columns(3)
        with col1:
                st.write("Total Complaints: ",df.shape[0])
        with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
        with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

        col23, col24, col25 = st.columns(3)
        with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
        with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
        with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
        col4, col5, col6 = st.columns(3)
        with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
        with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
        with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

        df_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
        fig = px.bar(df_grouped, x='Action_Status', y='Count', color='Action_Status',
                 title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': f"Overall Action Taken by Site {selected_site}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        df_grouped = df.groupby(['Segment']).size().reset_index(name='Count')
        fig = px.bar(df_grouped, x='Segment', y='Count', color='Segment',
                title='Segment Counts',
                labels={'Segment': 'Segment', 'Count': 'Count of Actions'},
                barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': f"Segment Counts by Site {selected_site}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        df_grouped = df.groupby(['SITE']).size().reset_index(name='Count')
        fig = px.bar(df_grouped, x='SITE', y='Count', color='SITE',
                title='Site Counts',
                labels={'SITE': 'Site', 'Count': 'Count of Actions'},
                barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': f"Site Counts by Site {selected_site}", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

if user_menu == 'Segment-Wise Analysis':
    
    # Sub Header
    st.markdown("<h3 style='text-align: center;'>Segment-Wise Analysis</h3>", unsafe_allow_html=True)
    
    selected_year = st.sidebar.selectbox("Select Year",year)
    disabled = selected_year == "Overall"
    selected_month = st.sidebar.selectbox("Select Month",month,disabled=disabled)
    st.markdown(
                    """
                    <div style="text-align: center; color: yellow; font-size: 16px;">
                        Note: If you want to see Specific Year Analyzation, select a year first and Month respectively. <br>
                        Note: Sub Segment is not available for Overall Segment.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    selected_site = st.sidebar.selectbox("Select Site",site_list(df))

    col1, col2 = st.columns(2)
    with col1:
        selected_segment = st.selectbox("Select Segment",segment_list(df))
    def sub_segment_list(df):
        if selected_segment == 'Overall':
            sub_segment_list = df['Sub_Segment'].unique().tolist()
            sub_segment_list.sort()
            sub_segment_list.insert(0, 'Overall')
        else:
            sub_segment_list = df[df['Segment'] == selected_segment]['Sub_Segment'].unique().tolist()
            sub_segment_list.sort()
            sub_segment_list.insert(0, 'Overall')
    
        return sub_segment_list

    with col2:
        disabled = selected_segment == "Overall"
        selected_sub_segment = st.selectbox("Select Sub_Segment",sub_segment_list(df), disabled=disabled)

    if selected_segment == 'Overall' and selected_year == 'Overall' and selected_site == 'Overall':
        
        col1, col2, col3 = st.columns(3)
        with col1:
                st.write("Total Complaints: ",df.shape[0])
        with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
        with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

        col23, col24, col25 = st.columns(3)
        with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
        with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
        with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
        col4, col5, col6 = st.columns(3)
        with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
        with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
        with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

        df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
        fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                title='Overall Action Taken by Date',
                labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)
        # Plotting bar chart of Over all Action Status Count
        df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
        fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
             labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plotting bar chart of Over all Segment wise count
        df_Se_grouped = df.groupby(['Segment']).size().reset_index(name='Count')
        fig = px.bar(df_Se_grouped, x='Segment', y='Count', color='Segment', title='Segment Wise Counts',
             labels={'Segment': 'Segment', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Segment Wise Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plotting bar chart of Over all Product wise count
        df_suseg_grouped = df.groupby(['Sub_Segment']).size().reset_index(name='Count')
        fig = px.bar(df_suseg_grouped, x='Sub_Segment', y='Count', color='Sub_Segment', title='Sub_Segment Wise Counts',
             labels={'Sub_Segment': 'Sub_Segment', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Sub_Segment Wise Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plotting bar chart of Over all Site wise count
        df_Site_grouped = df.groupby(['SITE']).size().reset_index(name='Count')
        fig = px.bar(df_Site_grouped, x='SITE', y='Count', color='SITE', title='Site Wise Counts',
             labels={'SITE': 'Site', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Site Wise Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plot for Cast Score 1
        df['ACPT_Category'] = df['ACPT_Category'].str.lower()
        df_CS_grouped_c = df[df['Csat_Score'] == 1]
        df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
        fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count',  title='Count of ACPT Category for Csat_Score == 1',
             labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Customer Satisfaction Score = 1", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plot for Cast Score 2
        df_CS_grouped_c = df[df['Csat_Score'] == 2]
        df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
        fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count', title='Count of ACPT Category for Csat_Score == 2',
             labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Customer Satisfaction Score = 2", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

        # Plot for Cast Score 3
        df_CS_grouped_c = df[df['Csat_Score'] == -100]
        df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
        fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count', title='Count of ACPT Category for Csat_Score == -100',
             labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Customer Satisfaction Score = -100", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)
    if selected_segment != 'Overall' and selected_year == 'Overall' and selected_site == 'Overall':
        df = df[df['Segment'] == selected_segment]
        if selected_sub_segment == 'Overall':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
            
            # Plotting bar chart of Over all Action Status Count
            df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            # Plotting bar chart of Over all Site wise count
            df_Site_grouped = df.groupby(['SITE']).size().reset_index(name='Count')
            fig = px.bar(df_Site_grouped, x='SITE', y='Count', color='SITE', title='Site Wise Counts',
                labels={'SITE': 'Site', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Site Wise Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            # Plot for Cast Score 1
            df['ACPT_Category'] = df['ACPT_Category'].str.lower()
            df_CS_grouped_c = df[df['Csat_Score'] == 1]
            df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
            fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count',  title='Count of ACPT Category for Csat_Score == 1',
                labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Customer Satisfaction Score = 1", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            # Plot for Cast Score 2
            df_CS_grouped_c = df[df['Csat_Score'] == 2]
            df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
            fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count', title='Count of ACPT Category for Csat_Score == 2',
                labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Customer Satisfaction Score = 2", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            # Plot for Cast Score 3
            df_CS_grouped_c = df[df['Csat_Score'] == -100]
            df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
            fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count', title='Count of ACPT Category for Csat_Score == -100',
                labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Customer Satisfaction Score = -100", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
        if selected_sub_segment != 'Overall':
            df = df[df['Sub_Segment'] == selected_sub_segment]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
            
            # Plotting bar chart of Over all Action Status Count
            df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            # Plotting bar chart of Over all Site wise count
            df_Site_grouped = df.groupby(['SITE']).size().reset_index(name='Count')
            fig = px.bar(df_Site_grouped, x='SITE', y='Count', color='SITE', title='Site Wise Counts',
                labels={'SITE': 'Site', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Site Wise Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            # Plot for Cast Score 1
            df['ACPT_Category'] = df['ACPT_Category'].str.lower()
            df_CS_grouped_c = df[df['Csat_Score'] == 1]
            df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
            fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count',  title='Count of ACPT Category for Csat_Score == 1',
                labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Customer Satisfaction Score = 1", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            # Plot for Cast Score 2
            df_CS_grouped_c = df[df['Csat_Score'] == 2]
            df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
            fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count', title='Count of ACPT Category for Csat_Score == 2',
                labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Customer Satisfaction Score = 2", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

            # Plot for Cast Score 3
            df_CS_grouped_c = df[df['Csat_Score'] == -100]
            df_CS_grouped_cast = df_CS_grouped_c.groupby('ACPT_Category').size().reset_index(name='Count')
            fig = px.bar(df_CS_grouped_cast, x='ACPT_Category', y='Count', color='Count', title='Count of ACPT Category for Csat_Score == -100',
                labels={'Count': 'ACPT Category Count', 'ACPT_Category': 'ACPT Category'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Customer Satisfaction Score = -100", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
    if selected_segment != 'Overall' and selected_year != 'Overall' and selected_site == 'Overall':
        df = df[(df['Segment'] == selected_segment) & (df['EYear'] == selected_year)]
        if selected_sub_segment == 'Overall' and selected_month == 'Overall':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
        if selected_sub_segment != 'Overall' and selected_month == 'Overall':
            df = df[(df['Segment'] == selected_segment) & (df['EYear'] == selected_year) & (df['Sub_Segment'] == selected_sub_segment)]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
        if selected_sub_segment == 'Overall' and selected_month != 'Overall':
            df = df[(df['Segment'] == selected_segment) & (df['EYear'] == selected_year) & (df['EMonth'] == selected_month)]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
        if selected_sub_segment != 'Overall' and selected_month != 'Overall':
            df = df[(df['Segment'] == selected_segment) & (df['EYear'] == selected_year) & (df['Sub_Segment'] == selected_sub_segment) & (df['EMonth'] == selected_month)]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
    if selected_segment != 'Overall' and selected_year != 'Overall' and selected_site != 'Overall':
        # df = df[(df['Segment'] == selected_segment) & (df['EMonth'] == selected_month) & (df['EYear'] == selected_year) & (df['SITE'] == selected_site)]
        df = df[(df['Segment'] == selected_segment) & (df['EYear'] == selected_year) & (df['SITE'] == selected_site)]
        if selected_sub_segment == 'Overall' and selected_month == 'Overall':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())
        if selected_sub_segment != 'Overall' and selected_month == 'Overall':
            df = df[(df['Segment'] == selected_segment) & (df['EYear'] == selected_year) & (df['Sub_Segment'] == selected_sub_segment) & (df['SITE'] == selected_site)]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())
        if selected_sub_segment == 'Overall' and selected_month != 'Overall':
            df = df[(df['Segment'] == selected_segment) & (df['EYear'] == selected_year) & (df['EMonth'] == selected_month) & (df['SITE'] == selected_site)]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())
        if selected_sub_segment != 'Overall' and selected_month != 'Overall':
            df = df[(df['Segment'] == selected_segment) & (df['EYear'] == selected_year) & (df['EMonth'] == selected_month) & (df['Sub_Segment'] == selected_sub_segment) & (df['SITE'] == selected_site)]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Total Complaints: ",df.shape[0])
            with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

if user_menu == 'Group-wise Analysis':
    # Sub Header
    st.markdown("<h3 style='text-align: center;'>Group-Wise Analysis</h3>", unsafe_allow_html=True)
    selected_year = st.sidebar.selectbox("Select Year",year)
    disabled = selected_year == "Overall"
    selected_month = st.sidebar.selectbox("Select Month",month, disabled=disabled)
    selected_site = st.sidebar.selectbox("Select Site",site_list(df))
    st.markdown(
                    """
                    <div style="text-align: center; color: yellow; font-size: 16px;">
                        Note: If you want to see Specific Year Analyzation, select a year first and Month respectively.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    selected_group = st.selectbox("Select Group",group_list(df))

    if selected_group == 'Overall' and selected_year == 'Overall' and selected_site == 'Overall':
        
        col1, col2, col3 = st.columns(3)
        with col1:
                st.write("Total Complaints: ",df.shape[0])
        with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
        with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

        col23, col24, col25 = st.columns(3)
        with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
        with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
        with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
        col4, col5, col6 = st.columns(3)
        with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
        with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
        with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

        df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
        fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                title='Overall Action Taken by Date',
                labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)
        
        # Plotting bar chart of Over all Action Status Count
        df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
        fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
             labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

    if selected_group != 'Overall' and selected_year == 'Overall' and selected_site == 'Overall':
        df = df[(df['Group_Name'] == selected_group)]
        col1, col2, col3 = st.columns(3)
        with col1:
                st.write("Total Complaints: ",df.shape[0])
        with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
        with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

        col23, col24, col25 = st.columns(3)
        with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
        with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
        with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
        col4, col5, col6 = st.columns(3)
        with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
        with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
        with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

        df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
        fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                title='Overall Action Taken by Date',
                labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)
        
        # Plotting bar chart of Over all Action Status Count
        df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
        fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
             labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
             barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)    

    if selected_group != 'Overall' and selected_year != 'Overall' and selected_site == 'Overall':
        
        if selected_month == 'Overall':
            df = df[(df['Group_Name'] == selected_group) & (df['EYear'] == selected_year)]
            col1, col2, col3 = st.columns(3)
            with col1:
                    st.write("Total Complaints: ",df.shape[0])
            with col2:
                    st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                    st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                    st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                    st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                    st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
                
            col4, col5, col6 = st.columns(3)
            with col4:
                    st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                    st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                    st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())
            
            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
            
            # Plotting bar chart of Over all Action Status Count
            df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

        if selected_month != 'Overall':
            df = df[(df['Group_Name'] == selected_group) & (df['EYear'] == selected_year) & (df['EMonth'] == selected_month)]
            col1, col2, col3 = st.columns(3)
            with col1:
                    st.write("Total Complaints: ",df.shape[0])
            with col2:
                    st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                    st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                    st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                    st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                    st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
                
            col4, col5, col6 = st.columns(3)
            with col4:
                    st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                    st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                    st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
            
            # Plotting bar chart of Over all Action Status Count
            df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

    if selected_group == 'Overall' and selected_year != 'Overall' and selected_site == 'Overall':
        df = df[(df['EYear'] == selected_year)]
        if selected_month == 'Overall':
            col1, col2, col3 = st.columns(3)
            with col1:
                    st.write("Total Complaints: ",df.shape[0])
            with col2:
                    st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                    st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                    st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                    st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                    st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
                
            col4, col5, col6 = st.columns(3)
            with col4:
                    st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                    st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                    st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())

            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
            
            # Plotting bar chart of Over all Action Status Count
            df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

        if selected_month != 'Overall':
            df = df[(df['EYear'] == selected_year) & (df['EMonth'] == selected_month)]
            col1, col2, col3 = st.columns(3)
            with col1:
                    st.write("Total Complaints: ",df.shape[0])
            with col2:
                    st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                    st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                    st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                    st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                    st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
                
            col4, col5, col6 = st.columns(3)
            with col4:    
                    st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                    st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                    st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())
            
            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
            
            # Plotting bar chart of Over all Action Status Count
            df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

    if selected_group == 'Overall' and selected_year == 'Overall' and selected_site != 'Overall':
        df = df[(df['SITE'] == selected_site)]
        col1, col2, col3 = st.columns(3)
        with col1:
                st.write("Total Complaints: ",df.shape[0])
        with col2:
                st.write("Total Agents: ",df['Agent_Name'].nunique())
        with col3:
                st.write("Total Sites: ",df['SITE'].nunique())

        col23, col24, col25 = st.columns(3)
        with col23:
                st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
        with col24:
                st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
        with col25:
                st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
            
        col4, col5, col6 = st.columns(3)
        with col4:
                st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
        with col5:
                st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
        with col6:
                st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())
        df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
        fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)
            
        # Plotting bar chart of Over all Action Status Count
        df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
        fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
        # Update layout of the plot
        fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
        # Show plot in Streamlit
        st.plotly_chart(fig)

    if selected_group != 'Overall' and selected_year != 'Overall' and selected_site != 'Overall':
        df = df[(df['Group_Name'] == selected_group) & (df['EYear'] == selected_year) & (df['SITE'] == selected_site)]
        if selected_month == 'Overall':
            col1, col2, col3 = st.columns(3)
            with col1:
                    st.write("Total Complaints: ",df.shape[0])
            with col2:
                    st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                    st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                    st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                    st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                    st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
                
            col4, col5, col6 = st.columns(3)
            with col4:
                    st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                    st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                    st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())
            
            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
            
            # Plotting bar chart of Over all Action Status Count
            df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)

        if selected_month != 'Overall':
            df = df[(df['Group_Name'] == selected_group) & (df['EMonth'] == selected_month) & (df['EYear'] == selected_year) & (df['SITE'] == selected_site)]
            col1, col2, col3 = st.columns(3)
            with col1:
                    st.write("Total Complaints: ",df.shape[0])
            with col2:
                    st.write("Total Agents: ",df['Agent_Name'].nunique())
            with col3:
                    st.write("Total Sites: ",df['SITE'].nunique())

            col23, col24, col25 = st.columns(3)
            with col23:
                    st.write("Ajman Agents: ",df[df['SITE']=='Ajman']['Agent_Name'].nunique())
            with col24:
                    st.write("CNX Agents: ",df[df['SITE']=='CNX']['Agent_Name'].nunique())
            with col25:
                    st.write("EGS Agents: ",df[df['SITE']=='EGS']['Agent_Name'].nunique())
                
            col4, col5, col6 = st.columns(3)
            with col4:
                    st.write("Csat Score 1: ",df[df['Csat_Score'] == 1]['Csat_Score'].count())
            with col5:
                    st.write("Csat Score 2: ",df[df['Csat_Score'] == 2]['Csat_Score'].count())
            with col6:
                    st.write("Csat Score -100: ",df[df['Csat_Score'] == -100]['Csat_Score'].count())
            df_grouped = df.groupby(['Action_Status', df['EDate'].dt.date]).size().reset_index(name='Count')
            fig = px.bar(df_grouped, x='EDate', y='Count', color='Action_Status',
                    title='Overall Action Taken by Date',
                    labels={'EDate': 'Date', 'Count': 'Count of Actions'},
                    barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Overall Action Taken", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)
            
            # Plotting bar chart of Over all Action Status Count
            df_AC_grouped = df.groupby(['Action_Status']).size().reset_index(name='Count')
            fig = px.bar(df_AC_grouped, x='Action_Status', y='Count', color='Action_Status', title='Action Status Counts',
                labels={'Action_Status': 'Action Status', 'Count': 'Count of Actions'},
                barmode='group')
            # Update layout of the plot
            fig.update_layout( title={'text': "Action Status Counts", 'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
            # Show plot in Streamlit
            st.plotly_chart(fig)



            

