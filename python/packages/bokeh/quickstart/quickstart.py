from bokeh.layouts import gridplot
from bokeh.plotting import * # figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.sampledata.stocks import AAPL
import numpy as np


## -- Line Plot example

# Some sample data, prepared
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML File
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example",
    x_axis_label='x',
    y_axis_label='y')

# add a line renderer with a legend and line thickness
p.line(x,y,legend="Temp.", line_width=2)

# show the results
show(p)

## -- Log Plot example

# preparesome data
x0 = [0.1,0.5,1.0,1.5,2.0,2.5,3.0]
y0 = [i**2 for i in x0]
y1 = [10**i for i in x0]
y2 = [10**(i**2) for i in x0]

# output to static HTML File
output_file("log_lines.html")

# create a new plot
p2 =figure(
    tools="pan,box_zoom,reset,save",
    y_axis_type="log",
    y_range=[0.001,10**11],
    title="log axis example",
    x_axis_label="sections",
    y_axis_label="particles"
)

# add some renderers
p2.line(x0, x0, legend="y=x")
p2.circle(x0, x0, legend="y=x", fill_color="white",size=8)
p2.line(x0,y0,legend="y=x^2", line_width=3)
p2.line(x0,y1,legend="y=10^x", line_color="red")
p2.circle(x0,y1,legend="y=10^x",fill_color="red",line_color="red",size=6)
p2.line(x0,y2,legend="y=10^x^2",line_color="orange",line_dash="4 4")

# show the results
show(p2)

## ---- Vectorized Colors and Sizes

# prepare some data
N = 4000
x_vcs = np.random.random(size=N)*100
y_vcs = np.random.random(size=N)*100
radii_vcs = np.random.random(size=N)*1.5
colors_vcs =    [
                    "#%02x%02x%02x" % (int(r), int(g),150)
                    for r,g in zip(50+2*x_vcs,30+2*y_vcs)
                ]

# output to static HTML file (with CDN resources)
output_file("color_scatter.html",
            title="color_scatter.pty example",
            mode="cdn")

TOOLS_vcs="resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

# create a new plot with the tools above, and explicit ranges
p3 = figure(tools=TOOLS_vcs, x_range=(0,100), y_range=(0,100))

# add a circle renderer with vectorized colors and sizes
p3.circle(  x_vcs,
            y_vcs,
            radius=radii_vcs,
            fill_color=colors_vcs,
            fill_alpha=0.6,
            line_color=None)

show(p3)

## ---- Linked panning and brushing

# Prepare some data
N4 = 100
x4 = np.linspace(0,4*np.pi, N4)
y04 = np.sin(x4)
y14 = np.cos(x4)
y24 = np.sin(x4) + np.cos(x4)

# output to static HTML File
output_file("linked_panning.html")

# create a new plot
s1 = figure(width=250,
            plot_height=250,
            title=None)
s1.circle(  x4,
            y04,
            size=10,
            color="navy",
            alpha=0.5)

# NEW create a new pplot and share both ranges
s2 = figure(width=250,
            height=250,
            x_range=s1.x_range,
            y_range=s1.y_range,
            title=None)
s2.triangle(x4,y14,size=10,color="firebrick",alpha=0.5)

# NEW create a new plot and shareonly one range
s3 = figure(width=250,
            height=250,
            x_range=s1.x_range,
            title=None)
s3.square(x4,y24,size=10,color="olive",alpha=0.5)

# NEW put the plots in a gridplot
p4 = gridplot([[s1,s2,s3]],toolbar_location=None)

# show the results
show(p4)

## ---- Linked brushing example

# prepare some date
N5 = 300
x5 = np.linspace(0,4*np.pi, N5)
y05 = np.sin(x5)
y15 = np.cos(x5)

# output to static HTML File
output_file("linked_brushing.html")

# NEW: create a column data source for the plots to share
source = ColumnDataSource(data=dict(x5=x5,y05=y05,y15=y15))

TOOLS5 = "pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select"

# create a new plot and add a renderer
left = figure(tools=TOOLS5,width=350,height=350,title=None)
left.circle('x5','y05',source=source)

# create another new plot and add a renderer
right = figure(tools=TOOLS5,width=350,height=350,title=None)
right.circle('x5','y15',source=source)

# put the subplots in a gridplot
p5 = gridplot([[left,right]])
show(p5)

## ---- Datetime axes

# prepare some data
aapl = np.array(AAPL['adj_close'])
aapl_dates = np.array(AAPL['date'],dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
aapl_avg = np.convolve(aapl,window,'same')

# output to static HTML File
output_file("stocks.html", title="stocks.py example")

# create a new plot with a datetime axis type
p6 = figure(width=800,height=300,x_axis_type="datetime")

# add renderers
p6.circle(aapl_dates, aapl, size=4, color="darkgrey",alpha=0.2, legend='close')
p6.line(aapl_dates, aapl_avg, color="navy",legend="avg")

# NEW: customize by setting attributes
p6.title.text = "AAPL One-Month Average"
p6.legend.location = "top_left"
p6.grid.grid_line_alpha = 0
p6.xaxis.axis_label = "Date"
p6.yaxis.axis_label = "Price"
p6.ygrid.band_fill_color = "olive"
p6.ygrid.band_fill_alpha = 0.1

# show the results
show(p6)
