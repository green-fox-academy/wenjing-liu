import raw_data from  './avg_msg_counter_hour_day_data.js'


function draw(raw_data) {
  
  nv.addGraph(function() {
    var chart = nv.models.lineChart()
      .useInteractiveGuideline(true);
  
    chart.xAxis
      .axisLabel('Hour (h)')
      .tickFormat(d3.format(',r'));
  
    chart.yAxis
      .axisLabel('Count')
      .tickFormat(d3.format('.02f'));
  
    d3.select('#avgMsgCounterHourDay svg')
      .datum(formate_data(raw_data))
      .transition().duration(500)
      .call(chart);
  
    nv.utils.windowResize(chart.update);
  
    return chart;
  });
}

function formate_data(data) {
  var result = []
  data.forEach(item => {
    result.push({
      x: item['hour'],
      y: item['count']
    })
  })
  return [
    {
      values: result,
      key: 'msg in hour avg day',
      color: '#ff7f0e'
    }
  ]
}

draw(raw_data)