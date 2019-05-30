import reaction_counter from './reaction_counter_data.js'


function draw(raw_data) {

  nv.addGraph(function() {
    var chart = nv.models.scatterChart()
                  .showDistX(true)    //showDist, when true, will display those little distribution lines on the axis.
                  .showDistY(true)
                  // .transitionDuration(350)
                  .color(d3.scale.category10().range());

    //Configure how the tooltip looks.
    // chart.tooltipContent(function(key) {
    //     return '<h3>' + key + '</h3>';
    // });

    //Axis settings
    chart.xAxis.tickFormat(d3.format('.02f'));
    chart.yAxis.tickFormat(d3.format('.02f'));

    //We want to show shapes other than circles.
    // chart.scatter.onlyCircles(false);

    // var myData = randomData(4,40);
    var myData = formate_data(raw_data)
    d3.select('#chart svg')
        .datum(myData)
        .call(chart);

    nv.utils.windowResize(chart.update);

    return chart;
  });
}

/**************************************
 * Simple test data generator
 */
function randomData(groups, points) { //# groups,# points per group
  var data = [],
      shapes = ['circle', 'cross', 'triangle-up', 'triangle-down', 'diamond', 'square'],
      random = d3.random.normal();

  for (var i = 0; i < groups; i++) {
    data.push({
      key: 'Group ' + i,
      values: []
    });

    for (var j = 0; j < points; j++) {
      data[i].values.push({
        x: random()
      , y: random()
      , size: Math.random()   //Configure the size of each scatter point
      , shape: (Math.random() > 0.95) ? shapes[j % 6] : "circle"  //Configure the shape of each scatter point.
      });
    }
  }

  return data;
}

function formate_data(raw_data) {
  var data = [],
      shapes = ['circle', 'cross', 'triangle-up', 'triangle-down', 'diamond', 'square'],
      random = d3.random.normal();
  data.push({
    key: 'Group ' + 1,
    values: []
  });
  var i = 0
  raw_data.forEach(item => {
    data[0].values.push({
      x: random()
    , y: random()
    , size: item['count']  //Configure the size of each scatter point
    , shape: shapes[item['count'] % 6]  //Configure the shape of each scatter point.
    })
  })
  return data;
}


draw(reaction_counter)