$(document).ready(function(){
  var dom = document.getElementById('chart-container');
  var myChart = echarts.init(dom, null, {
    renderer: 'canvas',
    useDirtyRect: false
  });
  var app = {};
  
  var option;

  app.configParameters = {
    rotate: {
      min: -90,
      max: 90
    },
    align: {
      options: {
        left: 'left',
        center: 'center',
        right: 'right'
      }
    },
    grid: {
      options: {
        left: '300px'
      }
    },
    verticalAlign: {
      options: {
        top: 'top',
        middle: 'middle',
        bottom: 'bottom'
      }
    },
    distance: {
      min: 0,
      max: 100
    }
  };
  app.config = {
    rotate: 90,
    align: 'left',
    verticalAlign: 'middle',
    position: 'insideBottom',
    distance: 15,
   
  };
  const labelOption = {
    show: true,
    position: app.config.position,
    distance: app.config.distance,
    align: app.config.align,
    verticalAlign: app.config.verticalAlign,
    rotate: app.config.rotate,
    formatter: '{c}  {name|{a}}',
    fontSize: 16,
    rich: {
      name: {}
    }
  };
  option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    legend: {
      data: ['Accuracy', 'Docs Processed', 'Error', 'Coin collected', 'Medals earned']
    },
    xAxis: [
      {
        type: 'category',
        axisTick: { show: false },
        data: ['May', 'June', 'July', 'August', 'September'],
        
      },
      
    ],
    yAxis: [
      {
       show:false
      }
    ],
    series: [
      {
        name: 'Accuracy',
        type: 'bar',
        barGap: 0,
        label: labelOption,
        emphasis: {
          focus: 'series'
        },
        data: [98.3, 98, 93, 90, 99]
      },
      {
        name: 'Docs Processsed',
        type: 'bar',
        label: labelOption,
        emphasis: {
          focus: 'series'
        },
        data: [313, 445, 513, 610, 546]
      },
      {
        name: 'Error',
        type: 'bar',
        label: labelOption,
        emphasis: {
          focus: 'series'
        },
        data: [2, 4, 3, 1, 5]
      },
      {
        name: 'Coins Collected',
        type: 'bar',
        label: labelOption,
        emphasis: {
          focus: 'series'
        },
        data: [95, 57,64, 96, 91]
      }, {
        name: 'Medals earned',
        type: 'bar',
        label: labelOption,
        emphasis: {
          focus: 'series'
        },
        data: [10,5,6,11,12]
      }
    ],
    
  };
  if (option && typeof option === 'object') {
    myChart.setOption(option);
  }
  
  window.addEventListener('resize', myChart.resize);


// Pie Chat

var dom = document.getElementById('pie-container');
var myChart = echarts.init(dom, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var app = {};

var option;

option = {
   tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: '50%',
      data: [
        { value: 175, name: '175 Docs left!' },
        { value: 75, name: '75 Docs Completed' },
        { value: 6, name: '6 fields with low accuracy' },
        { value: 15, name: 'No of documents for scanning' },
        { value: 3, name: 'TAT missed' }
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};

if (option && typeof option === 'object') {
  myChart.setOption(option);
}

window.addEventListener('resize', myChart.resize);

});

