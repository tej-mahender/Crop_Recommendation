document.getElementById('yield-form').addEventListener('submit', async (e) => {
  e.preventDefault();

  const feature1 = parseFloat(document.getElementById('feature1').value);
  const feature2 = parseFloat(document.getElementById('feature2').value);
  const feature3 = parseFloat(document.getElementById('feature3').value);

  const response = await fetch('http://localhost:8000/predict/yield', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ feature1, feature2, feature3 }),
  });

  if (response.ok) {
    const data = await response.json();
    document.getElementById('yield-result').textContent = `Predicted Yield: ${data.predicted_yield}`;
  } else {
    document.getElementById('yield-result').textContent = 'Error in prediction.';
  }
});
