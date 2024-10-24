"""initial prod schema

Revision ID: 5d9a7ee21ae5
Revises: 
Create Date: 2023-07-25 13:52:06.082838

"""

from alembic import op
import sqlalchemy as sa

from lamp_py.migrations.versions.performance_manager_prod.sql_strings.strings_001 import (
    func_insert_feed_info,
    func_red_is_ashmont_branch,
    func_red_is_braintree_branch,
    func_rt_red_is_ashmont_branch,
    func_rt_red_is_braintree_branch,
    func_rt_trips_branch_trunk,
    func_static_trips_branch_trunk,
    view_opmi_all_rt_fields_joined,
    view_service_id_by_date_and_route,
    view_static_service_id_lookup,
)


# revision identifiers, used by Alembic.
revision = "5d9a7ee21ae5"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "metadata_log",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("processed", sa.Boolean(), nullable=True),
        sa.Column("process_fail", sa.Boolean(), nullable=True),
        sa.Column("path", sa.String(length=256), nullable=False),
        sa.Column(
            "created_on",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("pk_id"),
        sa.UniqueConstraint("path"),
    )
    op.create_index(
        "ix_metadata_log_not_processed",
        "metadata_log",
        ["path"],
        unique=False,
        postgresql_where=sa.text("processed = false"),
    )

    op.create_table(
        "static_calendar",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("service_id", sa.String(length=128), nullable=False),
        sa.Column("monday", sa.Boolean(), nullable=True),
        sa.Column("tuesday", sa.Boolean(), nullable=True),
        sa.Column("wednesday", sa.Boolean(), nullable=True),
        sa.Column("thursday", sa.Boolean(), nullable=True),
        sa.Column("friday", sa.Boolean(), nullable=True),
        sa.Column("saturday", sa.Boolean(), nullable=True),
        sa.Column("sunday", sa.Boolean(), nullable=True),
        sa.Column("start_date", sa.Integer(), nullable=False),
        sa.Column("end_date", sa.Integer(), nullable=False),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("pk_id"),
    )
    op.create_index(
        "ix_static_calendar_composite_1",
        "static_calendar",
        ["static_version_key", "service_id", "start_date", "end_date"],
        unique=False,
    )

    op.create_table(
        "static_calendar_dates",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("service_id", sa.String(length=128), nullable=False),
        sa.Column("date", sa.Integer(), nullable=False),
        sa.Column("exception_type", sa.SmallInteger(), nullable=False),
        sa.Column("holiday_name", sa.String(length=128), nullable=True),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("pk_id"),
    )
    op.create_index(
        "ix_static_calendar_dates_composite_1",
        "static_calendar_dates",
        ["static_version_key", "service_id", "date"],
        unique=False,
    )

    op.create_table(
        "static_directions",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("route_id", sa.String(length=60), nullable=False),
        sa.Column("direction_id", sa.Boolean(), nullable=True),
        sa.Column("direction", sa.String(length=30), nullable=False),
        sa.Column("direction_destination", sa.String(length=60), nullable=False),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("pk_id"),
    )
    op.create_index(
        "ix_static_directions_composite_1",
        "static_directions",
        ["static_version_key", "route_id", "direction_id"],
        unique=False,
    )

    op.create_table(
        "static_feed_info",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("feed_start_date", sa.Integer(), nullable=False),
        sa.Column("feed_end_date", sa.Integer(), nullable=False),
        sa.Column("feed_version", sa.String(length=75), nullable=False),
        sa.Column("feed_active_date", sa.Integer(), nullable=False),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.Column(
            "created_on",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("pk_id"),
        sa.UniqueConstraint("feed_version"),
        sa.UniqueConstraint("static_version_key"),
    )

    op.create_table(
        "static_routes",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("route_id", sa.String(length=60), nullable=False),
        sa.Column("agency_id", sa.SmallInteger(), nullable=False),
        sa.Column("route_short_name", sa.String(length=60), nullable=True),
        sa.Column("route_long_name", sa.String(length=150), nullable=True),
        sa.Column("route_desc", sa.String(length=40), nullable=True),
        sa.Column("route_type", sa.SmallInteger(), nullable=False),
        sa.Column("route_sort_order", sa.Integer(), nullable=False),
        sa.Column("route_fare_class", sa.String(length=30), nullable=False),
        sa.Column("line_id", sa.String(length=30), nullable=True),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("pk_id"),
    )
    op.create_index(
        "ix_static_routes_composite_1",
        "static_routes",
        ["static_version_key", "route_id", "route_type"],
        unique=False,
    )

    op.create_table(
        "static_stop_times",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("trip_id", sa.String(length=128), nullable=False),
        sa.Column("arrival_time", sa.Integer(), nullable=False),
        sa.Column("departure_time", sa.Integer(), nullable=False),
        sa.Column("schedule_travel_time_seconds", sa.Integer(), nullable=True),
        sa.Column("schedule_headway_trunk_seconds", sa.Integer(), nullable=True),
        sa.Column("schedule_headway_branch_seconds", sa.Integer(), nullable=True),
        sa.Column("stop_id", sa.String(length=60), nullable=False),
        sa.Column("stop_sequence", sa.SmallInteger(), nullable=False),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("pk_id"),
    )
    op.create_index(
        "ix_static_stop_times_composite_1",
        "static_stop_times",
        ["static_version_key", "trip_id", "stop_sequence"],
        unique=False,
    )
    op.create_index(
        "ix_static_stop_times_composite_2",
        "static_stop_times",
        ["static_version_key", "stop_id"],
        unique=False,
    )

    op.create_table(
        "static_stops",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("stop_id", sa.String(length=128), nullable=False),
        sa.Column("stop_name", sa.String(length=128), nullable=False),
        sa.Column("stop_desc", sa.String(length=256), nullable=True),
        sa.Column("platform_code", sa.String(length=10), nullable=True),
        sa.Column("platform_name", sa.String(length=60), nullable=True),
        sa.Column("parent_station", sa.String(length=30), nullable=True),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("pk_id"),
    )
    op.create_index(
        "ix_static_stops_composite_1",
        "static_stops",
        ["static_version_key", "stop_id"],
        unique=False,
    )
    op.create_index(
        "ix_static_stops_composite_2",
        "static_stops",
        ["static_version_key", "parent_station", "stop_id"],
        unique=False,
    )

    op.create_table(
        "static_trips",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("route_id", sa.String(length=60), nullable=False),
        sa.Column("branch_route_id", sa.String(length=60), nullable=True),
        sa.Column("trunk_route_id", sa.String(length=60), nullable=True),
        sa.Column("service_id", sa.String(length=60), nullable=False),
        sa.Column("trip_id", sa.String(length=128), nullable=False),
        sa.Column("direction_id", sa.Boolean(), nullable=True),
        sa.Column("block_id", sa.String(length=128), nullable=True),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("pk_id"),
    )
    op.create_index(
        "ix_static_trips_composite_1",
        "static_trips",
        ["static_version_key", "trip_id", "direction_id"],
        unique=False,
    )
    op.create_index(
        "ix_static_trips_composite_2",
        "static_trips",
        ["static_version_key", "branch_route_id"],
        unique=False,
    )
    op.create_index(
        "ix_static_trips_composite_3",
        "static_trips",
        ["static_version_key", "trunk_route_id"],
        unique=False,
    )

    op.create_table(
        "static_route_patterns",
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("route_id", sa.String(length=60), nullable=False),
        sa.Column("direction_id", sa.Boolean(), nullable=True),
        sa.Column("route_pattern_typicality", sa.SmallInteger(), nullable=True),
        sa.Column("representative_trip_id", sa.String(length=128), nullable=False),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("pk_id"),
    )
    op.create_index(
        "ix_static_route_pattern_composite_1",
        "static_route_patterns",
        ["static_version_key", "route_id", "direction_id"],
        unique=False,
    )

    op.create_table(
        "temp_event_compare",
        sa.Column("do_update", sa.Boolean(), nullable=True),
        sa.Column("do_insert", sa.Boolean(), nullable=True),
        sa.Column("pk_id", sa.Integer(), nullable=False),
        sa.Column("new_trip", sa.Boolean(), nullable=True),
        sa.Column("pm_trip_id", sa.Integer(), nullable=True),
        sa.Column("service_date", sa.Integer(), nullable=False),
        sa.Column("direction_id", sa.Boolean(), nullable=False),
        sa.Column("route_id", sa.String(length=60), nullable=False),
        sa.Column("start_time", sa.Integer(), nullable=True),
        sa.Column("vehicle_id", sa.String(length=60), nullable=False),
        sa.Column("stop_sequence", sa.SmallInteger(), nullable=True),
        sa.Column("stop_id", sa.String(length=60), nullable=False),
        sa.Column("parent_station", sa.String(length=60), nullable=False),
        sa.Column("vp_move_timestamp", sa.Integer(), nullable=True),
        sa.Column("vp_stop_timestamp", sa.Integer(), nullable=True),
        sa.Column("tu_stop_timestamp", sa.Integer(), nullable=True),
        sa.Column("trip_id", sa.String(length=128), nullable=False),
        sa.Column("vehicle_label", sa.String(length=128), nullable=True),
        sa.Column("vehicle_consist", sa.String(), nullable=True),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("pk_id"),
    )

    op.create_table(
        "vehicle_events",
        sa.Column("pm_event_id", sa.Integer(), nullable=False),
        sa.Column("service_date", sa.Integer(), nullable=False),
        sa.Column("pm_trip_id", sa.Integer(), nullable=False),
        sa.Column("stop_sequence", sa.SmallInteger(), nullable=True),
        sa.Column("canonical_stop_sequence", sa.SmallInteger(), nullable=True),
        sa.Column("sync_stop_sequence", sa.SmallInteger(), nullable=True),
        sa.Column("stop_id", sa.String(length=60), nullable=False),
        sa.Column("parent_station", sa.String(length=60), nullable=False),
        sa.Column("previous_trip_stop_pm_event_id", sa.Integer(), nullable=True),
        sa.Column("next_trip_stop_pm_event_id", sa.Integer(), nullable=True),
        sa.Column("vp_move_timestamp", sa.Integer(), nullable=True),
        sa.Column("vp_stop_timestamp", sa.Integer(), nullable=True),
        sa.Column("tu_stop_timestamp", sa.Integer(), nullable=True),
        sa.Column("travel_time_seconds", sa.Integer(), nullable=True),
        sa.Column("dwell_time_seconds", sa.Integer(), nullable=True),
        sa.Column("headway_trunk_seconds", sa.Integer(), nullable=True),
        sa.Column("headway_branch_seconds", sa.Integer(), nullable=True),
        sa.Column(
            "updated_on",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("pm_event_id"),
    )
    op.create_index(
        "ix_vehicle_events_composite_1",
        "vehicle_events",
        ["service_date", "pm_trip_id", "parent_station"],
        unique=True,
    )
    op.create_index(
        "ix_vehicle_events_composite_2",
        "vehicle_events",
        ["service_date", "pm_trip_id", "stop_sequence"],
        unique=False,
    )
    op.create_index(
        "ix_vehicle_events_vp_not_null",
        "vehicle_events",
        ["pm_event_id"],
        unique=False,
        postgresql_where=sa.text("vp_move_timestamp IS NOT NULL OR vp_stop_timestamp IS NOT NULL"),
    )

    op.create_table(
        "vehicle_trips",
        sa.Column("pm_trip_id", sa.Integer(), nullable=False),
        sa.Column("service_date", sa.Integer(), nullable=False),
        sa.Column("route_id", sa.String(length=60), nullable=False),
        sa.Column("direction_id", sa.Boolean(), nullable=False),
        sa.Column("start_time", sa.Integer(), nullable=True),
        sa.Column("vehicle_id", sa.String(length=60), nullable=False),
        sa.Column("branch_route_id", sa.String(length=60), nullable=True),
        sa.Column("trunk_route_id", sa.String(length=60), nullable=True),
        sa.Column("stop_count", sa.SmallInteger(), nullable=True),
        sa.Column("trip_id", sa.String(length=128), nullable=False),
        sa.Column("vehicle_label", sa.String(length=128), nullable=True),
        sa.Column("vehicle_consist", sa.String(), nullable=True),
        sa.Column("direction", sa.String(length=30), nullable=True),
        sa.Column("direction_destination", sa.String(length=60), nullable=True),
        sa.Column("static_trip_id_guess", sa.String(length=128), nullable=True),
        sa.Column("static_start_time", sa.Integer(), nullable=True),
        sa.Column("static_stop_count", sa.SmallInteger(), nullable=True),
        sa.Column("first_last_station_match", sa.Boolean(), nullable=False),
        sa.Column("static_version_key", sa.Integer(), nullable=False),
        sa.Column(
            "updated_on",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["static_version_key"],
            ["static_feed_info.static_version_key"],
        ),
        sa.PrimaryKeyConstraint("pm_trip_id"),
        sa.UniqueConstraint(
            "service_date",
            "route_id",
            "trip_id",
            name="vehicle_trips_unique_trip",
        ),
    )
    op.create_index(
        "ix_vehicle_trips_composite_1",
        "vehicle_trips",
        ["route_id", "direction_id", "vehicle_id"],
        unique=False,
    )

    create_update_on_function = """
        CREATE OR REPLACE FUNCTION update_modified_columns() 
        RETURNS TRIGGER AS $$ 
        BEGIN 
        NEW.updated_on = CURRENT_TIMESTAMP; 
        RETURN NEW;
        END; $$ LANGUAGE plpgsql
    """
    op.execute(create_update_on_function)

    for table in [
        "vehicle_events",
        "vehicle_trips",
    ]:
        trigger_name = f"update_{table}_modified".lower()
        create_trigger = """
            CREATE TRIGGER %s BEFORE UPDATE ON "%s" 
            FOR EACH ROW EXECUTE PROCEDURE update_modified_columns();
        """ % (
            trigger_name,
            table,
        )
        op.execute(create_trigger)

    op.execute(func_insert_feed_info)

    create_insert_into_feed_info_trigger = """
        CREATE TRIGGER insert_into_feed_info BEFORE INSERT ON static_feed_info 
        FOR EACH ROW EXECUTE PROCEDURE insert_feed_info();
    """
    op.execute(create_insert_into_feed_info_trigger)

    op.execute(func_red_is_ashmont_branch)

    op.execute(func_red_is_braintree_branch)

    op.execute(func_static_trips_branch_trunk)

    create_static_trips_create_branch_trunk = """
        CREATE TRIGGER static_trips_create_branch_trunk BEFORE INSERT ON static_trips 
        FOR EACH ROW EXECUTE PROCEDURE insert_static_trips_branch_trunk();
    """
    op.execute(create_static_trips_create_branch_trunk)

    op.execute(func_rt_red_is_braintree_branch)

    op.execute(func_rt_red_is_ashmont_branch)

    op.execute(func_rt_trips_branch_trunk)

    create_trigger = """
        CREATE TRIGGER rt_trips_update_branch_trunk BEFORE UPDATE ON vehicle_trips 
        FOR EACH ROW EXECUTE PROCEDURE update_rt_branch_trunk_id();
    """
    op.execute(create_trigger)

    op.execute(view_service_id_by_date_and_route)

    op.execute(view_static_service_id_lookup)

    op.execute(view_opmi_all_rt_fields_joined)


def downgrade() -> None:
    drop_opmi_all_rt_fields_joined = "DROP VIEW IF EXISTS opmi_all_rt_fields_joined;"
    op.execute(drop_opmi_all_rt_fields_joined)

    drop_static_service_id_lookup = "DROP VIEW IF EXISTS static_service_id_lookup;"
    op.execute(drop_static_service_id_lookup)

    drop_service_id_by_date_and_route = "DROP VIEW IF EXISTS service_id_by_date_and_route;"
    op.execute(drop_service_id_by_date_and_route)

    drop_trigger = "DROP TRIGGER IF EXISTS rt_trips_update_branch_trunk ON vehicle_trips;"
    op.execute(drop_trigger)

    drop_function = "DROP function if EXISTS public.update_rt_branch_trunk_id();"
    op.execute(drop_function)

    drop_function = "DROP function if EXISTS public.rt_red_is_ashmont_branch();"
    op.execute(drop_function)

    drop_function = "DROP function if EXISTS public.rt_red_is_braintree_branch();"
    op.execute(drop_function)

    drop_trigger = "DROP TRIGGER IF EXISTS static_trips_create_branch_trunk ON static_trips;"
    op.execute(drop_trigger)

    drop_function = "DROP function IF EXISTS public.red_is_braintree_branch();"
    op.execute(drop_function)

    drop_function = "DROP function IF EXISTS public.red_is_ashmont_branch();"
    op.execute(drop_function)

    drop_function = "DROP function IF EXISTS public.insert_static_trips_branch_trunk();"
    op.execute(drop_function)

    drop_trigger = "DROP TRIGGER IF EXISTS insert_into_feed_info ON static_feed_info;"
    op.execute(drop_trigger)
    drop_function = "DROP function IF EXISTS public.insert_feed_info();"
    op.execute(drop_function)

    for table in [
        "vehicle_events",
        "vehicle_trips",
    ]:
        trigger_name = f"update_{table}_modified".lower()
        drop_trigger = f"DROP TRIGGER IF EXISTS {trigger_name} on {table};"
        op.execute(drop_trigger)

    drop_update_on_and_triggers = "DROP function if EXISTS public.update_modified_columns();"
    op.execute(drop_update_on_and_triggers)

    op.drop_index("ix_vehicle_trips_composite_1", table_name="vehicle_trips")
    op.drop_table("vehicle_trips")

    op.drop_index("ix_vehicle_events_vp_not_null", table_name="vehicle_events")
    op.drop_index("ix_vehicle_events_composite_2", table_name="vehicle_events")
    op.drop_index("ix_vehicle_events_composite_1", table_name="vehicle_events")
    op.drop_table("vehicle_events")

    op.drop_table("temp_event_compare")

    op.drop_index(
        "ix_static_route_pattern_composite_1",
        table_name="static_route_patterns",
    )
    op.drop_table("static_route_patterns")

    op.drop_index("ix_static_trips_composite_3", table_name="static_trips")
    op.drop_index("ix_static_trips_composite_2", table_name="static_trips")
    op.drop_index("ix_static_trips_composite_1", table_name="static_trips")
    op.drop_table("static_trips")

    op.drop_index("ix_static_stops_composite_2", table_name="static_stops")
    op.drop_index("ix_static_stops_composite_1", table_name="static_stops")
    op.drop_table("static_stops")

    op.drop_index("ix_static_stop_times_composite_2", table_name="static_stop_times")
    op.drop_index("ix_static_stop_times_composite_1", table_name="static_stop_times")
    op.drop_table("static_stop_times")

    op.drop_index("ix_static_routes_composite_1", table_name="static_routes")
    op.drop_table("static_routes")

    op.drop_table("static_feed_info")

    op.drop_index("ix_static_directions_composite_1", table_name="static_directions")
    op.drop_table("static_directions")

    op.drop_index(
        "ix_static_calendar_dates_composite_1",
        table_name="static_calendar_dates",
    )
    op.drop_table("static_calendar_dates")

    op.drop_index("ix_static_calendar_composite_1", table_name="static_calendar")
    op.drop_table("static_calendar")

    op.drop_index("ix_metadata_log_not_processed", table_name="metadata_log")
    op.drop_table("metadata_log")
    # ### end Alembic commands ###
