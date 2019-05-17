import averageData from './data/average_arriving_by_day.js'
import drawAverageTimeByDay from './draw/drawAverageTimeByDay.js'
import lateToNotLate from './data/lateToNotLate.js'
import lateNotLatePieChart from './draw/lateNotLatePieChart.js'
import personInDayData from './data/person_in_day.js'
import drawPersonInDay from './draw/personInDay.js'




drawAverageTimeByDay(averageData)
lateNotLatePieChart(lateToNotLate)
drawPersonInDay(personInDayData)