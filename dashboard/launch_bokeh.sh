#!/bin/bash
bokeh serve \
	--address='*' \
	--port=8080 \
	--auth=auth.py \
	--allow-websocket-origin=<your_ip_address>:8080 nyc_dash
