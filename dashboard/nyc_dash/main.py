from bokeh.layouts import column
from bokeh.models import Button, Dropdown, CustomJS, Legend, LegendItem
from bokeh.plotting import figure, curdoc  # curdoc is web document
from bokeh.io import show
import pandas as pd
import math

averages = pd.read_csv("averages.csv")
zip_list = [averages.columns[k] for k in range(2, len(averages.columns))]
x = [k for k in range(1, 13)]
y_all = [averages.loc[i]['All'] if averages.loc[i]['All'] != 0 else math.nan for i in range(12)]

selected_zipcode1 = None
selected_zipcode2 = None

need_to_add_zipcode1 = False
need_to_add_zipcode2 = False


def update_legend(ix):
    global need_to_add_zipcode1
    global need_to_add_zipcode2
    if need_to_add_zipcode2:
        legend.append(LegendItem(label=selected_zipcode2, renderers=[r2]))
    if need_to_add_zipcode1:
        if len(legend) == 1:
            legend.append(LegendItem(label=selected_zipcode1, renderers=[r1]))
        else:
            legend.insert(1, LegendItem(label=selected_zipcode1, renderers=[r1]))


    if ix == 1:
        if not need_to_add_zipcode1:
            legend[1] = LegendItem(label=selected_zipcode1, renderers=[r1])

    if ix == 2:
        if not need_to_add_zipcode2:
            if len(legend) == 3:
                legend[2] = LegendItem(label=selected_zipcode2, renderers=[r2])
            else:
                legend[1] = LegendItem(label=selected_zipcode2, renderers=[r2])


def handler1(event):
    global selected_zipcode1
    global need_to_add_zipcode1
    if selected_zipcode1 is None:
        need_to_add_zipcode1 = True
    else:
        need_to_add_zipcode1 = False
    zipcode = event.item
    selected_zipcode1 = zipcode
    update_legend(1)
    need_to_add_zipcode1 = False
    y1 = [averages.loc[i][zipcode] if averages.loc[i][zipcode] != 0 else math.nan for i in range(12)]
    new_data = {}
    new_data['x'] = ds1.data['x']
    new_data['y'] = y1
    p.legend.items = legend
    ds1.data = new_data


def handler2(event):
    global selected_zipcode2
    global need_to_add_zipcode2
    if selected_zipcode2 is None:
        need_to_add_zipcode2 = True
    else:
        need_to_add_zipcode2 = False
    zipcode = event.item
    selected_zipcode2 = zipcode
    update_legend(2)
    need_to_add_zipcode2 = False
    y2 = [averages.loc[i][zipcode] if averages.loc[i][zipcode] != 0 else math.nan for i in range(12)]
    new_data = {}
    new_data['x'] = ds2.data['x']
    new_data['y'] = y2
    p.legend.items = legend
    ds2.data = new_data


dropdown1 = Dropdown(label="Select zipcode 1", button_type="success", menu=zip_list)
dropdown2 = Dropdown(label="Select zipcode 2", button_type="success", menu=zip_list)

p = figure(x_axis_label='Month when SR was created', y_axis_label='Average Response Time (Hours)')

r_all = p.line(x, y_all, line_width=3, line_color="red", legend_label="All")
r1 = p.line(x, [math.nan for i in range(12)], line_width=3, line_color="green")
r2 = p.line(x, [math.nan for i in range(12)], line_width=3, line_color="blue")

legend = [LegendItem(label="All", renderers=[r_all])]

p.legend.title = 'Zip code'
ds1 = r1.data_source
ds2 = r2.data_source
# p.legend.items = [LegendItem(label="test2", renderers=[r_all])]
# r_all = p.line()
# r2 = p.line()
# r3 = p.line()
# ds_all = r_all.data_source
# ds2 = r2.data_source
# ds3 = r3.data_source

dropdown1.on_click(handler1)
dropdown2.on_click(handler2)

# p.line(x, y)
# r2 = p.line()
# r3 = p.line()


curdoc().add_root(column(dropdown1, dropdown2, p))

#######################################################
# num_circles = 10


# LOAD DATA
# x = [random()*70 for i in range(num_circles)]
# y = [random()*70 for i in range(num_circles)]


# GENERATE PLOTS
# p = figure(x_range=(0, 100), y_range = (0, 100))
# r = p.circle(x, y, size=5)

# HANDLE CALLBACKS ... user interactions
# ds = r.data_source

# def add_circle():
#    new_data = {}
#    new_data['x'] = ds.data['x'] + [random()*70]
#    new_data['y'] = ds.data['y'] + [random()*70]

#    ds.data = new_data

# create interactive widgets
# b = Button(label='Add circle')
# b.on_click(add_circle)

# format/create the document
# curdoc().add_root(column(b, p))
