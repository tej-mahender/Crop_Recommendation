document.getElementById('cropForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.target;

  const data = {
    N: +form.N.value,
    P: +form.P.value,
    K: +form.K.value,
    temperature: +form.temperature.value,
    humidity: +form.humidity.value,
    ph: +form.ph.value,
    rainfall: +form.rainfall.value
  };

  const res = await fetch('http://127.0.0.1:5000/recommend-crop', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });

  const result = await res.json();
  document.getElementById('cropResult').innerText = result.recommended_crop
    ? `✅ Recommended Crop: ${result.recommended_crop}`
    : `❌ ${result.error}`;
});


document.getElementById('companionForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const crop = e.target.crop.value.trim().toLowerCase();

  const res = await fetch('http://127.0.0.1:5000/recommend-companions', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ crop })
  });

  const result = await res.json();
  document.getElementById('companionResult').innerText = result.companions
    ? `🌿 Companion Crops: ${result.companions.join(', ')}`
    : `❌ ${result.error}`;
});


document.getElementById('yieldForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.target;

  const data = {
    crop_year: +form.crop_year.value,
    season: form.season.value.trim(),
    crop: form.crop.value.trim().toLowerCase(),
    area: +form.area.value
  };

  const res = await fetch('http://127.0.0.1:5000/predict-yield', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });

  const result = await res.json();
  document.getElementById('yieldResult').innerText = result.predicted_yield
    ? `🌾 Predicted Yield: ${result.predicted_yield} tons`
    : `❌ ${result.error}`;
});
