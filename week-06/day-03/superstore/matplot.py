
#%%
import pandas as pd
import numpy as np
import matplotlib
import datetime
from matplotlib import pyplot as plt
import os
 
def load_data(path):
  return pd.read_excel(path, index_col=0)

#%%
#A) What is the percentage contribution of each region to overall sales?
def draw_region_to_sales():
  sales = load_data('Superstore_Sales.xls')
  labels = sales['Region'].unique()
  explode = (0, 0, 0.3, 0)
  sizes = sales['Sales'].groupby(sales['Region']).sum()
  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',startangle=90)
  ax1.axis('equal')
  plt.show()
  fig1.savefig('region_to_sales')

# draw_region_to_sales()

#%%
#B) What are the overal sales month by month?
def draw_sales_by_month():
  sales = load_data('Superstore_Sales.xls')
  sales_overtime = sales[['Order Date', 'Sales']]
  sales_overtime.sort_values(by=['Order Date'], inplace = True)
  x = np.array(sales_overtime['Order Date'].unique())
  y = np.array(sales_overtime['Sales'].astype(int).groupby(sales_overtime['Order Date']).sum())
  plt.plot(x, y, 'm')
  # plt.show()
  plt.savefig('sales_by_month')

# draw_sales_by_month()

#%%
# C) Which sub-category brought the highest profits?
def draw_category_to_profits():
  sales = load_data('Superstore_Sales.xls')
  profits_sub_category = sales[['Profit', 'Product Sub-Category']]
  profits_sub_category.sort_values(by=['Product Sub-Category'], inplace = True)
  data = profits_sub_category.groupby(profits_sub_category['Product Sub-Category']).sum()
  names = np.array(profits_sub_category['Product Sub-Category'].unique())
  values = np.array(profits_sub_category['Profit'].astype(int).groupby(profits_sub_category['Product Sub-Category']).sum())
  fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
  axs[0].bar(names, values)
  # plt.show()
  fig.savefig('category_to_profits')

# draw_category_to_profits()

#%%
# D) Map the amount of high-priority shipments within 2010 on a timeline.
def draw_high_priority_shipments():
  sales = load_data('Superstore_Sales.xls')
  order_pr_date = sales[['Order Date', 'Order Priority']][(sales['Order Priority'] == 'High') & (sales['Order Date'].between('2010-01-01', '2010-12-31'))]
  order_pr_date.sort_values(by=['Order Date'], inplace=True)
  x = order_pr_date['Order Date'].unique()
  y = order_pr_date['Order Priority'].groupby(order_pr_date['Order Date']).count()
  fig, ax = plt.subplots()
  ax.plot(x, y)
  ax.set(xlabel='date (d)', ylabel='count',
       title='amount of high-priority shipments within 2010')
  ax.grid()
  plt.show()
  fig.savefig('high-priority_shipments')

draw_high_priority_shipments()

#%%
# Graph out the minimum and maximum shipping costs per container type.
def draw_min_max_shipping_cost():
  sales = load_data('Superstore_Sales.xls')
  cost_container_type = sales[['Product Container', 'Shipping Cost']].sort_values(by=['Product Container'])
  labels = np.array(cost_container_type['Product Container'].unique())
  max = np.array(cost_container_type.groupby(cost_container_type['Product Container'])['Shipping Cost'].max())
  min = np.array(cost_container_type.groupby(cost_container_type['Product Container'])['Shipping Cost'].min())
  
  ind = np.arange(len(labels)) # the x locations for the groups
  width = 0.35  # the width of the bars

  fig, ax = plt.subplots()
  rects1 = ax.bar(ind - width/2, max, width,
                  label='Max')
  rects2 = ax.bar(ind + width/2, min, width,
                  label='Min')
  # Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_ylabel('Cost($)')
  ax.set_xlabel('Container type')
  ax.set_title('Minimum and maximum shipping costs per container type')
  ax.set_xticks(ind)
  ax.set_xticklabels(labels)
  ax.legend()

  def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

  
  autolabel(rects1, "left")
  autolabel(rects2, "right")
  fig.tight_layout()
  plt.show()
  fig.savefig('min_max_cost_container_type')


# draw_min_max_shipping_cost()

#%%
# Compare profits per category amongst the different regions
def draw_profits_catergory_region():
  sales = load_data('Superstore_Sales.xls')
  profit_catergory_region = sales[['Profit', 'Product Category', 'Region']]
  profit_catergory_region.sort_values(by=['Product Category', 'Region'])

  labels = np.array(profit_catergory_region['Product Category'].unique())
  label_data = {} 
  for label in labels:
    data = profit_catergory_region[profit_catergory_region['Product Category'] == label]
    data.sort_values(by=['Region'], inplace=True)
    result = {}
    regions = data['Region'].unique()
    profits = data.groupby(['Region'])['Profit'].sum()
    for i in range(len(regions)):
      result[regions[i]] = profits[i]
    label_data[label] = result
  df = pd.DataFrame(label_data)
  regions = df.index.values


  ind = np.arange(len(labels)) # the x locations for the groups
  width = 0.2  # the width of the bars
  mid_ = len(regions)/2+1

  fig, ax = plt.subplots()
  rects = []
  i = 0
  for region in regions:
    i += 1
    width_ = (i - mid_) * width
    rects.append(ax.bar(ind + width_, np.array(df.loc[region]), width,
                  label=region))
  # Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_ylabel('Cost($)')
  ax.set_xlabel('Category')
  ax.set_title('Profits per category amongst the different regions')
  ax.set_xticks(ind - width/2)
  ax.set_xticklabels(labels)
  ax.legend()
  fig.tight_layout()
  plt.show()
  fig.savefig('profits_per_category')



draw_profits_catergory_region()

#%%
