import reaction_counter from './reaction_counter_data.js'

function formate_data(raw_data) {
   var data = raw_data.slice(0, 10)
    var result = []
    data.forEach(item => {
      result.push({
        "key" : item['reaction'],
        "value" : parseInt(item['count'])
      })
    })
    return result
  }

let data = formate_data(reaction_counter)
let Xdatas = data.map(function(d) {return d.key}),
Ydatas = data.map(function(d) {return d.value});
let width = 800, height = 500;
let x = d3.scaleBand().domain(Xdatas).rangeRound([0, width]).padding(0.1);
let y = d3.scaleLinear().domain([0, d3.max(Ydatas)]).rangeRound([height, 0]);

let padding = {left: 50, top: 70, right: 50, bottom: 100};
let svg = d3.select('body #reactionCounter').append('svg').attr('width', width + padding.left)
.attr('height', height + padding.bottom);
let g = svg.append('g').attr('transform', 'translate(' + padding.left + ',' + padding.top + ')');
// 表头
// svg.append('text').attr('transform', 'translate(' + (width/2 - padding.left) + ',' + padding.top/2 + ')')
// .attr('font-weight', 600).text('Top 10 Mostly Used Reactions');
// x轴和y轴
g.append('g').attr('transform', 'translate(0,' + height + ')')
.call(d3.axisBottom(x));
g.append('g').call(d3.axisLeft(y).ticks(10));

var chart = g.selectAll('.bar').data(data).enter().append('g');
// 矩形
chart.append('rect')
.attr('x', function(d) {
return x(d.key);
})
.attr('cursor', 'pointer')
.attr('y', function(d) {
return y(y.domain()[0]) - 5;
})
.attr('fill', function(d) {
// 生成随机颜色
return '#'+Math.floor(Math.random()*0xffffff).toString(16);
})
.attr('stroke', '#FFF').attr('stroke-width', '3px')
.transition()
.delay(function(d, i) {
return (i + 1) * 50
})
.duration(2000).ease(d3.easeBounceIn)
.attr('y', function(d) {
return y(d.value) - 5;
})
.attr('width', x.bandwidth())
.attr('height', function(d) {
return height - y(d.value);
});
// 矩形文字
chart.append('text').attr('fill', '#FFF')
.attr('x', function(d) {
return x(d.key) + 14;
})
.attr('y', function(d) {
return y(y.domain()[0]);
})
.transition()
.delay(function(d, i) {
return (i + 1) * 100
})
.duration(2000).ease(d3.easeBounceIn)
.attr('y', function(d) {
return y(d.value);
})
.attr('dx', function(d) {
return (x.bandwidth() - padding.left) / 2;
})
.attr('dy', 20)
.text(function(d) {
return d.value
});
// 悬浮提示框
var tooltip = d3.select('body').append('div');

// hover事件
chart.on('mouseover', function() {
d3.select(this).attr('opacity', 0.5);
// 悬浮在直方图上时，显示提示框
tooltip.html('我是提示框').transition().duration(500).style('left', d3.event.pageX - 20)
.style('top', d3.event.pageY + 20).style('opacity', 1.0);
}).on('mouseout', function() {
d3.select(this).transition().delay(100).duration(500).attr('opacity', 1.0);
});
// 当鼠标移出svg画布时，就将提示框隐藏掉，考虑到鼠标移出时显示的动画还未完成，需要加transition()过滤
svg.on('mouseout', function() {
tooltip.transition().style('opacity', 0);

});
