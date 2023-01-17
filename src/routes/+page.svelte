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
    const L = await import('leaflet')
		const map = L.map('map').setView([24.9546286, 121.1913004], 3);

		const info = L.control();

		info.onAdd = function (map) {
			this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
			this.update();
			return this._div;
		};

		info.update = function (props) {
			this._div.innerHTML =
				`<h3><b>${props?.NAME_ZHT}</b> 對台交通安全資訊</h3>` +
				(props?.deathRate
					? '' +
					  (props?.originalText
							? '<br/><hr/><b>原文</b><br/>' +
							  props.originalText.replaceAll('\n', '<br/>') +
							  '<br/><hr/>'
							: '') +
					  (props?.translatedText
							? '<b>Google Translate 譯文</b><br/>' +
							  props.translatedText.replaceAll('\n', '<br/>') +
							  '<br/><hr/>'
							: '') +
					  (props?.reference
							? '資料來源：<a href="' +
							  encodeURI(props.reference) +
							  '">' +
							  props.reference +
							  '</a><br/>'
							: '') +
					  '<br />' +
					  props.deathRate +
					  ' 道路交通死亡率估計值 (每十萬人)'
					: '尚無資料');
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
		}

		function onEachFeature(feature, layer) {
			layer.on({
				mouseover: highlightFeature,
				mouseout: resetHighlight,
				click: clickFeature
			});
			info.update();
		}

		map.attributionControl.addAttribution(
			'Estimated road traffic death rate data &copy; <a href="https://www.who.int/data/gho/data/indicators/indicator-details/GHO/estimated-road-traffic-death-rate-(per-100-000-population)">WHO</a>'
		);
		map.attributionControl.addAttribution(
			'Regions data &copy; <a href="https://github.com/AshKyd/geojson-regions">GeoJSON Regions</a>, <a href="https://www.naturalearthdata.com/about/">Natural Earth</a>'
		);
	});
</script>

<div id="map" />
