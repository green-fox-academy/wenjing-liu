/*These lines are all chart setup.  Pick and choose which chart features you want to utilize. */
export default function draw (averageData) {
  nv.addGraph(function() {
    var chart = nv.models.lineChart().forceY([4, 20])
                  .margin({left: 100})  //Adjust chart margins to give the x-axis some breathing room.
                  .useInteractiveGuideline(true)  //We want nice looking tooltips and a guideline!
                  .showLegend(true)       //Show the legend, allowing users to turn on/off line series.
                  .showYAxis(true)        //Show the y-axis
                  .showXAxis(true)        //Show the x-axis
                  // .x(function(d) { return d.label })
                  // .y(function(d) { return d.value })
                  .width(1000).height(500)
                  
    ;

    chart.xAxis     //Chart x-axis settings
        .axisLabel('Time (Date)')
        .ticks(10)
        // .tickFormat(d3.format(',r'));

    chart.yAxis     //Chart y-axis settings
        .axisLabel('Time(hour.min)')
        // .tickFormat(d3.format(',f'));

    /* Done setting the chart up? Time to render it!*/
    var myData = getData(averageData);   //You need data...

    d3.select('#averageArrivingTimeByDay svg')    //Select the <svg> element you want to render the chart in.   
        .datum(myData)         //Populate the <svg> element with chart data...
        .call(chart);          //Finally, render the chart!

    //Update the chart when window resizes.
    nv.utils.windowResize(function() { chart.update() });
    return chart;
  });
}

function getData(averageData) {
  var data = []
  var valueData = averageData[0]['values']
  for (var i = 0; i < valueData.length; i++) {
    var totalSeconds = valueData[i]['y']
    var hours = Math.floor(totalSeconds / 3600);
    totalSeconds %= 3600;
    var minutes = Math.floor(totalSeconds / 60);  
    var yValue = hours + minutes * 0.01
    data.push({x: (new Date(valueData[i]['x']).getDate()), y: yValue.toFixed(2)});
  }
  

  //Line chart data should be sent as an array of series objects.
  return [
    {
      values: data,      //values - represents the array of {x,y} data points
      key: 'Average Arriving Time By Day', //key  - the name of the series.
      color: '#ff7f0e'  //color - optional: choose your own line color.
    }
  ];
}




// export default function  drawAverageTimeByDay (data) {
//   var averageData = data[0]
//   var averageValues = averageData['values']
//   var days = []
//   var tickValues = []
//   averageValues.forEach(item => {
//     days.push(item['x'])
//     tickValues.push(tickValues.length)
//   })
//   console.log(days)
//   console.log(tickValues)

//   var time_duration = ['07:00:00', '08:00:00', '09:00:00', '10:00:00', '11:00:00', '12:00:00', '13:00:00']

//   var format = d3.time.format("%Y-%m-%d");
//   var x = d3.time.scale()
//     .domain([format.parse(days[0]),
//              format.parse(days[days.length-1])])
//     .range([0, 600])
    
// nv.addGraph(function () {
//   var chart = nv.models.lineChart() // Initialise the lineChart object.
//     .width(800).height(500); // Turn on interactive guideline (tooltips) 
// chart.xAxis
//     .scale(x)
//     .orient("bottom")
//     .ticks(10)
//     .tickFormat(d3.time.format("%Y-%m-%d"))
//     .axisLabel('Jan 2019 (Day)'); // Set the label of the xAxis (Vertical)
// chart.yAxis
//     .axisLabel('Time (h:m:s)') // Set the label of the xAxis (Horizontal)
//     .tickFormat(function(d) {
//       // console.log(d)
//       return d3.time.format('%H:%M')(new Date(d));
//     })
//     // .tickFormat(d3.format('.02f')); // Rounded Numbers Format.
// d3.select('#averageArrivingTimeByDay svg') // Select the ID of the html element we defined earlier.
//     .datum(data) // Pass in the JSON
//     // .transition().duration(500) // Set transition speed
//     .call(chart); // Call & Render the chart
//   nv.utils.windowResize(chart.update); // Intitiate listener for window resize so the chart responds and changes width.
//   return;
// });
// }