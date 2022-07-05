import score
from prefect import flow
from datetime import datetime

from dateutil.relativedelta import relativedelta

@flow
def ride_duration_prediction_backfill():
    start_date = datetime(year=2021, month=3, day=1)
    end_date = datetime(year=2022, month=4, day=1)

    d = start_date

    while d <= end_date:
        score.ride_duration_prediction(
            taxi_type='green',
            run_id='9099cf72ff2d41ec82f98bb5a9f7d95e',
            run_date=d
        )

        d = d + relativedelta(months=1)

if __name__ == '__main__':
    ride_duration_prediction_backfill()