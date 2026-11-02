fetch(`http://${location.hostname}:5000/api/hello`)
  .then(r => r.json())
  .then(d => { document.getElementById("msg").textContent = d.message; })
  .catch(() => { document.getElementById("msg").textContent = "Backend not reachable ❌"; });