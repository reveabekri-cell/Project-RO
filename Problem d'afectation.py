from ortools.sat.python import cp_model


costs = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4],
]

num_workers = len(costs)
num_tasks = len(costs[0])

model = cp_model.CpModel()


x = {}
for i in range(num_workers):
    for j in range(num_tasks):
        x[i, j] = model.new_bool_var(f'x_{i}_{j}')


for i in range(num_workers):
    model.add_exactly_one([x[i, j] for j in range(num_tasks)])

for j in range(num_tasks):
    model.add_exactly_one([x[i, j] for i in range(num_workers)]) 

model.minimize(
    sum(costs[i][j] * x[i, j] 
        for i in range(num_workers) 
        for j in range(num_tasks))
)


solver = cp_model.CpSolver()
status = solver.solve(model)


if status == cp_model.OPTIMAL:
    print(f'Coût total optimal = {int(solver.objective_value)}')  
    for i in range(num_workers):
        for j in range(num_tasks):
            if solver.value(x[i, j]) == 1:
                print(f'  Travailleur {i+1} -> Tâche {j+1} (coût={costs[i][j]})')
