from bokeh.plotting import figure, output_file, show
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

## --Vectorized Colors and Sizes

# prepare some data
N = 4000
x_vcs = np.random.random(size=N)*100
y_vcs = np.random.random(size=N)*100
radii_vcs = np.random.random(size=N)*1.5
colors_vcs = [
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
