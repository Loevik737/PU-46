
google.charts.load('current', {'packages':['corechart']});
//google.charts.setOnLoadCallback(drawChart);


function drawChart(input) {
  console.log("bdsjf",input)
  var inputData = document.getElementById("data").value;
  var data = google.visualization.arrayToDataTable([
    ['Year', 'Sales', 'Expenses'],
    ['2004',  200,       400],
    ['2005',  1170,      460],
    ['2006',  660,       1120],
    ['2007',  1030,      540]
  ]);

  var options = {
    title:"hei paa deg",
    curveType: 'function',
    legend: { position: 'bottom' }
  };

  var chart = new google.visualization.LineChart(document.getElementById('chart1'));

  chart.draw(data, options);
}
