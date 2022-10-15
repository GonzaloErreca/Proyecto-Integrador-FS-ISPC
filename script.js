function iniciarMap(){
	var coord = {lat:-32.90031 ,lng:-68.80960};
	var map = new google.maps.Map(document.getElementById('map'),{
		zoom: 10,
		center: coord
	});
	var marker = new google.maps.Marker({
		position: coord,
		map: map
	})
}
  
