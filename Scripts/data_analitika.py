import pandas as pd
import plotly.express as px

def plot_top10(df, sort_by='view_count', title='Top 10 Kaggle datasets'):
    df_copy = df.copy()

    # Sanani datetime formatiga o'tkazish
    if sort_by == 'last_updated':
        df_copy['last_updated'] = pd.to_datetime(df_copy['last_updated'], errors='coerce')

    # Raqamli ustunlarni tozalash
    if sort_by != 'last_updated':
        def clean_count(x):
            if pd.isna(x): return 0
            s = str(x).replace(',', '').strip().upper()
            if s.endswith('K'): return float(s[:-1])*1000
            if s.endswith('M'): return float(s[:-1])*1000000
            try: return float(s)
            except: return 0
        df_copy[sort_by] = df_copy[sort_by].apply(clean_count)

    # Top10 olish
    top10 = df_copy.sort_values(sort_by, ascending=False).head(10).copy()

    # X o‘qini noyob qilish: index ishlatamiz
    top10['x_val'] = top10.index  # har bar uchun noyob

    # Plotly chart
    fig = px.bar(
        top10,
        x='x_val',
        y=sort_by,
        text=sort_by
    )

    # Hover orqali title ko‘rsatish
    fig.update_traces(
        customdata=top10['title'],
        hovertemplate='<b>%{customdata}</b><br>%{y}',
        texttemplate='%{text:,.0f}',
        textposition='outside'
    )

    # Chiroyli ko‘rinish
    fig.update_layout(
        xaxis_tickvals=[],  # x o‘qdagi raqamlarni yashiramiz
        yaxis=dict(tickformat=','),
        margin=dict(t=80, b=150)
    )

    try:
        fig.show()
    except:
        out_file = f"top10_{sort_by}.html"
        fig.write_html(out_file, include_plotlyjs='cdn')
        print(f"✅ Grafik saqlandi: {out_file}")

    return top10
