# encoding = utf-8

import json
import time
from datetime import datetime


def validate_input(helper, definition):
    interval = definition.parameters.get("interval")
    interval = int(interval)
    if interval < 5*60 or interval > 3*24*60*60:
        raise ValueError("Collect interval must be within 5 minutes and 3 days")

def collect_events(helper, ew):
    loglevel = helper.get_log_level()
    helper.set_log_level(loglevel)
    run_time = time.time()

    url_base = "https://urlhaus-api.abuse.ch"
    url_endpoint = "/v1/payloads/recent/"
    check_point_key = helper.get_input_stanza_names()

    is_proxy = False
    if helper.get_proxy():
        is_proxy = True

    start_time = None
    last_ran = helper.get_check_point(check_point_key)
    if not last_ran:
        start_time = datetime.fromtimestamp(0)
        helper.log_info("Fetching URLhaus Payloads for the last 3 days")
    else:
        start_time = datetime.fromtimestamp(last_ran)
        helper.log_info(f"Fetching URLhaus Payloads since {start_time} UTC")

    headers = {"Content-Type": "application/json"}
    url = url_base + url_endpoint
    resp = helper.send_http_request(
        url,
        "GET",
        parameters=None,
        payload=None,
        headers=None,
        timeout=30,
        verify=False,
        use_proxy=is_proxy,
    )
    resp.raise_for_status()
    respdata = resp.json()["payloads"]

    helper.log_info(f"Parsing {len(respdata)} URLhaus Payloads events")
    for event in respdata:
        ioc_time = datetime.strptime(event["firstseen"], "%Y-%m-%d %H:%M:%S")
        if ioc_time < start_time:
            continue

        e = helper.new_event(
            data=json.dumps(event),
            source=helper.get_input_type(),
            index=helper.get_output_index(),
            sourcetype=helper.get_sourcetype(),
            done=True,
        )
        ew.write_event(e)

    helper.save_check_point(check_point_key, run_time)
