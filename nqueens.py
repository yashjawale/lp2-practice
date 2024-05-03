def solveNQueens(n):
  col = []
  posDiag = []
  negDiag = []

  res = []
  board = [["_" for _ in range(n)] for _ in range(n)]

  def backtrack(r):
    if (r == n):
      copy = ["".join(row) for row in board]
      res.append(copy)
      return
    
    for c in range(n):
      if (c in col or (r+c) in posDiag or (r-c) in negDiag):
        continue
      col.append(c)
      posDiag.append(r+c)
      negDiag.append(r-c)
      board[r][c] = "Q"

      backtrack(r+1)

      col.remove(c)
      posDiag.remove(r+c)
      negDiag.remove(r-c)
      board[r][c] = "_"
  
  backtrack(0)

  return res

result = solveNQueens(4)

for i in result:
  for j in i:
    print(j)
  print("\n\n")

print("TOTAL RESULTS: clear", len(result))