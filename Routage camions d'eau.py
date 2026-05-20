import pyomo.environ as pyo

n = 7  

dist = {}
raw_dist = [
    [0,  10, 15, 20, 25, 30, 35],
    [10, 0,  12, 18, 22, 28, 32],
    [15, 12, 0,  10, 15, 20, 25],
    [20, 18, 10, 0,  12, 18, 22],
    [25, 22, 15, 12, 0,  10, 15],
    [30, 28, 20, 18, 10, 0,  12],
    [35, 32, 25, 22, 15, 12, 0]
]

for i in range(n):
    for j in range(n):
        dist[i, j] = raw_dist[i][j]

demand = {0: 0, 1: 150, 2: 200, 3: 180, 4: 120, 5: 160, 6: 190}
capacity = 1000

model = pyo.ConcreteModel()
nodes = range(n)
customers = range(1, n)

model.x = pyo.Var(nodes, nodes, domain=pyo.Binary)
model.u = pyo.Var(nodes, domain=pyo.NonNegativeReals, bounds=(0, capacity))

model.obj = pyo.Objective(
    expr=sum(dist[i,j] * model.x[i,j] for i in nodes for j in nodes if i != j),
    sense=pyo.minimize
)

model.visit_in = pyo.ConstraintList()
for j in nodes:
    model.visit_in.add(sum(model.x[i,j] for i in nodes if i != j) == 1)

model.visit_out = pyo.ConstraintList()
for i in nodes:
    model.visit_out.add(sum(model.x[i,j] for j in nodes if i != j) == 1)

model.subtour = pyo.ConstraintList()
for i in nodes:
    for j in customers:
        if i != j:
            model.subtour.add(
                model.u[j] >= model.u[i] + demand[j] - capacity * (1 - model.x[i,j])
            )

for i in customers:
    model.subtour.add(model.u[i] >= demand[i])

solver = pyo.SolverFactory('glpk')
result = solver.solve(model, tee=False)

print("\n=== Resultats ===")
if (result.solver.status == pyo.SolverStatus.ok) and \
   (result.solver.termination_condition == pyo.TerminationCondition.optimal):
    print(f"Distance totale optimale = {pyo.value(model.obj):.2f} km")
    current_node = 0
    path = [0]
    while True:
        for j in nodes:
            if current_node != j and pyo.value(model.x[current_node, j]) > 0.5:
                path.append(j)
                current_node = j
                break
        if current_node == 0:
            break
    print("Route optimale:")
    print(" -> ".join(map(str, path)))
else:
    print("Aucune solution optimale trouvee.")