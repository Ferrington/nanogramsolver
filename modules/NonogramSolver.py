class NonogramSolver:

	def __init__(self, row_def, col_def):

		self.rows = len(row_def)
		self.cols = len(col_def)
		self.row_def = row_def
		self.col_def = col_def
		self.grid = [[0] * self.cols for _ in range(self.rows)]

	def solve(self):
		changed = True
		while changed:
			changed = self._solve_rows()

		if self._is_solved():
			return {'grid': self.grid, 'solved': True}
		else:
			return {'grid': self.grid, 'solved': False}

	def _solve_rows(self):
		changed = False

		for i, rule in enumerate(self.col_def):
			col = self._get_solved_row(rule, [x[i] for x in self.grid])
			for j, val in enumerate(col):
				if val and self.grid[j][i] != val:
					changed = True
				self.grid[j][i] = val
		for i, rule in enumerate(self.row_def):
			row = self._get_solved_row(rule, self.grid[i])
			for j, val in enumerate(row):
				if val and self.grid[i][j] != val:
					changed = True
				self.grid[i][j] = val

		return changed

	def _get_solved_row(self, rule, row):
		valid_permutations = []
		for permutation in self._generate_permutations(rule, row):
			permutation += [1] * (len(row) - len(permutation))
			for i, j in zip(row, permutation):
				if i > 0 and i != j:
					break
			else:
				valid_permutations.append(permutation)

		new_row = valid_permutations[0]
		for permutation in valid_permutations[1:]:
			new_row = [n if n == r else 0 for n, r in zip(new_row, permutation)]

		return new_row

	def _generate_permutations(self, values, row, n=0):
		if values and values[0]:
			current = values[0]
			other = values[1:]
			for i in range(len(row) - sum(other) - len(other) + 1 - current):
				if 1 not in row[i:i + current]:
					for j in self._generate_permutations(other, row[i + current + 1:], 1):
						yield [1] * (i + n) + [2] * current + j
		else:
			yield []

	def _is_solved(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.grid[i][j] == 0:
					return False

		return True;

	def _print_grid(self, final=False):
		for row in self.grid:
			for col in row:
				if final and col == '1':
					print(' ', sep='', end='')
				else:
					print(col, sep='', end='')
			print('')
		print('')
