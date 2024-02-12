"""fix trip id length

Revision ID: 1b53fd278b10
Revises: 5d9a7ee21ae5
Create Date: 2023-11-27 16:25:42.657967

Details
* upgrade -> change "trip_id" field from length 128 to 512
* downgrade -> change "trip_id" field from length 512 to 128
"""

from alembic import op
import sqlalchemy as sa

from lamp_py.migrations.versions.performance_manager_staging.sql_strings.strings_001 import (
    view_opmi_all_rt_fields_joined,
)

# revision identifiers, used by Alembic.
revision = "1b53fd278b10"
down_revision = "5d9a7ee21ae5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP VIEW IF EXISTS opmi_all_rt_fields_joined;")
    op.alter_column(
        "static_route_patterns",
        "representative_trip_id",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=512),
        existing_nullable=False,
    )
    op.alter_column(
        "static_stop_times",
        "trip_id",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=512),
        existing_nullable=False,
    )
    op.alter_column(
        "static_trips",
        "trip_id",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=512),
        existing_nullable=False,
    )
    op.alter_column(
        "temp_event_compare",
        "trip_id",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=512),
        existing_nullable=False,
    )
    op.alter_column(
        "vehicle_trips",
        "trip_id",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=512),
        existing_nullable=False,
    )
    op.alter_column(
        "vehicle_trips",
        "static_trip_id_guess",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=512),
        existing_nullable=True,
    )
    op.execute(view_opmi_all_rt_fields_joined)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP VIEW IF EXISTS opmi_all_rt_fields_joined;")
    op.alter_column(
        "vehicle_trips",
        "static_trip_id_guess",
        existing_type=sa.String(length=512),
        type_=sa.VARCHAR(length=128),
        existing_nullable=True,
    )
    op.alter_column(
        "vehicle_trips",
        "trip_id",
        existing_type=sa.String(length=512),
        type_=sa.VARCHAR(length=128),
        existing_nullable=False,
    )
    op.alter_column(
        "temp_event_compare",
        "trip_id",
        existing_type=sa.String(length=512),
        type_=sa.VARCHAR(length=128),
        existing_nullable=False,
    )
    op.alter_column(
        "static_trips",
        "trip_id",
        existing_type=sa.String(length=512),
        type_=sa.VARCHAR(length=128),
        existing_nullable=False,
    )
    op.alter_column(
        "static_stop_times",
        "trip_id",
        existing_type=sa.String(length=512),
        type_=sa.VARCHAR(length=128),
        existing_nullable=False,
    )
    op.alter_column(
        "static_route_patterns",
        "representative_trip_id",
        existing_type=sa.String(length=512),
        type_=sa.VARCHAR(length=128),
        existing_nullable=False,
    )
    op.execute(view_opmi_all_rt_fields_joined)
    # ### end Alembic commands ###
