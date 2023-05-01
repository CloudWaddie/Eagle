part1 = """<!DOCTYPE html>
<html>
<head>
<title>eagler</title>
<meta charset="UTF-8" />
<link type="image/x-icon" rel="shortcut icon" href="data:image/x-icon;base64,AAABAAEAICAQAAEABADoAgAAFgAAACgAAAAgAAAAQAAAAAEABAAAAAAAgAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAACAAAAAgIAAgAAAAIAAgACAgAAAgICAAMDAwAAAAP8AAP8AAAD//wD/AAAA/wD/AP//AAD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd3d3d3d3d3d3d3d3d3d3cHiIiIiIiIiIiIiIiIiIiHB4f/////////////////hweH/////////////////4cHh/////cAAHiI//////+HB4f///8REREAiIj/////hweH///3GNmREHAAAIiI/4cHh///8Y2ZmREHeqoIiI+HB4f///GNmZmRB3qqIIiIhweH///xjZmZkQd6qiIIiIcHh///8Y2ZmZEHqqoiD/+HB4f///cY2ZmRd6qqIg//hweH////EY2ZEXqqqiIP/4cHh/////cREXL6qqoiD/+HB4f////////y////Ig//hweH/////////yIiIoIP/4cHh//////////yIiIoD/+HB4f//////////yIiIn//hweH/////////////////4cHh/////////////////+HB4d3d3d3d3d3d3d3d3d3hweIiIiIiIiIiIiIiIiIiIcHhMwiRERERERERAAAAAAHB4TsokRERERERESICICIBweEETNEREREREREiAiAiAcHhJGzRERERERERERERERHB4iIiIiIiIiIiIiIiIiIhwd3d3d3d3d3d3d3d3d3d3cAAAAAAAAAAAAAAAAAAAAAD//////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/////w==" />
<script type="text/javascript">
window.addEventListener("load", function(){
window.minecraftOpts = [
"game_frame",createAssetURI("assets"),
"CgAACQAHc2VydmVycwoAAAABCAACaXAAIHdzKHMpOi8vIChhZGRyZXNzIGhlcmUpOihwb3J0KSAvCAAEbmFtZQAIdGVtcGxhdGUBAAtoaWRlQWRkcmVzcwEIAApmb3JjZWRNT1REABl0aGlzIGlzIG5vdCBhIHJlYWwgc2VydmVyAAA="
];
(function(){
var q = window.location.search;
if(typeof q === 'string' && q.startsWith("?")) {
	q = new URLSearchParams(q);
	var s = q.get("server");
	if(s) window.minecraftOpts.push(s);
}
})();
main();
});
</script>
<script type="text/javascript">
function createAssetURI(el) {
	var eee = document.getElementById(el);
	var str = eee.innerText;
	eee.remove();
	return "data:application/octet-stream;base64," + str.trim();
}
</script>
<script type="text/javascript">"""
classesJs = ""
part2 = """
</script>
</head>
<body style="margin:0px;width:100vw;height:100vh;" id="game_frame">
<div style="display:none;" id="assets">
"""
assets = ""
part3 = """
</div>
</body>
</html>"""

with open('assets.epk', 'r') as f:
    assets = f.read()
    
with open('classes.js', 'r') as f:
    classesJs = f.read()

with open('classes.js.map', 'r') as f:
    classesJs += f.read()

with open('output.html', 'w') as f:
    data = part1+classesJs+part2+assets+part3
    f.write(data)
