import plotly.express as px
import pandas as pd

def generate_graphs(df, df_under_60):
    figs = {}
    if df is None:
        return figs

    # عملنا متغير واحد فيه كل تعديلات الـ UI عشان مانكررش الكود ونتفادى الأخطاء
    transparent_layout = dict(
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=40, b=20, l=20, r=20),
        font_family="Segoe UI"
    )

    # 1. User Type Pie Chart
    user_counts = df['user_type'].value_counts().reset_index()
    user_counts.columns = ['user_type', 'count']
    figs['user_type'] = px.pie(user_counts, names='user_type', values='count', hole=0.4, title='Proportion of User Types', color_discrete_sequence=px.colors.qualitative.Set2)
    figs['user_type'].update_layout(**transparent_layout)

    # 2. Gender Histogram
    figs['gender'] = px.histogram(df, x='member_gender', title='Distribution of Member Gender', color='member_gender', color_discrete_sequence=px.colors.qualitative.Pastel)
    figs['gender'].update_layout(**transparent_layout)

    # 3. Top 10 Start Stations
    top_start = df['start_station_name'].value_counts().nlargest(10).reset_index()
    top_start.columns = ['station', 'count']
    figs['top_start'] = px.bar(top_start, x='count', y='station', orientation='h', title='Top 10 Start Stations', color='count', color_continuous_scale='Blues')
    # هنا ضفنا ترتيب المحطات مع الخلفية الشفافة في سطر واحد
    figs['top_start'].update_layout(yaxis={'categoryorder':'total ascending'}, **transparent_layout)

    # 4. Boxplot Duration by User Type
    figs['box'] = px.box(df_under_60, x='user_type', y='duration_min', color='user_type', title='Trip Duration by User Type')
    figs['box'].update_layout(**transparent_layout)

    return figs