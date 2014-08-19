$(document).ready(function(){
  var plot1 = $.jqplot('chart2', [goog],  { 
      title: 'Google, Inc.', 
      series: [{ 
          label: 'Google, Inc.', 
          neighborThreshold: -1 
      }], 
      axes: { 
          xaxis: { 
              renderer: $.jqplot.DateAxisRenderer,
              min:'August 1, 2007 16:00:00', 
              tickInterval: '4 months', 
              tickOptions:{formatString:'%Y/%#m/%#d'} 
          }, 
          yaxis: { 
              tickOptions:{formatString:'$%.2f'} 
          } 
      }, 
      cursor:{ 
        show: true,
        zoom:true, 
        showTooltip:false
      } 
  });
});