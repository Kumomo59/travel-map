const map = L.map("map").setView([35.681, 139.767], 12);

// 地図タイル
L.tileLayer(
  "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
  {
    attribution: "&copy; OpenStreetMap contributors &copy; CARTO"
  }
).addTo(map);
// お店データをFlaskから取得
fetch("/shops")
  .then(res => res.json())
  .then(shops => {
      shops.forEach(shop => {
          const marker = L.marker([shop.lat, shop.lng]).addTo(map);
          marker.bindPopup(`<b>${shop.name}</b><br>${shop.memo}`);
      });
  });
