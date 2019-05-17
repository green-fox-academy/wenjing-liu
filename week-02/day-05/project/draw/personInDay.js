export default function drawPersonInDay(data) {
nv.addGraph(function() {
  var chart = nv.models.discreteBarChart()
      .x(function(d) { return d.label })    //Specify the data accessors.
      .y(function(d) { return d.value })
      .width(1000).height(500)
      .staggerLabels(true)    //Too many bars and not enough room? Try staggering labels.
      // .tooltips(false)        //Don't show tooltips
      .showValues(true)       //...instead, show the bar value right on top of each bar.
      // .transitionDuration(350)
      ;

  d3.select('#personInDayBarChart svg')
      .datum(exampleData(data))
      .call(chart);

  nv.utils.windowResize(chart.update);

  return chart;
});
}

//Each bar represents a single discrete quantity.
function exampleData(data) {
  console.log(data)
  var result = [{key: "Cumulative Return", values: []}]
  data.forEach(item => {
    result[0].values.push({
      "label" : (new Date(item['label'])).getDate() ,
      "value" : parseInt(item['value'])
    })
  })
  return result
}