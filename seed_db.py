import pandas as pd
from db import Base, SessionLocal, DailyInsight, engine


def seed_db():

    # Drop all tables
    Base.metadata.drop_all(bind=engine)

    # Recreate all tables
    Base.metadata.create_all(bind=engine)
    df = pd.read_csv(
       "university_mental_health_iot_dataset.csv",
       parse_dates=["timestamp"]
     )

    # Prepare daily averages
    df["date"] = df["timestamp"].dt.date
    daily_avg = df.groupby("date")["stress_level"].mean().reset_index()

    def generate_note(score):
        # 39 was the average stress_level with a std of 13
        if score >= 52:
            return "High stress day"
        elif score <= 26:
            return "Low stress day"
        return "Moderate stress"

    daily_avg["notes"] = daily_avg["stress_level"].apply(generate_note)

    # Insert into database
    db = SessionLocal()
    for _, row in daily_avg.iterrows():

        insight = DailyInsight(
            date=row["date"],
            avg_stress=row["stress_level"],
            notes=row["notes"]
        )
        db.merge(insight)  # merge prevents duplicates
    db.commit()
    db.close()

    print("Database seeded with daily insights.")
