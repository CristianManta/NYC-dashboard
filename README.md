## NYC 311 service Bokeh dahboard
This repository contains code and data to run a fully functional authenticated Bokeh dashboard. The data itself is not updated live. It comes from https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9 and it has been trimmed down and cleaned.

The dashboard contains the average response time it took for a service request to be resolved in 2020 as a function of the month when the SR was created. Different zipcodes can be selected to adjust the line plot.

To launch the server, you need to cd into the `dashboard` directory and run

```
bash launch_bokeh.sh
```

Make sure to modify the ip address in that script so that it matches the one of your server.
### Screenshot
![example](/figures/example.png)
