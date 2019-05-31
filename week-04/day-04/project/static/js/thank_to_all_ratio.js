import raw_data from './thank_to_all_ratio_data.js'

function draw (raw_data) {
  nv.addGraph(function() {
    var chart = nv.models.pieChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .showLabels(true);
  
      d3.select("#thanksRatioInAll svg")
          .datum(formate_data(raw_data))
        .transition().duration(1200)
          .call(chart);
  
    return chart;
  });
}


function formate_data(raw_data) {
  let thank_ratio = (raw_data['thank_count'] / raw_data['total_count']) * 100
  let other_ratio = 100 - thank_ratio
  let results = [{
    "label": "Thanks",
    "value" : thank_ratio
  }, {
    "label": "Others",
    "value" : other_ratio
  }]
  return results
}

draw(raw_data)




