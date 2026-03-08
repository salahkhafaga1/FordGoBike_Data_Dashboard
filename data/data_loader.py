import pandas as pd

def load_data(filepath=r"D:\AI\ai_deploma_master\ai_deploma_master\Data_Analysis\Final_Project\FordGoBike_Project-main\data\fordgobike-tripdataFor201902_cleaned.csv"):
    try:
        df = pd.read_csv(filepath)
        # Filter trips under 60 minutes for cleaner visualizations
        df_under_60 = df[df['duration_min'] <= 60]
        return df, df_under_60
    except FileNotFoundError:
        print(f"⚠️ Error: Data file not found at {filepath}")
        return None, None
