document.getElementById('cropForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.target;

  const data = {
    N: parseInt(form.N.value),
    P: parseInt(form.P.value),
    K: parseInt(form.K.value),
    temperature: parseFloat(form.temperature.value),
    humidity: parseFloat(form.humidity.value),
    ph: parseFloat(form.ph.value),
    rainfall: parseFloat(form.rainfall.value),
  };
  console.log(data);

  const response = await fetch('http://127.0.0.1:5000/recommend-crop', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  document.getElementById('result').innerText = result.crop
    ? `✅ Recommended Crop: ${result.crop}`
    : `❌ ${result.error}`;
});
