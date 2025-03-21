def calculateStats(numbers):
  if not numbers:
    return {"avg": float('nan'), "max": float('nan'), "min": float('nan')}

  avg = sum(numbers) / len(numbers)
  max_num = max(numbers)
  min_num = min(numbers)

  return {"avg": avg, "max": max_num, "min": min_num}
