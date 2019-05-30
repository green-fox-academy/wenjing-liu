import reaction_user_counter from './reaction_user_counter_data.js'

function drawReactionUserCounter(raw_data) {
  var data = raw_data.slice(0, 15)
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
  
    d3.select('#reactionUserCounter svg')
        .datum(exampleData(data))
        .call(chart);
  
    nv.utils.windowResize(chart.update);
  
    return chart;
  });
}
  
  //Each bar represents a single discrete quantity.
function exampleData(data) {
  var result = [{key: "Reaction Counter", values: []}]
  data.forEach(item => {
    result[0].values.push({
      "label" : item['user_id'],
      "value" : item['count']
    })
  })
  return result
}

drawReactionUserCounter(reaction_user_counter)
