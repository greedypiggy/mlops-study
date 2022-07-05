from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule
from prefect.flow_runners import SubprocessFlowRunner

DeploymentSpec(
    flow_location="score.py",
    name="ride_duration_prediction",
    parameters={
        'taxi_type': "green",
        "run_id": "9099cf72ff2d41ec82f98bb5a9f7d95e",

    },
    flow_storage="3ef10446-8c43-4806-9a20-b368ff81a72e",
    schedule=CronSchedule(cron="0 3 2 * *"),
    flow_runner=SubprocessFlowRunner(),
    tags=["ml"]
)