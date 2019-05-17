///==============Pie chart for late to not late in month
//Regular pie chart example
export default function lateNotLatePieChart(exampleData){
  nv.addGraph(function() {
    var chart = nv.models.pieChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .showLabels(true);
      d3.select("#lateToNotLatePieChart svg")
          .datum(exampleData)
          .transition().duration(350)
          .call(chart);
    return chart;
  });
  
  //Donut chart example
  nv.addGraph(function() {
    var chart = nv.models.pieChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        // .width(1000).height(1000)
        .showLabels(true)     //Display pie labels
        .labelThreshold(.05)  //Configure the minimum slice size for labels to show up
        .labelType("percent") //Configure what type of data to show in the label. Can be "key", "value" or "percent"
        .donut(true)          //Turn on Donut mode. Makes pie chart look tasty!
        .donutRatio(0.35)     //Configure how big you want the donut hole size to be.
        ;
  
      d3.select("#lateToNotLatePieChart svg")
          .datum(exampleData)
          .transition().duration(350)
          .call(chart);
  
    return chart;
  });
}




