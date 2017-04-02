
google.charts.load('current', {'packages':['bar']});

function drawChart(inData,id,subject) {
  var dataArray = [['Assignment', 'Correct answers in %']];
  var tempArray = [];
  var average = 0
  /*
  for(var i = 0; i <inData.length; i++){
      if(i % 2 == 1 && i != 0){
        average += inData[i]
        tempArray.push(inData[i]);
        dataArray.push(tempArray);
        tempArray = []
      }
      else{
        tempArray.push(inData[i]);
      }
  }*/

  for(var i = 0; i <inData.length; i++){
      if(i % 2 == 1 && i != 0){
        average += inData[i]
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
        title: subject+ ' Overall: '+Math.round(average/(inData.length/2)*100 )/100+'%',
        chartArea: {width: '50%'},
        animation:{
        duration: 1000,
        easing: 'out',
        startup: true
      },
        hAxis: {
          title: 'Correct answers in %',
          minValue: 0,
          maxValue:200

        },
        vAxis: {
          title: 'Assignment'
        }
      };
      var result = google.visualization.data.group(
        // input data
        data,
        // key columns (columns to group by)
        [0],
        // third column (index 2) will be summed
        [{'column': 1, 'aggregation': google.visualization.data.sum, 'type': 'number'}]
      );

      var chart = new google.visualization.BarChart(document.getElementById('chart'+id));
      chart.draw(result, options);
}
