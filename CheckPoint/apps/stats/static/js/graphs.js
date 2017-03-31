
google.charts.load('current', {'packages':['bar']});

function drawChart(inData,id,subject) {
  var dataArray = [['Assignment', 'Correct answers in %']];
  var tempArray = [];
  for(var i = 0; i <inData.length; i++){
      if(i % 2 == 1 && i != 0){
        tempArray.push(inData[i]);
        dataArray.push(tempArray);
        tempArray = []
      }
      else{
        tempArray.push(inData[i]);
      }
  }
  var data = google.visualization.arrayToDataTable(dataArray);

      var options = {
        title: subject,
        chartArea: {width: '50%'},
        hAxis: {
          title: 'Total Correct of 100%',
          minValue: 0,
          maxValue:100

        },
        vAxis: {
          title: 'Assignment'
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('chart'+id));
      chart.draw(data, options);
}
