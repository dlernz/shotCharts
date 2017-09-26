var width = window.innerWidth-30 || 900;
if (width>1000) {
	width=1000
}
var stage = new Kinetic.Stage({
  container: 'container',
  width: width,
  height: (.716)*width,
  scaleX:width/900,
  scaleY:width/900,
});

var circlayer = new Kinetic.Layer({
	hitGraphEnabled: true,
	transformsEnabled: 'none',
});

var court = new Kinetic.Layer();
stage.add(circlayer);

var rim = new Kinetic.Shape({
	sceneFunc: function(context) {
		context.beginPath();
		context.moveTo(344.5,50);
		context.arc(450,144.5,144,-.7279,3.8679)
   		context.lineTo(344.5,50);
		context.closePath();
		context.fillStrokeShape(this);
	},
	fillRed:50,
	fillGreen:250,
	fillBlue:50,
	fillAlpha:0,
	strokeWidth: 0,
	volume: 0,
	fg: 0
});
var midrange = new Kinetic.Shape({
	sceneFunc: function(context) {
		context.beginPath();
		context.moveTo(54,50);
		context.lineTo(54,302);
		context.arc(450,144.5,427.5,.87*Math.PI,0.125*Math.PI,true);
		context.lineTo(846,50);
		context.lineTo(554.5,50);
		context.arc(450,144.5,144,-.7279,3.8679);
		context.lineTo(54,50);
		context.closePath();
		context.fillStrokeShape(this);
	},
	fillRed:50,
	fillGreen:200,
	fillBlue:50,
	fillAlpha:0,
	strokeWidth: 0,
	volume: 0,
	fg: 0
});
var threes = new Kinetic.Shape({
	sceneFunc: function(context) {
		context.beginPath();
		context.moveTo(0,50);
		context.lineTo(54,50);
		context.lineTo(54,302);
		context.arc(450,144.5,427.5,.87*Math.PI,0.125*Math.PI,true);
		context.lineTo(846,50);
		context.lineTo(900,50);
		context.lineTo(900,650);
		context.lineTo(0,650);
		context.lineTo(0,50);
		context.closePath();
		context.fillStrokeShape(this);
	},
	fillRed:0,
	fillGreen:150,
	fillBlue:50,
	fillAlpha:0,
	strokeWidth: 0,
	volume: 0,
	fg: 0
});


// TODO: Refactor for drawing court, maybe assigning CSS properties, class name, ids -- refactor to HTML 5 canvas?
function nba_court_base() {
	var base=new Kinetic.Rect({x:54,y:50,width:792,height:255,fill:'#E0E0E0'})
	court.add(base)
	var base=new Kinetic.Rect({x:0,y:0,width:900,height:49,fill:'#a50026'})
	court.add(base)
	var base=new Kinetic.Rect({x:0,y:50,width:54,height:590,fill:'#E0E0E0'})
	court.add(base)
	var base=new Kinetic.Rect({x:846,y:50,width:54,height:590,fill:'#E0E0E0'})
	court.add(base)
	var base=new Kinetic.Rect({x:0,y:305,width:900,height:339,fill:'#E0E0E0'})
	court.add(base)
	var arc=new Kinetic.Arc({x:450,y:144.5,innerRadius:427.5,outerRadius:127.5,angle:136,fill:'#D0D0D0',rotationDeg:22})
	court.add(arc)
	var arc=new Kinetic.Arc({strokeWidth:2,stroke:'white',x:450,y:144.5,innerRadius:427.5,outerRadius:427.5,angle:136,rotationDeg:22,shadowColor:'#ffffff',shadowBlur:100})
	court.add(arc)
	var base=new Kinetic.Rect({x:342,y:50,width:216,height:342,fill:'#C0C0C0'})
	court.add(base)
	var base=new Kinetic.Rect({x:306,y:50,width:36,height:342,fill:'#C0C0C0'})
	court.add(base)
	var base=new Kinetic.Rect({x:558,y:50,width:36,height:342,fill:'#C0C0C0'})
	court.add(base)

	// var line=new Kinetic.Line({strokeWidth:2,points:[306,50,306,392],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	// court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[594,50,594,392],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[342,50,342,392],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[558,50,558,392],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[306,392,594,392],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[252,50,252,59],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[648,50,648,59],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[360,284,369,284],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[540,284,531,284],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[396,120.2,504,120.2],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[378,125.6,378,148.1],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[522,125.6,522,148.1],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[306,176,292.5,176],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[594,176,607.5,176],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[306,194,292.5,194],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[594,194,607.5,194],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[306,248,292.5,248],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[594,248,607.5,248],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[306,302,292.5,302],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[594,302,607.5,302],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var arc=new Kinetic.Arc({innerRadius:13.5,outerRadius:13.5,strokeWidth:2,stroke:'white',x:450,y:134.6,angle:360,rotationDeg:0,shadowColor:'#ffffff',shadowBlur:100})
	court.add(arc)
	var arc=new Kinetic.Arc({strokeWidth:2,stroke:'white',x:450,y:392,innerRadius:108,outerRadius:108,angle:180,shadowColor:'#ffffff',shadowBlur:100})
	court.add(arc)
	var arc=new Kinetic.Arc({strokeWidth:2,stroke:'white',x:450,y:148.1,innerRadius:72,outerRadius:72,angle:180,shadowColor:'#ffffff',shadowBlur:100})
	court.add(arc)
	var arc=new Kinetic.Arc({strokeWidth:2,stroke:'white',x:450,y:392,innerRadius:108,outerRadius:108,angle:180,dash:[22,22],rotationDeg:180,shadowColor:'#ffffff',shadowBlur:100})
	court.add(arc)
	var line=new Kinetic.Line({strokeWidth:2,points:[54,50,54,305.6],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)
	var line=new Kinetic.Line({strokeWidth:2,points:[846,50,846,305.6],stroke:'white',shadowColor:'#ffffff',shadowBlur:100})
	court.add(line)

	// var box = new Kinetic.Circle({x: 798,y: 34, radius:8,fill: '#a50026',shadowBlur:2,shadowColor:'#000000'});
	// court.add(box)
	// var box = new Kinetic.Circle({x: 798,y: 34, radius:7,fill: '#a50026',strokeWidth:1,stroke:'rgba(195,30,68,1)'});
	// court.add(box)
	court.add(rim)
	court.add(midrange)
	court.add(threes)
	stage.add(court)
}

function addPlayerShots(playerShots, parse = true){
    for (i = 0; i < playerShots.length; i++) {
        var curShot = playerShots[i];
        if (parse){
			curShot = JSON.parse(curShot);
		}
        var x = curShot['locX'];
        var y = curShot['locY'];
        var made = curShot['shotMadeFlag'];
        var toAdd = addShot(x,y,made);
        court.add(toAdd);
    }
    stage.add(court);
    return "done"
}

function addShot(x,y, made) {
    var old_radius = 467;
    var new_radius = 835
    var new_coords = get_new_coords(x, y, old_radius, new_radius);
    var toAdd;
    if(!made){
        toAdd = new Kinetic.Circle({x: new_coords["x"],y: new_coords['y'], radius:8,stroke: '#ff0000'});
    }
    else {
        toAdd = new Kinetic.Circle({x:  new_coords['x'], y: new_coords['y'], radius:8,stroke: '#008000'});
    }
    return toAdd
}

function get_new_coords(x, y, old_radius, new_radius){
    var x_offset = 450;
    var y_offset = 144.5;
    var x_theta = Math.acos(x/old_radius);
    var y_theta = Math.asin(y/old_radius);
    var new_x = new_radius*Math.cos(x_theta) + x_offset;
    var new_y = new_radius*Math.sin(y_theta) + y_offset;
    var coords = {"x": new_x, "y": new_y};
    return coords
}

$('#lightSlider').lightSlider({
	gallery: false,
	item: 3,
	loop: true,
	slideMargin: 200,
	thumbItem: 9,
	vertical:true,
	verticalHeight:500,
	vThumbWidth:100,
});


$(".dropdown-menu").css({"top": "60px", "left": "25px"});


function getPlayerInfo(playerShots, parse = true){
	var curShot = playerShots[0];
	if(parse){
		curShot = JSON.parse(curShot);
	}
	var playerName = curShot["playerName"];
	var teamName = curShot["teamName"];
	var shotsAttempted = playerShots.length;
	var shotsMade = 0;
	var triples = 0;
	for(var i = 0; i < playerShots.length; i++){
		var shot = playerShots[i];
		if (parse) {
			shot = JSON.parse(shot);
		}
		var shotType = shot["shotType"];
		var shotMadeFlag = shot["shotMadeFlag"];

		if (shotMadeFlag){
			shotsMade += 1;
		}

		if(shotMadeFlag == 1 && shotType == "3PT Field Goal"){
			triples += 1
		}
	}
	var fgPercent = 100.0*shotsMade/shotsAttempted;
	fgPercent = fgPercent.toFixed(2);
	var effFgPercent = 100*(shotsMade + 0.5*triples)/shotsAttempted; // (FG + 0.5 * 3P) / FGA
	effFgPercent = effFgPercent.toFixed(2);

	var playerData = {"playerName": playerName, "playerTeam": teamName, "shotsMade": shotsMade, "shotsAttempted": shotsAttempted,
		"effFgPercent": effFgPercent, "fgPercent": fgPercent};
	return playerData;
}

function injectPlayerInfo(playerData){
	 var playerInfoTable = $("#playerInfoTable");
	 var tableElts = $(playerInfoTable).find(".tableItem");
	 var data;
	 $(tableElts.each(function(){
	 	this.innerHTML = "";
	 	var id = this.id;
	 	var content = this.innerHTML;
		data = playerData[id];
		if (typeof data != 'undefined'){
			this.innerHTML = content + data;
		}
	 }))
}