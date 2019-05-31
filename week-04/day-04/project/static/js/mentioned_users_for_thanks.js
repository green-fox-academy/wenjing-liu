import raw_data from './mentioned_users_for_thanks_data.js'


function drawThankUserMsgCounter(raw_data) {
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
  
    d3.select('#thankedUserCounter svg')
        .datum(formate_data(data))
        .call(chart);
  
    nv.utils.windowResize(chart.update);
  
    return chart;
  });
  }
  
  //Each bar represents a single discrete quantity.
function formate_data(data) {
  var result = [{key: "Thanks Recived Users", values: []}]
  data.forEach(item => {
    result[0].values.push({
      "label" : item['user_id'],
      "value" : item['count']
    })
  })
  return result
}

drawThankUserMsgCounter(raw_data)



