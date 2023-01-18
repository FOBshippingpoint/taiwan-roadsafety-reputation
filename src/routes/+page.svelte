<script>
	import { onMount } from 'svelte';
	import countries from '$lib/assets/countries.geo.json';
	import reputation from '$lib/assets/reputation.json';

	for (const r of reputation) {
		for (let f of countries.features) {
			if (f.properties.ADM0_A3 == r.ADM0_A3) {
				f.properties = { ...f.properties, ...r };
			}
		}
	}

	onMount(async () => {
		const L = await import('leaflet');
		const map = L.map('map').setView([24.9546286, 121.1913004], 3);

		map.attributionControl.addAttribution(
			'Estimated road traffic death rate data &copy; <a href="https://www.who.int/data/gho/data/indicators/indicator-details/GHO/estimated-road-traffic-death-rate-(per-100-000-population)">WHO</a>'
		);
		map.attributionControl.addAttribution(
			'Regions data &copy; <a href="https://github.com/AshKyd/geojson-regions">GeoJSON Regions</a>, <a href="https://www.naturalearthdata.com/about/">Natural Earth</a>'
		);

		const info = new L.Control();

		info.onAdd = function (map) {
			this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
			this.update();
			return this._div;
		};

		info.update = function (props) {
			this._div.innerHTML = props?.NAME_ZHT
				? `<h2>${props?.NAME_ZHT}</h2>` +
				  (props?.deathRate
						? `<div class='death-rate'>${props.deathRate}<span>(十萬人交通事故死亡率估計值)</span></div><hr/>` +
						  (props?.originalText
								? `<h3>道安資訊原文</h3><p>${props.originalText.replaceAll('\n', '<br/>')}</p><hr/>`
								: '') +
						  (props?.translatedText
								? `<h3>Google Translate 譯文</h3><p>${props.translatedText.replaceAll(
										'\n',
										'<br/>'
								  )}</p><hr/>`
								: '') +
						  (props?.reference
								? '資料來源：<a href="' +
								  encodeURI(props.reference) +
								  '">' +
								  props.reference +
								  '</a><br/>'
								: '')
						: '尚無資料')
				: '<h2>請選擇一個國家</h2>';
		};

		info.addTo(map);

		const geojson = L.geoJson(countries, {
			style: style,
			onEachFeature: onEachFeature
		}).addTo(map);

		function resetHighlight(e) {
			geojson.resetStyle(e.target);
		}

		info.isLock = false;

		function getColor(d) {
			return d > 40
				? '#800026'
				: d > 30
				? '#BD0026'
				: d > 20
				? '#FC4E2A'
				: d > 10
				? '#FEB24C'
				: d > 0
				? '#FED976'
				: '#FDFDFD';
		}

		function style(feature) {
			return {
				fillColor: getColor(feature.properties.deathRate),
				weight: 2,
				opacity: 1,
				color: 'white',
				dashArray: '1',
				fillOpacity: 0.7
			};
		}

		function highlightFeature(e) {
			var layer = e.target;

			layer.setStyle({
				weight: 2,
				color: '#666',
				dashArray: '',
				fillOpacity: 0.7
			});

			layer.bringToFront();
			if (!info.isLock) {
				info.update(layer.feature.properties);
			}
		}

		function clickFeature(e) {
			info.isLock = !info.isLock;
			const layer = e.target;
			info.update(layer.feature.properties);
			map.fitBounds(e.target.getBounds());
		}

		function onEachFeature(feature, layer) {
			layer.on({
				mouseover: highlightFeature,
				mouseout: resetHighlight,
				click: clickFeature
			});
			info.update();
		}


    // change layout for mobile or desktop
		const mql = window.matchMedia('only screen and (max-device-width: 480px)');

		function changePosition(matches) {
			if (matches) {
				// mobile
				map.attributionControl.setPosition('topright');
				info.setPosition('bottomright');
			} else {
				// desktop
				map.attributionControl.setPosition('bottomright');
				info.setPosition('topright');
			}
		}

		mql.addEventListener('change', (event) => changePosition(event.matches));
		changePosition(mql.matches);
	});
</script>

<div id="map" />
