# Simple smoke-test for the API: creates a movie and a review, lists them, then cleans up.
$base = 'http://127.0.0.1:8000/api'

Write-Host "Creating movie..."
$movie = Invoke-RestMethod -Uri "$base/movies/" -Method Post -Body (@{title="Test Movie"; description="Smoke test"} | ConvertTo-Json) -ContentType 'application/json'
Write-Host "Created movie id=$($movie.id)"

Write-Host "Creating review..."
$review = Invoke-RestMethod -Uri "$base/reviews/" -Method Post -Body (@{movie=$movie.id; rating=5; content="Great"} | ConvertTo-Json) -ContentType 'application/json'
Write-Host "Created review id=$($review.id)"

Write-Host "Listing movies..."
Invoke-RestMethod -Uri "$base/movies/" -Method Get | ConvertTo-Json -Depth 4 | Write-Host

Write-Host "Listing reviews..."
Invoke-RestMethod -Uri "$base/reviews/" -Method Get | ConvertTo-Json -Depth 4 | Write-Host

Write-Host "Cleaning up..."
Invoke-RestMethod -Uri "$base/reviews/$($review.id)/" -Method Delete
Invoke-RestMethod -Uri "$base/movies/$($movie.id)/" -Method Delete

Write-Host "Smoke-test complete."
