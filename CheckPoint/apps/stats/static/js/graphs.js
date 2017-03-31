
google.charts.load('current', {'packages':['bar']});

function drawChart(inData,id) {
  console.log(inData,parseInt(id))
  var data = google.visualization.arrayToDataTable([
        ['Assignment', 'Correct answers in %',],
        [inData[0], ((inData[1]-inData[2])/inData[1])*100],

      ]);

      var options = {
        title: 'Population of Largest U.S. Cities',
        chartArea: {width: '50%'},
        hAxis: {
          title: 'Total Population',
          minValue: 0
        },
        vAxis: {
          title: 'City'
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('chart'+id));
      chart.draw(data, options);
}
