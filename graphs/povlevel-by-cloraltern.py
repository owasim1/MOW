# Desc: File that utilizes Bokeh to generate plot of aggregate count of
#       povlevel by cloraltern
#
# Written in Python 3.4
# Last updated: 4/11/2017

from bokeh.charts import Bar, output_file, show
import bokeh, pandas

# Creating pandas dataframe for Bokeh to use
df = pandas.read_csv("mow-data-final.csv")

# Creating a bar graph
p = Bar(df, label='cloraltern', values='povlevel', agg='count', stack='povlevel',
        title="Poverty Level Distribution of Clients or Alternates", legend='top_left')

output_file("povlevel-vs-cloraltern-wp.html")

show(p)
