# AutoReplicator

参考《张江·复杂科学前沿27讲-23 冯·诺伊曼：探索复杂科学核心问题第一人》  
AutoReplicator is a Python simulation of self-replicating cells based on the concept of von Neumann's self-replicating machines. The project models a grid of cells that follow simple rules to replicate and evolve over time, mimicking basic life-like behavior similar to Conway's Game of Life.

## Features
- Random initialization of cells
- Simulates cell reproduction based on neighboring states
- Step-by-step visual updates of the grid
- Customizable grid size and simulation steps

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Ody-trek/AutoReplicator.git
2. Make sure you have Python installed (version 3.x).
3. Run the simulation:
   ```bash
   python main.py

## Usage
You can configure the number of simulation steps and grid size in the run_simulation function inside main.py. By default, the simulation runs for 15 steps on a 10x10 grid.
Example:
run_simulation(steps=20, rows=15, cols=15)

## How It Works
The simulation is based on a grid of cells, where each cell can either be 'alive' or 'dead'. The state of each cell is updated according to the number of alive neighbors it has:
- A live cell with fewer than 2 or more than 3 live neighbors dies.
- A dead cell with exactly 3 live neighbors comes to life.
These simple rules can create complex and fascinating behaviors over time, including self-replication, survival, and death.

## Future Plans
- Add more complex cell behaviors.
- Introduce patterns that can evolve over time.
- Enable visualization with graphical output.

## Contributions
Contributions are welcome! Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.


