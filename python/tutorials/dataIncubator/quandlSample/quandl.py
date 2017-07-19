import requests
from bokeh.plotting import figure
from bokeh.embed import components

# ----
#api_url = "https://www.quandl.com/api/v1/datasets/WIKI/%s.json" % stock
api_url = "https://www.quandl.com/api/v3/datasets/OPEC/ORB.json"
session = requests.Session()
session.mount('http://',requests.adapters.HTTPAdapter(max_retries=3))
raw_data = session.get(api_url)

print(raw_data)

# ----
plot = figure(tools=TOOLS,
              title='Data from Quandl OPEC Crude Oil Price',
              x_axis_label='date',
              x_axis_type='datetime'
              )

# ----
script, div = components(plot)
render_template('graph.html', script=script, div=div)
