$(function() {
		    //...$( "#tabs" ).tabs();
		    $('#tabs').jqxTabs({ 
		    	width: '100%',
		    	//height: 350,
		    	position: 'top',
		    	theme: "bootstrap", 
		    	//collapsible: true
		    });


//GRIDS
	var ip = $("#ip").html()

	
    // prepare the data
    function get_data(data_url,fields){
    	var devices_source =
        	{
            	datatype: "json",
            	datafields:fields,
            	url: data_url,
            	pagesize: 8
        	};
    	var dataAdapter = new $.jqx.dataAdapter(devices_source);
    	return dataAdapter
    }

    var devices_url = "/gestion/json/devices/"+ip;
    var dev_fields = [	
    					{ name: 'desc', type: 'string' },
                		{ name: 'status', type: 'string' },
                	]

    var sw_url = "/gestion/json/sw/"+ip;
    var sw_fields = [	
    					{ name: 'name', type: 'string' },
    					{ name: 'path', type: 'string' },
    					{ name: 'parameters', type: 'string' },
    					{ name: 'type', type: 'string' },
                		{ name: 'status', type: 'string' },
                	]

    var proc_url = "/gestion/json/procs/"+ip;
    var proc_fields = [   
                        { name: 'name', type: 'string' },
                        { name: 'min', type: 'int' },
                        { name: 'max', type: 'int' },
                        { name: 'count', type: 'int' },
                        { name: 'err_msg', type: 'string' },
                        { name: 'flag', type: 'string' },
                        { name: 'date', type: 'string' },
                    ]
    

    
            $('#tabs').on('selected', function (event) 
            { 
                var selectedTab = event.args.item;
                if (selectedTab==4){
                    $("#devices_grid").jqxGrid(
                        {
                            theme: "bootstrap",
                            pageable: true,
                               
                            autoheight: true,
                            source: get_data(devices_url,dev_fields),
                            columnsresize: true,
                            filterable: true,
                            showfilterrow: true,
                            columns: [
                                { text: 'Dispositivo', dataField: 'desc', width: 400,cellsalign: 'center', align: 'center' },
                                { text: 'Estado', dataField: 'status', width: 200 , cellsalign: 'center', align: 'center'},
                            ]
                    }); 
                }
                if (selectedTab==5){
                    $("#sw_grid").jqxGrid(
                        {
                            theme: "bootstrap",
                            pageable: true,
                            autoheight: true,
                            width:'700px',
                            source: get_data(sw_url,sw_fields),
                            columnsresize: true,
                            filterable: true,
                            showfilterrow: true,
                            columns: [
                              { text: 'Nombre', dataField: 'name', width: 150,cellsalign: 'center', align: 'center' },
                              { text: 'Ruta', dataField: 'path', width: 200,cellsalign: 'center', align: 'center' },
                              { text: 'Parametros', dataField: 'parameters', width: 150,cellsalign: 'center', align: 'center' },
                              { text: 'Tipo', dataField: 'type', width: 100,cellsalign: 'center', align: 'center' },
                              { text: 'Estado', dataField: 'status', width: 100 , cellsalign: 'center', align: 'center'},
                            ]
                        });
                }
                if(selectedTab==2){
                     $("#procs").jqxGrid(
                        {
                            theme: "bootstrap",
                            pageable: true,
                            autoheight: true,
                            width:'100%',
                            source: get_data(proc_url,proc_fields),
                            columnsresize: true,
                            filterable: true,
                            showfilterrow: true,
                            columns: [
                              { text: 'Nombre', dataField: 'name', width: 150,cellsalign: 'left', align: 'center' },
                              { text: 'Min', dataField: 'min', width: 50,cellsalign: 'center', align: 'center' },
                              { text: 'Max', dataField: 'max', width: 50,cellsalign: 'center', align: 'center' },
                              { text: 'Count', dataField: 'count', width: 50,cellsalign: 'center', align: 'center' },
                              { text: 'Estado', dataField: 'flag', width: 70 , cellsalign: 'center', align: 'center'},
                              { text: 'Error Msg', dataField: 'err_msg', width: 300,cellsalign: 'left', align: 'center' },
                              { text: 'Ult. Actualiz.', dataField: 'date', width: 130,cellsalign: 'center', align: 'center' },
                            ]
                    });
                }
            });
		  
});