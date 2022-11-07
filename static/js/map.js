
function initMap() {
    const absolutefitness = { lat: 52.211388, lng: -7.203230 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 13,
      center: absolutefitness,
    });
    const marker = new google.maps.Marker({
      position: absolutefitness,
      map: map,
    });
  }
  
  window.initMap = initMap;