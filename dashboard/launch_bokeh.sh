#!/bin/bash
bokeh serve \
	--address='*' \
	--port=8080 \
	--auth=auth.py \
	--allow-websocket-origin=100.26.136.186:8080 nyc_dash
