# Desc: File that utilizes Bokeh to generate plot of age by zipcode
#
# Written in Python 3.4
# Last updated: 4/11/2017

from bokeh.charts import BoxPlot, output_file, show
import bokeh, pandas

# Creating pandas dataframe for Bokeh to use
df = pandas.read_csv("mow-data-final-ageadded.csv")

# Creating a graph
p = BoxPlot(df, values='age', label='zipcode',
            title="Age Distribution Per Zipcode", legend=False)

output_file("age-vs-zipcode-wp.html")

show(p)
