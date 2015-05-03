$(function(){

        var ip = $("#ip").html()    
        var hdata = [];
        var ddata = [];
        var ddata3 = [];
  

    function drawChartMin(data,container,titulo, ytext, legend,interval){
        //console.log(data[0] + " "+titulo)

       Highcharts.setOptions({
            global: {
                useUTC: false
            },
            lang: {
                months: ['Enero', 'Febrero', 'Marzo', 'Avril', 'Mai', 'Juin',  'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
                shortMonths: [ "Ene" , "Feb" , "Mar" , "Abr" , "May" , "Jun" , "Jul" , "Ago" , "Sep" , "Oct" , "Nov" , "Dic"],
                weekdays: ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'],
                downloadJPEG: "Descargar como JPG",
                printChart:"Imprimir Grafico",
                weekdays: ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
            }
        });


        $(container).highcharts({
        chart: {
            zoomType: 'x'
        },
        title: {
            text: titulo
        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                    'Click y arrastre en el area que desea hacer zoom' :
                    'Pinch the chart to zoom in'
        },
        xAxis: {
            type: 'datetime',
        },
        tooltip: {
            //xDateFormat: '%Y-%m-%d',
            shared: true,
            valueSuffix: ''
        },
        yAxis: {
            title: {
                text: ytext
            }
        },
        legend: {
            enabled: true
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1},
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },
        
        series: [{
            type: 'area',
            name: legend,
            pointInterval: interval,
            data: data,
            pointStart:data[0].date

            }]
        });
    }


var gaugeOptions = {

        chart: {
            type: 'solidgauge'
        },

        title: {
            text: ""
        },

        pane: {
            center: ['50%', '85%'],
            size: '100%',
            startAngle: -90,
            endAngle: 90,
            background: {
                backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || '#EEE',
                innerRadius: '60%',
                outerRadius: '100%',
                shape: 'arc'
            }
        },

        tooltip: {
            enabled: false
        },

        // the value axis
        yAxis: {
            stops: [
                [0.25, '#55BF3B'], // green
                [0.5, '#DDDF0D'], // blue
                [0.75, '#ff6666'], // yellow
                [0.99, '#DF5353'] // red
            ],
            lineWidth: 0,
            minorTickInterval: null,
            tickPixelInterval: 500,
            tickWidth: 0,
            title: {
                y: -75
            },
            labels: {
                y: 25
            }
        },

        plotOptions: {
            solidgauge: {
                dataLabels: {
                    y: 10,
                    borderWidth: 0,
                    useHTML: true
                }
            }
        }
    };

      $.ajax({
                    url: '/gestion/json/mem/'+ip,
                    type: 'get',
                    dataType: 'json',
                     success: function(data) {
                        ram = data.ram;
                        used_ram = data.used_ram;
                        used_swap = data.swap - data.free_swap
                        swap = data.swap 
                            // The speed gauge###############
                            $('#chartdiv').highcharts(Highcharts.merge(gaugeOptions, {
                                yAxis: {
                                    min: 0,
                                    max: ram,
                                    title: {
                                        text: 'RAM'
                                    }
                                },

                                credits: {
                                    enabled: false
                                },

                                series: [{
                                    name: 'Speed',
                                    data: [used_ram],
                                    dataLabels: {
                                        format: '<div style="text-align:center"><span style="font-size:14px;color:' +
                                            ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y} de '+ram+'</span><br/>' +
                                               '<span style="font-size:12px;color:silver">MB</span></div>'
                                    },
                                    tooltip: {
                                        valueSuffix: ' MB'
                                    }
                                }]
                            }));
//#########################################################
    $('#swap').highcharts(Highcharts.merge(gaugeOptions, {
                                yAxis: {
                                    min: 0,
                                    max: swap,
                                    title: {
                                        text: 'SWAP'
                                    }
                                },

                                credits: {
                                    enabled: false
                                },

                                series: [{
                                    name: 'Speed',
                                    data: [used_swap],
                                    dataLabels: {
                                        format: '<div style="text-align:center"><span style="font-size:14px;color:' +
                                            ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y} de '+swap+'</span><br/>' +
                                               '<span style="font-size:12px;color:silver">MB</span></div>'
                                    },
                                    tooltip: {
                                        valueSuffix: ' MB'
                                    }
                                }]

    }));

                    }
        })  
 $.ajax({
                                    url: '/gestion/json/load/'+ip,
                                    type: 'get',
                                    dataType: 'json',
                                     success: function(data) {
                                        load = data.load;
                                        
                                            // The speed gauge###############
                                            $('#load_avg').highcharts(Highcharts.merge(gaugeOptions, {
                                                yAxis: {
                                                    min: 0,
                                                    max: 100,
                                                    title: {
                                                        text: 'Load avg'
                                                    }
                                                },

                                                credits: {
                                                    enabled: false
                                                },

                                                series: [{
                                                    name: 'Speed',
                                                    data: [load],
                                                    dataLabels: {
                                                        format: '<div style="text-align:center"><span style="font-size:14px;color:' +
                                                            ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y} de 100</span><br/>' +
                                                               '<span style="font-size:12px;color:silver">%</span></div>'
                                                    },
                                                    tooltip: {
                                                        valueSuffix: ' MB'
                                                    }
                                                }]
                                            }));

                                    }
 })  


// Bring life to the dials
    setInterval(function () {
        $.ajax({
                    url: '/gestion/json/mem/'+ip,
                    type: 'get',
                    dataType: 'json',
                     success: function(data) {
                        ram = data.used_ram;
                        used_ram = data.used_ram;
                                // Speed
                        var chart = $('#chartdiv').highcharts(),
                            point,
                            newVal,
                            inc;

                        if (chart) {
                            point = chart.series[0].points[0];
                            //inc = Math.round((Math.random() - 0.5) * 100);
                            newVal = point.y + inc;

                            if (newVal < 0 || newVal > 100) {
                                newVal = point.y - inc;
                            }

                            point.update(used_ram);
                        }
                }
        })

        $.ajax({
                    url: '/gestion/json/load/'+ip,
                    type: 'get',
                    dataType: 'json',
                     success: function(data) {
                        load = data.load;
                        $("#lavg").html(data.load)
                                // Speed
                        var chart2 = $('#load_avg').highcharts(),
                            point2,
                            newVal,
                            inc;

                        if (chart2) {
                            point2 = chart2.series[0].points[0];
                            //inc = Math.round((Math.random() - 0.5) * 100);
                            newVal = point2.y + inc;

                            if (newVal < 0 || newVal > 100) {
                                newVal = point2.y - inc;
                            }

                            point2.update(load);
                        }
                }
        })
    }, 5000);


    $('#tabs').on('selected', function (event) 
            { 
                var selectedTab = event.args.item;
                if(selectedTab==7){
                    //_Historial de Porc
                    $.ajax({
                        url: '/gestion/json/loadh/'+ip,
                        type: 'get',
                        dataType: 'json',
                         success: function(data2) {
                            for(var i=0; i < data2.length;i++){                            
                                date = new Date(data2[i].year, data2[i].month -1, data2[i].day, data2[i].hour,data2[i].min);
                                ddata.push([
                                   date,
                                   parseFloat(data2[i].load1)
                                ]);
                            }
                            
                            drawChartMin(ddata,'#loadHist','Historial de carga de procesador para '+ip,'Usado %','Uso %',(60 * 1000))
                        }
                    })
                }
                if(selectedTab==6){
                    $.ajax({
                        url: '/gestion/json/memh/'+ip,
                        type: 'get',
                        dataType: 'json',
                         success: function(data) {
                            for(var i=0; i < data.length;i++){                            
                                perc = ( data[i].mem_used *100 / data[i].mem).toFixed(2)
                                date = new Date(data[i].year, data[i].month -1, data[i].day, data[i].hour, data[i].min);
                                hdata.push([
                                   date,
                                   parseFloat(perc)
                                ]);
                            }
                            
                            drawChartMin(hdata,'#MemHist','Historial de uso de memoria RAM para '+ip,'Memoria usada %','Uso de RAM',60 * 1000)
                        }
                    })
                }
                if(selectedTab==8){
                    $.ajax({
                        url: '/gestion/json/diskh/'+ip,
                        type: 'get',
                        dataType: 'json',
                         success: function(data3) {
                            cat=[]
                            for(var i=0; i < data3.length;i++){                            
                                date = new Date(data3[i].year, data3[i].month -1, data3[i].day, data3[i].hour,data3[i].min);
                                ddata3.push([
                                  // date,
                                   parseFloat(data3[i].used)
                                ]);
                                cat.push(date)
                            }
                            
                            drawChartMin(ddata3,'#diskH','Historial uso de disco para '+ip,'Usado GB de particion '+data3[0].path,'Uso GB',(3600 * 1000))
                        }
                    })
                }

    });




})