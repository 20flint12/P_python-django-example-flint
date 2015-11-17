#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
# linux hostname

HOSTNAME = os.uname()[1]


# Load defaults ---------------------------------------------------------------

# Server name
SERVER_NAME = 'Unknown server'
# Server ip
SERVER_IP = 'localhost'
# Mail to addresses
EMAIL_LIST = ["20flint12@gmail.com"]

# if HOSTNAME == "flint":                   # 192.168.1.13
#     SERVER_NAME = 'Ukrainian server_test'
#     SERVER_IP = '192.168.1.10'
#     EMAIL_LIST = ["20flint12@gmail.com"]
#
# elif HOSTNAME == "devkit-c03fd5603287":   # 192.168.1.10
#     SERVER_NAME = 'Ukrainian server'
#     SERVER_IP = 'localhost'
#     EMAIL_LIST = ["monitor@redpointpositioning.com", "20flint12@gmail.com"]
#
# elif HOSTNAME == "rbs-lidl":              # 10.8.1.122
#     SERVER_NAME = 'Italian server'
#     SERVER_IP = 'localhost'
#     EMAIL_LIST = ["monitor@redpointpositioning.com", "20flint12@gmail.com"]
#
# elif HOSTNAME == "devkit-b8aeed7097a8":   # 10.8.1.162
#     SERVER_NAME = "Boston's server"
#     SERVER_IP = 'localhost'
#     EMAIL_LIST = ["monitor@redpointpositioning.com", "20flint12@gmail.com"]


print "HOSTNAME   :", HOSTNAME
print "SERVER_NAME:", SERVER_NAME
print "SERVER_IP  :", SERVER_IP

#------------------------------------------------------------------------------


# EMAIL_SENDER   = "ssurmilo@redpointpositioning.com"
# EMAIL_USERNAME = "ssurmilo@redpointpositioning.com"
# EMAIL_PASSWORD = "$rpp20flint12"

EMAIL_SENDER   = "astroreminder@gmail.com"
EMAIL_USERNAME = "astroreminder@gmail.com"
EMAIL_PASSWORD = "95dd2d30 "


# Nodes snapshot file name
MAIN_SNAP_FILE = 'nodes_main_snapshot.xml'
LAST_SNAP_FILE = 'nodes_last_snapshot.xml'

# Nodes last differences, timers for HB
LAST_DIFF_FILE = 'nodes_last_diff.xml'

# Mobile excluded
EXC_MOBILE = True

# Get snapshot
GET_SNAP = False

# Include only nodes with changes
ONLY_CHANGES = True

# Full time interval for snapshot
FULL_TIME_SNAP = "50d"
# Current time interval for snapshot (5 * report time)
CURR_TIME_SNAP = "15m"  # "150s" "15m"

# Exceeding the time interval (HB report)
EXC_TIME_INTERVAL = 5   # 5



USED_FIELDS = [
        # "root_formed_timestamp",
        "parent_mac_address",
        # "updated_at",
        "position_z",
        "position_x",
        "position_y",
        "id",
        "node_type_id",
        "current_system_timestamp",
        "battery_voltage",
        "mobile_dimension_mode",
        "mac_address",
        "ranging_frequency",
        "bridge_mac_address",
        "sw_version",
        "root_formed",
        "sublocation_id",
        # "position_update_timestamp",
        "battery_remaining_charge",
        "name",
        "created_at",
        # "announce_timestamp",
        "reporting_frequency",
        "last_heard",
        "sequence_number",
]


CHECKED_FIELDS = [
        # "root_formed_timestamp",
        # "parent_mac_address",
        # "updated_at",
        "position_z",               # include always !!!
        "position_x",               # include always !!!
        "position_y",               # include always !!!
        # "id",
        "node_type_id",             # include always !!!
        # "current_system_timestamp",
        # "battery_voltage",
        # "mobile_dimension_mode",
        "mac_address",
        # "ranging_frequency",
        # "bridge_mac_address",
        "sw_version",
        # "root_formed",
        "sublocation_id",
        # "position_update_timestamp",
        # "battery_remaining_charge",
        "name",
        # "created_at",
        # "announce_timestamp",
        "reporting_frequency",
        # "last_heard",
        # "sequence_number",
]


# Required fields
PRINT_FIELDS = [
        # "root_formed_timestamp",
        # "parent_mac_address",
        # "updated_at",
        # "position_z",
        # "position_x",
        # "position_y",
        "id",
        "node_type_id",
        # "current_system_timestamp",
        # "battery_voltage",
        # "mobile_dimension_mode",
        "mac_address",
        # "ranging_frequency",
        # "bridge_mac_address",
        "sw_version",
        # "root_formed",
        # "sublocation_id",
        # "position_update_timestamp",
        # "battery_remaining_charge",
        "name",
        # "created_at",
        # "announce_timestamp",
        # "reporting_frequency",
        # "last_heard",
        # "sequence_number",


        # Calculated fields ######################################
        "node_type_id_changed",
        "bridge_has_wrong_parent",
]


# Sort output with priority
PRINT_ORDER = [
        "id",
        "mac_address",
        "sw_version",
        "node_type_id",
        "name",
        "state",

        "position_x",
        "position_y",
        "position_z",
        "sublocation_id",
        "reporting_frequency",

        "node_type_id_changed",
        "bridge_has_wrong_parent",

        "miss_HBs",

]





