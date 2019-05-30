import user_msg_counter from './user_msg_counter_data.js'
function drawUserMsgCounter(raw_data) {
  var data = raw_data.slice(0, 20)

  nv.addGraph(function() {
    var chart = nv.models.multiBarHorizontalChart()
        .x(function(d) { return d.label })    //Specify the data accessors.
        .y(function(d) { return d.value })
        .width(1000).height(500)
        // .staggerLabels(true)    //Too many bars and not enough room? Try staggering labels.
        // .tooltips(false)        //Don't show tooltips
        .showValues(true)       //...instead, show the bar value right on top of each bar.
        // .transitionDuration(350)
        ;
  
    d3.select('#userMsgCounter svg')
        .datum(exampleData(data))
        .call(chart);
  
    nv.utils.windowResize(chart.update);
  
    return chart;
  });
  }
  
  //Each bar represents a single discrete quantity.
function exampleData(data) {
  var result = [{key: "Most Active Message Sender", values: []}]
  data.forEach(item => {
    result[0].values.push({
      "label" : item['user_id'],
      "value" : item['count']
    })
  })
  return result
}

drawUserMsgCounter(user_msg_counter)



